
from auth.auth_handler import signJWT
from fastapi import APIRouter, Response, status,  Depends
from schemas.aut_user import validateUser
from models.user import users
from config.db import get_db
from sqlalchemy.orm import Session
from routes.user import verify_password


loginRouter = APIRouter()

@loginRouter.post("/login",tags=["login"], status_code=status.HTTP_200_OK)
def login(user:validateUser,db:Session=Depends(get_db)):

    data = db.query(users).filter(users.email==user.email).first()
    if data is None:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    if not verify_password(user.password,data.password):
        return Response(status_code=status.HTTP_401_UNAUTHORIZED)

    return signJWT(data.email)

