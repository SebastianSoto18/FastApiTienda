from fastapi import APIRouter, Response, status, Depends
from models.order import orders
from models.product import products
from models.order_details import orders_detail
from schemas.order import Order
from config.db import get_db
from sqlalchemy.orm import Session


ordersRouter = APIRouter()

@ordersRouter.get("/orders",tags=["orders"])
def get_orders(db:Session=Depends(get_db)):
        return  db.query(orders).all()
    

@ordersRouter.get("/orders/client{id_client}",tags=["orders"])
def get_order_by_client(id_client:int,db:Session=Depends(get_db)):
        data=db.query(orders).filter(orders.user_id==id_client).all()
        return (data,Response(status_code=status.HTTP_404_NOT_FOUND))[data is None]

@ordersRouter.get("/orders/{id}",tags=["orders"])
def get_order(id:int,db:Session=Depends(get_db)):
    data = db.query(orders).filter(orders.id==id).first()
    return (data,Response(status_code=status.HTTP_404_NOT_FOUND))[data is None]

@ordersRouter.post("/orders",tags=["orders"], status_code=status.HTTP_201_CREATED)
def create_order(order:Order,db:Session=Depends(get_db)):
    new_order = orders(user_id=order.user_id,client_name=order.client_name,client_phone=order.client_phone,client_address=order.client_address,products=order.products,quantity_per_products=order.quantity_per_products,total=order.total,status=order.status)
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    newlist=new_order.products.split(",")
    for index, element in enumerate(newlist):
        product=db.query(products).filter(products.id==int(element)).first()
        db.query(products).filter(products.id==int(element)).update({products.Quantity:products.Quantity-int(new_order.quantity_per_products.split(",")[index])})
        new_order_details = orders_detail(order_id=new_order.id,product_id=product.id,quantity=int(new_order.quantity_per_products.split(",")[index]),price=product.price,name_product=product.name)
        db.add(new_order_details)
        db.commit()
        db.refresh(new_order_details)
        print(new_order_details)
        
    return Response(status_code=status.HTTP_201_CREATED)

##TODO
#@ordersRouter.put("/orders/{id}",tags=["orders"])

@ordersRouter.delete("/orders/{id}",tags=["orders"])
def delete_order(id:int,db:Session=Depends(get_db)):
    db.query(orders).filter(orders.id==id).delete()
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)