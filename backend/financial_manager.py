from fastapi import APIRouter, FastAPI, HTTPException, Depends, Request, Response, status
from fastapi.responses import JSONResponse
from sqlalchemy import Column, Integer, DateTime, DECIMAL, Text, Enum, ForeignKey
from sqlalchemy.orm import Session, declarative_base, relationship
from sqlalchemy.exc import SQLAlchemyError
from pydantic import  BaseModel
from decimal import Decimal
from datetime import datetime, timedelta
from database import SessionLocal, get_db
from models import User, Transaction, Category, TransactionCategory
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
        # Get existing tags
        existing_tags = {tc.category.name for tc in existing_transaction.categories}
        incoming_tags = set(transaction_data.tags or [])

        # Check if tags are identical
        if existing_tags == incoming_tags:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="An identical transaction with the same tags already exists"
            )
        
        # Add new tags to the existing transaction
        new_tags = incoming_tags - existing_tags
        for tag in new_tags:
            category = db.query(Category).filter(Category.name == tag).first()
            if not category:
                # Create the category if it doesn't exist
                category = Category(name=tag)
                db.add(category)
                db.flush()

            # Link the new tag to the existing transaction
            transaction_category = TransactionCategory(
                transaction_id=existing_transaction.id,
                category_id=category.id
            )
            db.add(transaction_category)

        db.commit()
        db.refresh(existing_transaction)
        return {"message": "Tags updated successfully", "transaction_id": existing_transaction.id}


    # Create a new transaction
    new_transaction = Transaction(
        user_id=user.id,
        amount=transaction_data.amount,
        description=transaction_data.description,
        date_time=transaction_data.date_time,
        type=transaction_data.type.value
    )

    # Handle categories (tags)
    if transaction_data.tags:
        for tag in transaction_data.tags:
            # Check if the category exists
            category = db.query(Category).filter(Category.name == tag).first()
            if not category:
                # Create the category if it doesn't exist
                category = Category(name=tag)
                db.add(category)
                db.flush()  # Flush to get the new category ID immediately

            # Link the category to the transaction
            transaction_category = TransactionCategory(
                transaction=new_transaction,
                category=category
            )
            db.add(transaction_category)
    
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

 # Debug logs
    print(f"Received request with start_date={start_date}, end_date={end_date}, transaction_type={transaction_type}")
    print(f"Authenticated user: {user.id}")
    try:
        transactions = db.query(Transaction).filter(
            Transaction.user_id == user.id,
            Transaction.date_time >= start_date,
            Transaction.date_time <= end_date,
            Transaction.type == transaction_type.value
        ).all()
        if not transactions:
            return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "No transactions found in this period"})
        
        # Convert to Pydantic model with `type` as a string
        result = [
            TransactionCreate(
                amount=transaction.amount,
                description=transaction.description,
                date_time=transaction.date_time,
                tags=None,  # Add tags if available
                type=transaction.type.value
            )
            for transaction in transactions
        ]

        return result

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

        result = []
        for income in incomes:
            tags = [tc.category.name for tc in income.categories]  # Fetch related tags
            result.append({
                "id": income.id,
                "amount": income.amount,
                "description": income.description,
                "date_time": income.date_time,
                "type": income.type,
                "tags": tags
            })

        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail="Error fetching incomes.")

@router.get("/allExpenses", status_code=200)
def get_all_incomes(
    db: Session = Depends(get_db),
    user: User = Depends(authenticate_user)
):
    """
    Get all expenses for the authenticated user, excluding tags.
    """
    try:
        # Query all incomes for the user
        expenses = db.query(Transaction).filter(
            Transaction.user_id == user.id,
            Transaction.type == "expense"  # Filter only expenses
        ).all()

        if not expenses:
            return {"message": "No expenses found."}

        # Transform data to exclude tags
        result = []
        for expense in expenses:
            tags = [tc.category.name for tc in expense.categories]  # Fetch related tags
            result.append({
                "id": expense.id,
                "amount": expense.amount,
                "description": expense.description,
                "date_time": expense.date_time,
                "type": expense.type,
                "tags": tags
            })

        return result


    except Exception as e:
        raise HTTPException(status_code=500, detail="Error fetching expenses.")


@router.get("/incomesTags", status_code=200)
def get_incomes_tags(
    db: Session = Depends(get_db),
    user: User = Depends(authenticate_user)
):
    """
    Get total income amounts grouped by tags for the authenticated user.
    """
    try:
        incomes = db.query(Transaction).filter(
            Transaction.user_id == user.id,
            Transaction.type == "income"
        ).all()

        if not incomes:
            return {"message": "No incomes found."}

        # Use a flat dictionary to store relationships
        tag_relationships = {}

        # Process transactions
        for transaction in incomes:
            # Get sorted tags for consistency
            tags = sorted([tc.category.name for tc in transaction.categories])
            amount = transaction.amount

            # Create a unique key for the combination of tags
            tags_key = ", ".join(tags)

            # Add or update the total for this combination
            if tags_key not in tag_relationships:
                tag_relationships[tags_key] = 0

            tag_relationships[tags_key] += amount

        return tag_relationships


    except Exception as e:
        raise HTTPException(status_code=500, detail="Error fetching income tags.")

@router.get("/expensesTags", status_code=200)
def get_expenses_tags(
    db: Session = Depends(get_db),
    user: User = Depends(authenticate_user)
):
    """
    Get total expense amounts grouped by tags for the authenticated user.
    """
    try:
        expenses = db.query(Transaction).filter(
            Transaction.user_id == user.id,
            Transaction.type == "expense"
        ).all()

        if not expenses:
            return {"message": "No expenses found."}

        tag_relationships = {}

        # Process transactions
        for transaction in expenses:
            # Get sorted tags for consistency
            tags = sorted([tc.category.name for tc in transaction.categories])
            amount = transaction.amount

            # Create a unique key for the combination of tags
            tags_key = ", ".join(tags)

            # Add or update the total for this combination
            if tags_key not in tag_relationships:
                tag_relationships[tags_key] = 0

            tag_relationships[tags_key] += amount

        return tag_relationships


    except Exception as e:
        raise HTTPException(status_code=500, detail="Error fetching expense tags.")
