from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

# variable_name = "enigne_name://myuser:mypass@localhost:port_name/db_name

DATABASE_URL = f"{os.getenv('enigne_name')}://{os.getenv('myuser')}:{os.getenv('mypass')}@localhost:5432/{os.getenv('db_name')}"

print(DATABASE_URL)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
