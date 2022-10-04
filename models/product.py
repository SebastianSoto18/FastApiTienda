from enum import unique
from sqlalchemy import  Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import Base



class products(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20))
    code = Column(String(8), unique=True)
    Quantity = Column(Integer)
    price = Column(Integer)

    
    def __repr__(self):
        return f"Product {self.name}"