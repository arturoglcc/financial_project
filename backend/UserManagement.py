from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session, declarative_base
from pydantic import  BaseModel, EmailStr, ValidationError
from passlib.context import CryptContext
from database import SessionLocal
from models import User

app = FastAPI()

# Password hashing configuration
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Dependency to get a session per request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    email = Column(String(50), unique=True, index=True)
    password_hashed = Column(String(100))


class UserBuilder(BaseModel):
    email: EmailStr
    username: str
    password: str

    def is_email_unique(self, db: Session, email: str) -> bool:
        return not db.query(User).filter(User.email == email).first()

    def _hash_password(self, password: str) -> str:
        return pwd_context.hash(password)
    
    def build(self, db: Session) -> User:
        if not self.is_email_unique(db, self.email):
            raise HTTPException(status_code=400, detail="The e-mail is already registered.")
        
        password_hashed = self._hash_password(self.password)
        
        new_user = User(
            username=self.username,
            email=self.email,
            password_hashed=password_hashed
        )
        return new_user

@app.post("/create-user")
async def create_user(user_data: UserBuilder, db: Session = Depends(get_db)):
    try:
        # Build the User object
        new_user = user_data.build(db)
        
        # Attempt to add and commit to the database
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