import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base
from urllib.parse import quote_plus
from sqlalchemy.exc import OperationalError


load_dotenv()

# Retrieve environment variables
DB_HOST = os.getenv("MYSQL_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "3306")
DB_NAME = os.getenv("MYSQL_DATABASE", "financial_project_db")
DB_USER = os.getenv("MYSQL_USER", "user")
DB_PASSWORD = quote_plus(os.getenv("MYSQL_PASSWORD", "data_base_password"))

# Construct the database URL
DATABASE_URL = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

print("Constructed DATABASE_URL:", DATABASE_URL)

def create_database_if_not_exists():
    # Extract the database name from the URL
    base_url = DATABASE_URL.rsplit('/', 1)[0]  # Get everything before the database name
    database_name = DATABASE_URL.rsplit('/', 1)[-1]  # Get the database name

    # Connect to the MySQL server without specifying a database
    engine = create_engine(base_url)
    try:
        # Connect and check if the database exists
        with engine.connect() as connection:
            result = connection.execute(
                text(f"SHOW DATABASES LIKE '{database_name}'")
            ).fetchone()
            if not result:
                print(f"Database '{database_name}' does not exist. Creating...")
                connection.execute(text(f"CREATE DATABASE {database_name}"))
                print(f"Database '{database_name}' created successfully.")
    except OperationalError as e:
        print(f"Error connecting to the database server: {e}")
    finally:
        engine.dispose()

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def init_db():
    create_database_if_not_exists()
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


# Dependency to get a data base session per request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
