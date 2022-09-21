from pydantic import BaseModel
from typing import Optional

class Product(BaseModel):
    id: Optional[int]
    name: str
    code: int
    Quantity: int
    price: float

    class Config:
        orm_mode = True