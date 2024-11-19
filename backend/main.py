import time
from sqlalchemy.exc import OperationalError
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import Base, engine, init_db  # Ensure the database is initialized here
from UserManagement import router as auth_router  # Import your router

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],  # Frontend origin
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods, or specify ["POST"]
    allow_headers=["*"],
)

# Initialize database
init_db()

# Define a root endpoint
@app.get("/")
async def read_root():
    return {"message": "Welcome to the Financial Project API"}

# Include the UserManagement router with the "/api" prefix
app.include_router(auth_router, prefix="/api")
