from fastapi import FastAPI
from routes.user import user
from routes.product import produc
from routes.order import ordersRouter
from routes.login import loginRouter
from routes.order_details import schemas
from dotenv import load_dotenv
from config.db import Base, engine
from fastapi.middleware.cors import CORSMiddleware


"""
    The function create_Tables() creates all the tables in the database using the metadata of the Base
    class which was created by extending declarative_base().
    """
def create_Tables():
    Base.metadata.create_all(bind=engine)
create_Tables()

# Creating the FastAPI object, which is the main object of the application.
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
        },
        {
        "name": "login",
        "description": "login authentication"
        }
        ]
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Including the routes from the different files.

app.include_router(user)
app.include_router(produc)
app.include_router(ordersRouter)
app.include_router(schemas)
app.include_router(loginRouter)

# Loading the environment variables from the .env file.
load_dotenv()