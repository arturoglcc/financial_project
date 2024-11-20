from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, DateTime, DECIMAL, Text, Enum
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime
import enum

# Enum for transaction type
class TransactionType(enum.Enum):
    income = "income"
    expense = "expense"

# Enum for reporting frequency
class ReportFrequency(enum.Enum):
    daily = "daily"
    weekly = "weekly"
    bi_weekly = "bi-weekly"
    monthly = "monthly"
    annually = "annually"
    
class User(Base):
    __tablename__ = "users"  # Specifies the table name in the database

    id = Column(Integer, primary_key=True, index=True)  
    email = Column(String(255), unique=True, index=True, nullable=False)  
    username = Column(String(255), unique=True, index=True, nullable=False)  
    password_hashed = Column(String(255), nullable=False)
    curp = Column(String(18), unique=True, nullable=True)
    rfc = Column(String(13), unique=True, nullable=True)
    name = Column(String(255), nullable=True)
    token_version = Column(Integer, default=0)

    # We add relationship with other tables
    transactions = relationship("Transaction", back_populates="user", cascade="all, delete-orphan")
    debts = relationship("Debt", back_populates="user", cascade="all, delete-orphan")
    reports = relationship("Report", back_populates="user", cascade="all, delete-orphan")


class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, nullable=False)

    transactions = relationship("TransactionCategory", back_populates="category")


class Transaction(Base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    amount = Column(DECIMAL(10, 2), nullable=False)
    description = Column(Text, nullable=True)
    date_time = Column(DateTime, nullable=False)
    type = Column(Enum(TransactionType), nullable=False)

    # Relationship with user and categories
    user = relationship("User", back_populates="transactions")
    categories = relationship("TransactionCategory", back_populates="transaction", cascade="all, delete-orphan")

class TransactionCategory(Base):
    __tablename__ = "transaction_categories"
    transaction_id = Column(Integer, ForeignKey("transactions.id", ondelete="CASCADE"), primary_key=True)
    category_id = Column(Integer, ForeignKey("categories.id", ondelete="CASCADE"), primary_key=True)

    # Transaction and category relationships
    transaction = relationship("Transaction", back_populates="categories")
    category = relationship("Category", back_populates="transactions")

class Debt(Base):
    __tablename__ = "debts"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    description = Column(Text, nullable=True)
    amount = Column(DECIMAL(10, 2), nullable=False)
    date = Column(DateTime, nullable=True, default=datetime.utcnow)
    due_date = Column(DateTime, nullable=True, default=datetime.utcnow)
    paid = Column(Boolean, default=False)

    # Relationship with user
    user = relationship("User", back_populates="debts")

# This table may be discarded
class Report(Base):
    __tablename__ = "reports"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    frequency = Column(Enum(ReportFrequency), default=ReportFrequency.monthly)
    last_sent = Column(DateTime, nullable=True)

    # Relationship with user
    user = relationship("User", back_populates="reports")

