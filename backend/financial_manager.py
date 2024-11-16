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
    income = "income"
    expense = "expense"


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
        Transaction.type == transaction_data.type.value
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
        type=transaction_data.type.value
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
            Transaction.type == transaction_type.value
        ).all()
        if not transactions:
            return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "No transactions found in this period"})
        
        return transactions

    except SQLAlchemyError as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Database error occurred")



@router.get("/lastIncome", status_code=status.HTTP_200_OK)
def get_last_income(
    db: Session = Depends(get_db),
    user: User = Depends(authenticate_user)
):
    try:
        # Query to fetch the latest income transaction for the user
        last_income = (
            db.query(Transaction)
            .filter(
                Transaction.user_id == user.id,
                Transaction.type == TransactionType.income.value  # Ensure it's an income
            )
            .order_by(Transaction.date_time.desc())  # Order by date_time descending
            .first()
        )

        # If no income transaction exists, return a message
        if not last_income:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="No income transactions found for the user."
            )

        # Return the last income as a JSON response
        return {
            "id": last_income.id,
            "amount": str(last_income.amount),  # Convert Decimal to string for JSON serialization
            "description": last_income.description,
            "date_time": last_income.date_time,
        }

    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while fetching the last income."
        )

@router.get("/lastExpense", status_code=status.HTTP_200_OK)
def get_last_expense(
    db: Session = Depends(get_db),
    user: User = Depends(authenticate_user)
):
    try:
        # Query to fetch the latest expense transaction for the user
        last_expense = (
            db.query(Transaction)
            .filter(
                Transaction.user_id == user.id,
                Transaction.type == TransactionType.expense.value  # Ensure it's an expense
            )
            .order_by(Transaction.date_time.desc())  # Order by date_time descending
            .first()
        )

        # If no expense transaction exists, return a message
        if not last_expense:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="No expense transactions found for the user."
            )

        # Return the last expense as a JSON response
        return {
            "id": last_expense.id,
            "amount": str(last_expense.amount),  # Convert Decimal to string for JSON serialization
            "description": last_expense.description,
            "date_time": last_expense.date_time,
        }

    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while fetching the last expense."
        )

@router.get("/allIncomes", status_code=200)
def get_all_incomes(
    db: Session = Depends(get_db),
    user: User = Depends(authenticate_user)
):
    """
    Get all incomes for the authenticated user, excluding tags.
    """
    try:
        # Query all incomes for the user
        incomes = db.query(Transaction).filter(
            Transaction.user_id == user.id,
            Transaction.type == "income"  # Filter only incomes
        ).all()

        if not incomes:
            return {"message": "No incomes found."}

        # Transform data to exclude tags
        result = [
            {
                "id": income.id,
                "amount": income.amount,
                "description": income.description,
                "date_time": income.date_time,
                "type": income.type
            }
            for income in incomes
        ]

        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail="Error fetching incomes.")

