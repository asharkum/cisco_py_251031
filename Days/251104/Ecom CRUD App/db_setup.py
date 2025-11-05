from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from product import Base

#setup database connection
engine = create_engine('sqlite:///ecom_db.sqlite', echo=True)
Base.metadata.create_all(engine) # create tables for model classes

# setup things for transactions (crud ops)
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()
