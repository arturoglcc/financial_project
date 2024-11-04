import time
from sqlalchemy.exc import OperationalError
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import Base, engine  # Ensure the database is initialized here
from UserManagement import router as auth_router  # Import your router

def init_db():
    retries = 5
    while retries > 0:
        try:
            # Attempt to create tables
            Base.metadata.create_all(bind=engine)
            print("Database initialized successfully.")
            break
        except OperationalError:
            print("Database not ready, retrying in 5 seconds...")
            retries -= 1
            time.sleep(5)
    else:
        print("Failed to connect to the database after several attempts.")
        raise Exception("Database initialization failed")

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

# Include the UserManagement router with the "/api" prefix
app.include_router(auth_router, prefix="/api")

@app.get("/")
def read_root():
    return {"Hello": "World"}
