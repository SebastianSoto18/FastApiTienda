from fastapi import APIRouter

user = APIRouter()

@user.get("/")
def hello():
    return {"message": "Hello World"}