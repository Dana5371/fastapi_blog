from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("postgresql://danaker:1@localhost/fastapi_blog", echo=True)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db 
    finally:
        db.close()
