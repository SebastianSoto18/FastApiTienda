from fastapi import APIRouter, Response, status, Header
from config.db import conn
from functions_jwt import validate_token, write_token
from models.user import users
from schemas.user import User
from schemas.aut_user import validateUser
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_200_OK
from middlewares.verify_token_routes import VerifyTokenRoutes

user = APIRouter(route_class=VerifyTokenRoutes)


@user.post("/login",tags=["auth"])
def login(user: validateUser):
    userfind=conn.execute(users.select().where(users.c.email == user.email)).first()
    
    if userfind==None:
        if ~(user.password == user.password):
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
    new_user = {"name": user.name, "email": user.email, "phone": user.phone, "password": user.password}
    conn.execute(users.insert().values(new_user))
    return Response(status_code=HTTP_201_CREATED)

@user.delete("/users/{id}",status_code=status.HTTP_204_NO_CONTENT,tags=["users"])
def delete_user(id: int):
    conn.execute(users.delete().where(users.c.id == id))
    return Response(status_code=HTTP_204_NO_CONTENT)

@user.put("/users/{id}",status_code=status.HTTP_200_OK,tags=["users"])
def update_user(id: int, user: User):
    conn.execute(users.update().where(users.c.id == id).values(name=user.name, email=user.email, phone=user.phone, password=user.password))
    return Response(status_code=HTTP_200_OK)