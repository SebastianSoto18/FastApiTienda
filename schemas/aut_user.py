from pydantic import BaseModel

class validateUser(BaseModel):
    email: str
    password: str

    class Config:
        orm_mode = True