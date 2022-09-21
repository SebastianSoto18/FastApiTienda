from fastapi import APIRouter, Response, status
from config.db import conn
from models.product import products
from schemas.product import Product


produc= APIRouter()

@produc.get("/products",response_model=list[Product],tags=["products"])
def get_produts():
    return conn.execute(products.select()).fetchall()

@produc.get("/products/{id}",response_model=Product,tags=["products"])
def get_product(id: int):
    return conn.execute(products.select().where(products.c.id == id)).first()

@produc.post("/products",response_model=Product,status_code=status.HTTP_201_CREATED,tags=["products"])
def create_product(product: Product):
    new_product = {"name": product.name, "code": product.code, "Quantity": product.Quantity, "price": product.price}
    conn.execute(products.insert().values(new_product))
    return Response(status_code=status.HTTP_201_CREATED)

@produc.delete("/products/{id}",status_code=status.HTTP_204_NO_CONTENT,tags=["products"])
def delete_product(id: int):
    conn.execute(products.delete().where(products.c.id == id))
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@produc.put("/products/{id}",status_code=status.HTTP_200_OK,tags=["products"])
def update_product(id: int, product: Product):
    conn.execute(products.update().where(products.c.id == id).values(name=product.name, code=product.code, quantity=product.quantity, price=product.price))
    return Response(status_code=status.HTTP_200_OK)