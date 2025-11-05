from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String, Float, create_engine

Base = declarative_base()

class Employee(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    job_title = Column(String(150), nullable=False)
    salary = Column(Float, nullable=False)

    def __repr__(self):
        return f"[id = {self.id}, name = {self.name}, job_title = {self.job_title}, salary = {self.salary}]"
    
engine = create_engine('sqlite:///employees_db.sqlite', echo=True) # create database if not exists
Base.metadata.create_all(engine) # create tables for model classes

# setup things for transactions (crud ops)
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

# CRUD Operations
# dravid = Employee(name="Dravid", job_title="Od Coach", salary=1200)
# session.add(dravid)
# session.commit()

jaiswal = Employee(name="Jaiswal", job_title="Batsman", salary=20000)
session.add(jaiswal)

abhishek = Employee(name="Abhishek", job_title="Bowler", salary=1000000)
session.add(abhishek)
session.commit()

employees = session.query(Employee).all()
print(employees)

abhi = session.query(Employee).filter_by(name="Abhishek").first()
print(abhi)

abhi.salary = 5000000
session.commit()

employees = session.query(Employee).all()
print(employees)