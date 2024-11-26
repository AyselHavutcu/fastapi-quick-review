from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'


engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


""" 
while True:

    try:
        conn = psycopg2.connect(database="fastapi", user="postgres", password="aysel123", host="localhost", port="5432")
        cursor = conn.cursor()
        print("DB connection was succesfull!")
        break

    except Exception as error:
        print("Connecting the DB failed")
        print("Error: ", error)
        time.sleep(2) """