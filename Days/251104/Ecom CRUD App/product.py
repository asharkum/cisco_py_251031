from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Float, create_engine

Base = declarative_base()
# id, name, description, price, stock, tags
class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False) 
    description = Column(String(500), nullable=True)
    price = Column(Float, nullable=False)
    stock = Column(Integer, nullable=False)
    # tags = Column(String(200), nullable=True)

    def __repr__(self):
        return f"[id={self.id}, name='{self.name}', price={self.price}, stock={self.stock}]"
    