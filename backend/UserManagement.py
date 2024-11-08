from fastapi import APIRouter, FastAPI, HTTPException, Depends, Request, Response
from fastapi.responses import JSONResponse
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session, declarative_base
from sqlalchemy.exc import SQLAlchemyError
from pydantic import  BaseModel, EmailStr, ValidationError
import bcrypt
import jwt
from datetime import datetime, timedelta
from database import SessionLocal
from models import User
from dotenv import load_dotenv
import os 


# Load environment variables from .env file
load_dotenv()

# Secret key for JWT
SECRET_KEY = os.getenv("SECRET_KEY")

# Initialize APIRouter for modular routing
router = APIRouter()

# Dependency to get a data base session per request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# UserBuilder creates a new user instance
class UserBuilder(BaseModel):
    email: EmailStr
    username: str
    password: str

    def is_email_unique(self, db: Session, email: str) -> bool:
        return not db.query(User).filter(User.email == email).first()

    def is_username_unique(self, db: Session, username: str) -> bool:
        return not db.query(User).filter(User.username == username).first()

    def _hash_password(self, password: str) -> str:
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_password.decode('utf-8')
    
    def build(self, db: Session) -> User:
        if not self.is_email_unique(db, self.email):
            raise HTTPException(status_code=400, detail="The e-mail is already registered.")

        if not self.is_username_unique(db, self.username):
            raise HTTPException(status_code=400, detail="The username is already taken.")
        
        password_hashed = self._hash_password(self.password)
        
        new_user = User(
            username=self.username,
            email=self.email,
            password_hashed=password_hashed
        )
        return new_user


@router.post("/signup")
async def create_user(user_data: UserBuilder, db: Session = Depends(get_db)):
    try:
        # Build the User object
        new_user = user_data.build(db)
        
        # Adding the User to the Database
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
    
    except HTTPException as e:
        raise e
    
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Failed to save user to the database.")
    
    except Exception as e:
        # Catch any other unexpected exceptions
        raise HTTPException(status_code=500, detail="An unexpected error occurred.")
    
    return {"message": "User created", "user": {"email": new_user.email, "username": new_user.username}}

class LoginRequest(BaseModel):
    username: str
    password: str

 # User login authentication function
def authenticate_login(db: Session, identifier: str, password: str) -> User:
    user = db.query(User).filter((User.username == identifier) | (User.email == identifier)).first()
    if not user:
        raise HTTPException(status_code=404, detail="Username or email not found")
    if not bcrypt.checkpw(password.encode('utf-8'), user.password_hashed.encode('utf-8')):
        raise HTTPException(status_code=401, detail="Incorrect password")
    return user  # Correct user and password


@router.post("/login")
async def login(response: Response, request: LoginRequest, db: Session = Depends(get_db)):
    user = authenticate_login(db, request.username, request.password)
     # Generate JWT token with user properties (including the id)
    expiration_time = datetime.utcnow() + timedelta(hours=1)
    token = jwt.encode(
        {
            "user_id": user.id,
            "username": user.username,
            "email": user.email,
            "exp": expiration_time
        },
        SECRET_KEY,
        algorithm="HS256"
    )

    # Set the JWT as an HttpOnly cookie
    response.set_cookie(
        key="jwtToken",
        value=token,
        httponly=True,
        secure=False,  # Set to True if using HTTPS
        samesite="Lax",  # Adjust as needed for cross-origin requests
        max_age=3600  # 1 hour in seconds
    )

    return JSONResponse(content={"message": "Inicio de sesión exitoso"}, headers=response.headers)

# Function to authenticate a user using JWT
def authenticate_user(token: str = Depends(lambda request: request.headers.get("Authorization"))):
    if not token:
        raise HTTPException(status_code=403, detail="Token not provided")
    try:
        token = token.replace("Bearer ", "")  # Remove Bearer prefix if present
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        user_id = payload.get("user_id")
        if not user_id:
            raise HTTPException(status_code=401, detail="Invalid token")
        return user_id
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")


@router.get("/me")
async def get_current_user(request: Request):
    token = request.cookies.get("jwtToken")
    if not token:
        print("Token not found in request cookies")
        raise HTTPException(status_code=403, detail="Token not provided")

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        print("Decoded payload:", payload)  # Debug line to check decoded token content
        username = payload.get("username")
        if not username:
            raise HTTPException(status_code=400, detail="Invalid token payload")
        return {"username": username}
    except jwt.ExpiredSignatureError:
        print("Token has expired")
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.InvalidTokenError:
        print("Invalid token")
        raise HTTPException(status_code=401, detail="Invalid token")
