from fastapi import APIRouter, Response, status, Header, Depends
#from functions_jwt import validate_token, write_token
from models.user import users
from schemas.user import User
from schemas.aut_user import validateUser
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_200_OK
from passlib.context import CryptContext
from config.db import get_db
from sqlalchemy.orm import Session

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

user = APIRouter()

@user.get("/users",tags=["users"])
def get_users(db:Session=Depends(get_db)):
        return  db.query(users).all()
    
@user.get("/users/{id}",tags=["users"])
def get_user(id:int,db:Session=Depends(get_db)):
        data=db.query(users).filter(users.id==id).first()
        return (data,Response(status_code=status.HTTP_404_NOT_FOUND))[data is None]
    
@user.post("/users",tags=["users"], status_code=HTTP_201_CREATED)
def post_user(user:User,db:Session=Depends(get_db)):
        new_user = users(name=user.name,email=user.email,password=get_password_hash(user.password),phone=user.phone)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return Response(status_code=status.HTTP_201_CREATED)
    
@user.put("/users/{id}",tags=["users"])
def update_user(id:int,user:User,db:Session=Depends(get_db)):
        new_user = db.query(users).filter(users.id==id).first()
        new_user.name = user.name
        new_user.email = user.email
        new_user.password = get_password_hash(user.password)
        new_user.phone = user.phone
        db.commit()
        return Response(status_code=status.HTTP_200_OK)

@user.delete("/users/{id}",tags=["users"])
def delete_user(id:int,db:Session=Depends(get_db)):
        db.query(users).filter(users.id==id).delete()
        db.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)
        