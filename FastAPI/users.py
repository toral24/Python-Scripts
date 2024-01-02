from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Inicia el server: uvicorn users:app --reload

#Entidad user

class User(BaseModel):
    nombre: str
    apellido: str
    edad: int

users_list = [User(nombre="Sergio", apellido="Toral", edad="25"),
         User(nombre="Sandra", apellido="Toral", edad="28"),
         User(nombre="Carmen", apellido="Nicolas", edad="24")]

@app.get("/usersjson")
async def usersjson():
    return [{"nombre": "Sergio"},
            {"nombre": "Pedro"},
            {"nombre": "Pablo"}]
@app.get("/users")
async def users():
    return users_list