from fastapi import APIRouter, Response, status, Depends
from models.product import products
from schemas.product import Product
from config.db import get_db
from sqlalchemy.orm import Session
from auth.auth_barrer import JWTBearer


# Creating a new router.
produc = APIRouter()


"""
        It takes a database session, queries the products table, and returns all the rows in the table
        
        :param db: Session = Depends(get_db)
        :type db: Session
        :return: A list of products
"""
@produc.get("/products",dependencies=[Depends(JWTBearer())],tags=["products"])
def get_products(db:Session=Depends(get_db)):
        return  db.query(products).all()


        """
        It returns the product with the given id.
        
        :param id: int - The id of the product to retrieve
        :type id: int
        :param db: Session = Depends(get_db)
        :type db: Session
        :return: The data is being returned if it is not None.
        """
@produc.get("/products/{id}",dependencies=[Depends(JWTBearer())],tags=["products"])
def get_product(id:int,db:Session=Depends(get_db)):
        data=db.query(products).filter(products.id==id).first()
        return (data,Response(status_code=status.HTTP_404_NOT_FOUND))[data is None]


        """
        It takes a code as a parameter, and returns the product with that code
        
        :param code: str - The code of the product to retrieve
        :type code: str
        :param db: Session = Depends(get_db)
        :type db: Session
        :return: The first product with the code that is passed in the url
        """

@produc.get("/products/{code}",dependencies=[Depends(JWTBearer())],tags=["products"])
def get_product_byCode(code:str,db:Session=Depends(get_db)):
        data=db.query(products).filter(products.code==code).first()
        return db.query(products).filter(products.code==code).first()



        """
        It creates a new product in the database
        
        :param product: Product is the input parameter
        :type product: Product
        :param db: Session = Depends(get_db)
        :type db: Session
        :return: a response object with the status code 201.
        """
@produc.post("/products",tags=["products"],dependencies=[Depends(JWTBearer())], status_code=status.HTTP_201_CREATED)
def create_prodcut(product:Product,db:Session=Depends(get_db)):
        new_product = products(name=product.name,code=product.code,Quantity=product.Quantity,price=product.price)
        try:
                if(not(db.query(products).filter(products.email==new_product.code).first() is None)):
                        raise Exception
                db.add(new_product)
                db.commit()
                db.refresh(new_product)
                return Response(status_code=status.HTTP_201_CREATED)
        except Exception as e:
                return Response(status_code=status.HTTP_400_BAD_REQUEST, content="code or name already exists")

        """
        It takes the id of the product to be updated, the new product object and the database session as
        parameters
        
        :param id: The id of the product to be updated
        :type id: int
        :param product: Product - This is the model that we created earlier
        :type product: Product
        :param db: Session = Depends(get_db)
        :type db: Session
        :return: a response object with a status code of 200 OK.
        """
@produc.put("/products/{id}",dependencies=[Depends(JWTBearer())],status_code=status.HTTP_200_OK,tags=["products"])
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

        """
        It deletes a product from the database, if the product exists
        
        :param id: int - The id of the product to delete
        :type id: int
        :param db: Session = Depends(get_db)
        :type db: Session
        :return: a response object with a status code of 204.
        """
@produc.delete("/products/{id}",dependencies=[Depends(JWTBearer())],tags=["products"], status_code=status.HTTP_204_NO_CONTENT)
def delete_product(id:int,db:Session=Depends(get_db)):
        data=db.query(products).filter(products.id==id)
        
        if db.query(products).filter(products.id==id).first() is None:
                return Response(status_code=status.HTTP_404_NOT_FOUND)
        
        data.delete()
        db.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)
