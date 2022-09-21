from fastapi import FastAPI
from routes.user import user

app = FastAPI(
    title="PedidosRest",
    description="API para la administracion de productos, pedidos y usuarios",
    openapi_tags=[
        {
        "name": "users",
        "description": "Operations with users"
    }]
)
app.include_router(user)

