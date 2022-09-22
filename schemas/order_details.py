from pydantic import BaseModel
from typing import Optional

# `OrderDetails` is a `BaseModel` with `id`, `order_id`, `product_id`, `quantity`, `price`,
# `name_product`, and `total` fields

class OrderDetails(BaseModel):
    id: Optional[int]
    order_id: int
    product_id: int
    quantity: int
    price: int
    name_product: str
    total: int

    class Config:
        orm_mode = True