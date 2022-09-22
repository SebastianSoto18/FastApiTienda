from fastapi import APIRouter, Response, status, Depends
from models.product import products
from schemas.product import Product
from config.db import get_db
from sqlalchemy.orm import Session


produc = APIRouter()


@produc.get("/products",tags=["products"])
def get_products(db:Session=Depends(get_db)):
        return  db.query(products).all()
    
@produc.get("/products/{id}",tags=["products"])
def get_product(id:int,db:Session=Depends(get_db)):
        data=db.query(products).filter(products.id==id).first()
        return (data,Response(status_code=status.HTTP_404_NOT_FOUND))[data is None]

@produc.post("/products",tags=["products"], status_code=status.HTTP_201_CREATED)
def create_prodcut(product:Product,db:Session=Depends(get_db)):
        new_product = products(name=product.name,code=product.code,Quantity=product.Quantity,price=product.price)
        try:
            db.add(new_product)
            db.commit()
            db.refresh(new_product)
            return Response(status_code=status.HTTP_201_CREATED)
        except:
            return Response(status_code=status.HTTP_400_BAD_REQUEST, content="code or name already exists")

@produc.put("/products/{id}",tags=["products"])
def update_product(id:int,product:Product,db:Session=Depends(get_db)):
    
        if db.query(products).filter(products.id==id).first() is None:
            Response(status_code=status.HTTP_404_NOT_FOUND)
            
        new_product = db.query(products).filter(products.id==id).first()
        new_product.name = product.name
        new_product.code = product.code
        new_product.Quantity = product.Quantity
        new_product.price = product.price
        
        db.commit()
        return Response(status_code=status.HTTP_200_OK)

@produc.delete("/products/{id}",tags=["products"])
def delete_product(id:int,db:Session=Depends(get_db)):
        data=db.query(products).filter(products.id==id)
        
        if db.query(products).filter(products.id==id).first() is None:
            return Response(status_code=status.HTTP_404_NOT_FOUND)
        
        data.delete()
        db.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    