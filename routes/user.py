from fastapi import APIRouter, Response, status, Header
from config.db import conn
from functions_jwt import validate_token, write_token
from models.user import users
from schemas.user import User
from schemas.aut_user import validateUser
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_200_OK
import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

user = APIRouter()
password = bytes("password", "utf-8")
salt = b"\x9b\x9c\x9d\x9e\x9f\xa0\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff"
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
)
key = base64.urlsafe_b64encode(kdf.derive(password))
serializer= Fernet(key)

@user.post("/login",tags=["auth"])
def login(user: validateUser):
    userfind=conn.execute(users.select().where(users.c.email == user.email)).first()
    
    if userfind==None:
        decodedpassword=serializer.decrypt(bytes(userfind[3], 'utf-8')).decode('utf-8')
        if ~(user.password == decodedpassword):
            return Response(status_code=status.HTTP_401_UNAUTHORIZED)
    
    return write_token({"email":userfind[2], "password":userfind[3]})

@user.post("/veryfy",tags=["auth"])
def verify(Autorization: str=Header(None) ):
    return validate_token(Autorization, output=True)

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