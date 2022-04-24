from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from .config import settings


SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#  for documentation purposes & reference we keep this code using the regular postgres driver to connect to the database
#  we are curently using SQLalchemy to connect to the database so this is not needed
#while True:  # loop to try to connect to database with provided info
#    try:                            # (host, database, user, password, column name)
#        conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres',password='Medjed7!', cursor_factory=RealDictCursor)
#        cursor = conn.cursor()  # used to perform the SQL statements
#        print("Database connection was succesfull!")
#        break
#    except Exception as error:  # if failed will retry in 3 sec
#        print("Connecting to Database failed :(")
#        print("Error: ", error)
#        time.sleep(3)