import pytest
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi import HTTPException
from models import Base, User  
from UserManagement import UserBuilder  

# Use an in-memory SQLite database for testing
TEST_DATABASE_URL = "sqlite:///:memory:"

# Set up the test database engine and session factory
engine = create_engine(TEST_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create tables in the test database
Base.metadata.create_all(bind=engine)

@pytest.fixture(scope="function")
def db():
    """Create a new database session for a test, and close it after the test completes."""
    session = TestingSessionLocal()
    yield session
    session.close()

def test_add_user(db):
    # Arrange
    user_data = UserBuilder(email="test@example.com", username="testuser", password="testpass")

    # Act
    new_user = user_data.build(db)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    # Assert
    assert new_user.id is not None
    assert new_user.email == "test@example.com"
    assert new_user.username == "testuser"

def test_add_user_duplicate_email(db):
    # Arrange
    user_data1 = UserBuilder(email="duplicate@example.com", username="user1", password="pass1")
    user_data2 = UserBuilder(email="duplicate@example.com", username="user2", password="pass2")

    # Act
    new_user1 = user_data1.build(db)
    db.add(new_user1)
    db.commit()
    
    # Attempt to add a user with the same email
    with pytest.raises(HTTPException) as excinfo:
        user_data2.build(db)

    # Assert
    assert excinfo.value.status_code == 400
    assert "The e-mail is already registered" in str(excinfo.value)

def test_remove_user(db):
    # Arrange
    user_data = UserBuilder(email="removeme@example.com", username="removeuser", password="removepass")
    new_user = user_data.build(db)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    # Act - remove the user
    db.delete(new_user)
    db.commit()
    
    # Assert - confirm user is removed
    user_in_db = db.query(User).filter(User.email == "removeme@example.com").first()
    assert user_in_db is None
