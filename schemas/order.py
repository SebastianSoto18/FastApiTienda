from pydantic import BaseModel
from typing import Optional

# `Order` is a class that inherits from `BaseModel` and has the following fields: `id`, `user_id`,
# `client_name`, `client_phone`, `client_address`, `quantity_per_products`, `products`, `status`,
# `date`, `total`
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