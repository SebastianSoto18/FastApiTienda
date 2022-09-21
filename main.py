from fastapi import FastAPI
from routes.user import user
from routes.product import produc
from dotenv import load_dotenv

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
        "name": "auth",
        "description": "auth operations"
        }
        ]
)

app.include_router(user)
app.include_router(produc)

load_dotenv()