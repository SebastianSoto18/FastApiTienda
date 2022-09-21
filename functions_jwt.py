from jwt import encode, decode
from datetime import datetime, timedelta
from os import getenv
from jwt import exceptions
from fastapi.responses import JSONResponse
from config.db import conn
from models.user import users

def expire_date(days: int):
    date = datetime.now()
    new_date = date + timedelta(days=days)
    return new_date

def write_token(data: dict):
    token=encode(payload={**data, "exp":expire_date(1)},key=getenv("SECRET"),algorithm="HS256")
    return  token

def validate_token(token, output=False):
    try:
        if output:
            data = decode(token, key=getenv("SECRET"), algorithms=["HS256"])
            user = conn.execute(users.select().where(users.c.email == data["email"])).first()
            if user == None:
                return False
            return {"response":True, "user":user}
        decode(token, key=getenv("SECRET"), algorithms=["HS256"])
    except exceptions.DecodeError:
        return JSONResponse(content={"message":"Invalid token"}, status_code=401)
    except exceptions.ExpiredSignatureError:
        return JSONResponse(content={"message":"Invalid expired"}, status_code=401)