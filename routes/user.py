from fastapi import APIRouter

user = APIRouter()

@user.get("/")
def hello():
    return {"message": "holi amorcito uwu",
            "afecto": "te amo"}