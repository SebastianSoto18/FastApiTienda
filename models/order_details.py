from sqlalchemy import  Column
from sqlalchemy.sql.sqltypes import Integer,Text
from config.db import Base


class orders_detail(Base):
    __tablename__ = 'orders_detail'
    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer)
    quantity = Column(Text)
    product_id = Column(Integer)
    name_product = Column(Text)
    price = Column(Integer)
    total = Column(Integer)


    def __repr__(self):
        return f"Order {self.id}"