from sqlalchemy import  Column
from sqlalchemy.sql.sqltypes import Integer, String, Text
from config.db import Base


class orders (Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer)
    client_name = Column(String(100))
    client_phone = Column(String(20))
    client_address = Column(String(255))
    products=Column(Text)
    quantity_per_products = Column(Text)
    total = Column(Integer)
    status = Column(String(20))
    date = Column(String(100))

    
    def __repr__(self):
        return f"Order {self.id}"