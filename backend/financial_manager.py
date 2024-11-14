from fastapi import APIRouter, FastAPI, HTTPException, Depends, Request, Response, status
from fastapi.responses import JSONResponse
from sqlalchemy import Column, Integer, DateTime, DECIMAL, Text, Enum, ForeignKey
from sqlalchemy.orm import Session, declarative_base, relationship
from sqlalchemy.exc import SQLAlchemyError
from pydantic import  BaseModel
from decimal import Decimal
from datetime import datetime, timedelta
from database import SessionLocal, get_db
from models import User, Transaction
import os
from fastapi import Request
from UserManagement import authenticate_user
from enum import Enum
from typing import List, Optional

# Initialize APIRouter for modular routing
router = APIRouter()


# Define TransactionType Enum
class TransactionType(Enum):
    INCOME = "income"
    EXPENSE = "expense"


# Pydantic model for transaction data
class TransactionCreate(BaseModel):
    amount: Decimal
    description: str
    date_time: datetime
    tags: Optional[List[str]] = None
    type: TransactionType


# Function to add a transaction
@router.post("/addTransaction", status_code=status.HTTP_201_CREATED)
def add_transaction(
    transaction_data: TransactionCreate,
    db: Session = Depends(get_db),
    user: User = Depends(authenticate_user)):
    # Check if a transaction with the same details already exists (ignoring tags)
    existing_transaction = db.query(Transaction).filter(
        Transaction.user_id == user.id,
        Transaction.amount == transaction_data.amount,
        Transaction.description == transaction_data.description,
        Transaction.date_time == transaction_data.date_time,
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
        date_time=transaction_data.date_time,
        type=transaction_data.type
    )
    
    # Add and commit the transaction to the database
    db.add(new_transaction)
    db.commit()
    db.refresh(new_transaction)

    return {"message": "Transaction added successfully", "transaction_id": new_transaction.id}

@router.get("/transactions", response_model=list[TransactionCreate])
def get_transactions(
   start_date: datetime,
   end_date: datetime,
    transaction_type: TransactionType,
    db: Session = Depends(get_db),
    user: User = Depends(authenticate_user)
):
    try:
        transactions = db.query(Transaction).filter(
            Transaction.user_id == user.id,
            Transaction.date_time >= start_date,
            Transaction.date_time <= end_date,
            Transaction.type == transaction_type
        ).all()
        if not transactions:
            return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "No transactions found in this period"})
        
        return transactions

    except SQLAlchemyError as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Database error occurred")

