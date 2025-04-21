from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError
from domain import models
import os
from dotenv import load_dotenv, find_dotenv
print("initializing db")
load_dotenv()
DATABASE_URL = os.environ.get("DATABASE_URL", "")

if not DATABASE_URL or DATABASE_URL.strip() == "":
        raise RuntimeError("DATABASE_URL environment variable is not set.")

def create_database_if_not_exists():
    temp_engine_url = os.getenv("DATABASE_ENGINE", "")
    if not temp_engine_url or temp_engine_url.strip() == "":
        raise RuntimeError("DATABASE_ENGINE environment variable is not set.")
    temp_engine = create_engine(temp_engine_url)
    with temp_engine.connect() as conn:
        try:
            conn.execute(text("CREATE DATABASE IF NOT EXISTS eway;"))
        except OperationalError as e:
            print(f"Error creating database: {e}")

create_database_if_not_exists()

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    models.Base.metadata.create_all(bind=engine)
