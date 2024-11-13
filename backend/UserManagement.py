from fastapi import APIRouter, FastAPI, HTTPException, Depends, Request, Response
from fastapi.responses import JSONResponse
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session, declarative_base
from sqlalchemy.exc import SQLAlchemyError
from pydantic import  BaseModel, EmailStr, ValidationError, constr
import bcrypt
import jwt
from datetime import datetime, timedelta
from database import SessionLocal, get_db
from models import User
from dotenv import load_dotenv
import os
from fastapi import Request



# Load environment variables from .env file
load_dotenv()

# Secret key for JWT
SECRET_KEY = os.getenv("SECRET_KEY")

# Initialize APIRouter for modular routing
router = APIRouter()

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
            raise HTTPException(status_code=400, detail={"code": "EMAIL_TAKEN", "message": "The e-mail is already registered."})

        if not self.is_username_unique(db, self.username):
            raise HTTPException(status_code=400, detail={"code": "USERNAME_TAKEN", "message": "The username is already taken."})
        
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
            "token_version": user.token_version,
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
def authenticate_user(request: Request, db: Session = Depends(get_db)) -> User:
    token = request.cookies.get("jwtToken")
    if not token:
        raise HTTPException(status_code=403, detail="Token not provided")
    try:
        token = token.replace("Bearer ", "")  # Remove Bearer prefix if present
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        user_id = payload.get("user_id")
        token_version = payload.get("token_version")
        if not user_id or token_version is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        user = db.query(User).filter(User.id == user_id).first()
        if not user or user.token_version != token_version:
            raise HTTPException(status_code=401, detail="Token has been invalidated")
        return user
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

#This schema defines the fields that the user can update
class UserUpdate(BaseModel):
    email: EmailStr = None
    username: str = None
    password: str = None
    curp: str = None
    rfc: str = None
    name: str = None

@router.put("/update_user")
async def update_user(user_update: UserUpdate, user = Depends(authenticate_user), db: Session = Depends(get_db)):
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Check if email is already in use by another user
    if user_update.email and db.query(User).filter(User.email == user_update.email, User.id != user.id).first():
        raise HTTPException(status_code=400, detail="Email is already registered.")
    
    # Check if username is already in use by another user
    if user_update.username and db.query(User).filter(User.username == user_update.username, User.id != user.id).first():
        raise HTTPException(status_code=400, detail="Username is already taken.")
    
    # Update fields if they are provided
    if user_update.email is not None:
        user.email = user_update.email
    if user_update.username is not None:
        user.username = user_update.username
    if user_update.curp is not None:
        user.curp = user_update.curp
    if user_update.rfc is not None:
        user.rfc = user_update.rfc
    if user_update.name is not None:
        user.name = user_update.name

    try:
        db.commit()
        db.refresh(user)
    except SQLAlchemyError:
        db.rollback()
        raise HTTPException(status_code=500, detail="Failed to update user.")

    return {"message": "User updated successfully", "user": user}


@router.get("/profile")
async def get_user_profile(request: Request, user: User = Depends(authenticate_user)):
    try:
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return {
            "username": user.username,
            "email": user.email,
            "name": user.name,
            "curp": user.curp,
            "rfc": user.rfc
        }
    except HTTPException as e:
        raise e

@router.post("/logout")
async def logout_user(user: User = Depends(authenticate_user), db: Session = Depends(get_db)):
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Increment the token version to invalidate old tokens
    user.token_version += 1
    db.commit()

    response = JSONResponse(content={"message": "Logged out successfully"})
    response.delete_cookie(key="jwtToken")
    return response
