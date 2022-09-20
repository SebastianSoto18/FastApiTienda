from fastapi import FastAPI

app = FastAPI()

@app.get("/inicio")
async def inicio():
    return {"message": "Hola Mundo"}
