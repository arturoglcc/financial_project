from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from passlib.context import CryptContext
from typing import Optional

app = FastAPI()

# passlib configuration for password hashes
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class User:
    def __init__(self, user_id: int, email: str, username: str, password_hashed: str):
        self.user_id = user_id
        self.email = email
        self.username = username
        self.password_hashed = password_hashed

connection = mysql.connector.connect(
    host="localhost",           
    user="user",                
    password="password",        
    database="financial-projectDB" 
)

cursor = connetion.cursor()

users_table = """
CREATE TABLE IF NOT EXISTS usuarios (
    id INT PRIMARY KEY,
    username VARCHAR(50),
    email VARCHAR(50),
    password-hashed VARCHAR(50)
)
"""
cursor.execute(users_table)
connetion.commit()


class UserBuilder(BaseModel):
    email: EmailStr
    username: str
    password: str

    def build(self) -> User:
        hashed_password = pwd_context.hash(self.password)
        user_id = 1  # Este id debería generarse en la base de datos en una implementación real
        return User(user_id=user_id, email=self.email, username=self.username, password_hashed=hashed_password)

@app.post("/create-user")
async def create_user(user_data: UserBuilder):
    new_user = user_data.build()
    # Aquí podrías agregar el nuevo usuario a la base de datos
    return {"message": "Usuario creado", "user": {"email": new_user.email, "username": new_user.username}}