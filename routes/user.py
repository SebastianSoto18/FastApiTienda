from fastapi import APIRouter
from config.db import conn
from models.user import users
from schemas.user import User
from cryptography.fernet import Fernet

user = APIRouter()

key=Fernet.generate_key()
serializer=Fernet(key)

@user.get("/users")
def get_users():
    return conn.execute(users.select()).fetchall()

@user.post("/users")
def create_user(user: User):
    new_user = {"name": user.name, "email": user.email, "phone": user.phone, "password": ""}
    new_user["password"] = serializer.encrypt(user.password.encode("utf-8"))
    conn.execute(users.insert().values(new_user))
    return "creado"