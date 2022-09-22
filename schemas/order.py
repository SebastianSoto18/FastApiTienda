from pydantic import BaseModel
from typing import Optional

class Order(BaseModel):
    id: Optional[int]
    user_id: int
    client_name: str
    client_phone: str
    client_address: str
    quantity_per_products: str
    products: str
    status: str
    date: str
    total: int

    class Config:
        orm_mode = True