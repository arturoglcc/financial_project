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
from UserManagement import authenticate_user

# Initialize APIRouter for modular routing
router = APIRouter()


# Define TransactionType Enum
class TransactionType(PyEnum):
    INCOME = "income"
    EXPENSE = "expense"


# Pydantic model for transaction data
class TransactionCreate(BaseModel):
    amount: Decimal
    description: str
    date: date
    type: TransactionType


# Function to add a transaction
@router.post("/addTransaction", status_code=status.HTTP_201_CREATED)
def add_transaction(
    transaction_data: TransactionCreate,
    db: Session = Depends(get_db),
    user: User = Depends(authenticate_user))
):
    # Check if a transaction with the same details already exists (ignoring tags)
    existing_transaction = db.query(Transaction).filter(
        Transaction.user_id == user.id,
        Transaction.amount == transaction_data.amount,
        Transaction.description == transaction_data.description,
        Transaction.date == transaction_data.date,
        Transaction.type == transaction_data.type
    ).first()
    
    if existing_transaction:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="An identical transaction already exists"
        )

    # Create a new transaction
    new_transaction = Transaction(
        user_id=user.id,
        amount=transaction_data.amount,
        description=transaction_data.description,
        date=transaction_data.date,
        type=transaction_data.type
    )
    
    # Add and commit the transaction to the database
    db.add(new_transaction)
    db.commit()
    db.refresh(new_transaction)

    return {"message": "Transaction added successfully", "transaction_id": new_transaction.id}
