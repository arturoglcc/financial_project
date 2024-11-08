from sqlalchemy import Boolean, Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = "users"  # Specifies the table name in the database

    id = Column(Integer, primary_key=True, index=True)  
    email = Column(String(255), unique=True, index=True, nullable=False)  
    username = Column(String(255), unique=True, index=True, nullable=False)  
    password_hashed = Column(String(255), nullable=False)
    curp = Column(String(18), unique=True, nullable=True)
    rfc = Column(String(13), unique=True, nullable=True)
    name = Column(String(255), nullable=True)
