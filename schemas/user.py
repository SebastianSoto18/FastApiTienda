from pydantic import BaseModel
from typing import Optional

# `User` is a class that inherits from `BaseModel` and has the following fields: `id`, `name`,
# `email`, `phone`, and `password`
class User(BaseModel):
    id: Optional[int]
    name: str
    email: str
    phone: str
    password: str
    address: str
    


    class Config:
        orm_mode = True