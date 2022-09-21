from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id: Optional[int]
    name: str
    email: str
    phone: str
    password: str

    class Config:
        orm_mode = True