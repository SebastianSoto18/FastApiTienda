from pydantic import BaseModel



# `validateUser` is a class that inherits from `BaseModel` and has two attributes: `email` and
# `password`

class validateUser(BaseModel):
    email: str
    password: str

    class Config:
        orm_mode = True