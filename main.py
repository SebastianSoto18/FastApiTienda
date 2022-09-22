from fastapi import FastAPI
from routes.user import user
from routes.product import produc
from routes.order import ordersRouter
from routes.order_details import schemas
from dotenv import load_dotenv
from config.db import Base, engine



def create_Tables():
    Base.metadata.create_all(bind=engine)
create_Tables()

app = FastAPI(
    title="PedidosRest",
    description="API para la administracion de productos, pedidos y usuarios",
    openapi_tags=[
        {
        "name": "users",
        "description": "Operations with users"
        },
        {
        "name": "products",
        "description": "Operations with products",
        },
        {
        "name": "orders",
        "description": "orders operation"
        },
        {
        "name": "order_details",
        "description": "obtain order details by order id"
        }
        ]
)

app.include_router(user)
app.include_router(produc)
app.include_router(ordersRouter)
app.include_router(schemas)
load_dotenv()