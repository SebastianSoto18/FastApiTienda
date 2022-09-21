from fastapi import APIRouter, Response, status
from config.db import conn
from models.user import users
from schemas.user import User
from cryptography.fernet import Fernet
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_200_OK

user = APIRouter()

key=Fernet.generate_key()
serializer=Fernet(key)

@user.get("/users",response_model=list[User],tags=["users"])
def get_users():
    return conn.execute(users.select()).fetchall()

@user.get("/users/{id}",response_model=User,tags=["users"])
def get_user(id: int):
    return conn.execute(users.select().where(users.c.id == id)).first()

@user.post("/users",response_model=User,status_code=HTTP_201_CREATED,tags=["users"])
def create_user(user: User):
    new_user = {"name": user.name, "email": user.email, "phone": user.phone, "password": ""}
    new_user["password"] = serializer.encrypt(user.password.encode("utf-8"))
    conn.execute(users.insert().values(new_user))
    return Response(status_code=HTTP_201_CREATED)

@user.delete("/users/{id}",status_code=status.HTTP_204_NO_CONTENT,tags=["users"])
def delete_user(id: int):
    conn.execute(users.delete().where(users.c.id == id))
    return Response(status_code=HTTP_204_NO_CONTENT)

@user.put("/users/{id}",status_code=status.HTTP_200_OK,tags=["users"])
def update_user(id: int, user: User):
    conn.execute(users.update().where(users.c.id == id).values(name=user.name, email=user.email, phone=user.phone, password=serializer.encrypt(user.password.encode("utf-8"))))
    return Response(status_code=HTTP_200_OK)