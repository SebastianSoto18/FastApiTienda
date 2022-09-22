from fastapi import APIRouter, Response, status, Depends
from config.db import get_db
from sqlalchemy.orm import Session
from models.order_details import orders_detail



schemas=APIRouter()

@schemas.get("/order_details/{id_venta}",tags=["order_details"])
def get_order_details(id_venta:int,db:Session=Depends(get_db)):
    data = db.query(orders_detail).filter(orders_detail.order_id==id_venta).all()
    return (data,Response(status_code=status.HTTP_404_NOT_FOUND))[data is None]