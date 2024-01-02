from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Inicia el server: uvicorn users:app --reload

#Entidad user

class User(BaseModel):
    id: int
    nombre: str
    apellido: str
    edad: int

users_list = [User(id=1, nombre="Sergio", apellido="Toral", edad="25"),
            User(id=2, nombre="Sandra", apellido="Toral", edad="28"),
            User(id=3, nombre="Carmen", apellido="Nicolas", edad="24")]

@app.get("/usersjson")
async def usersjson():
    return [{"nombre": "Sergio"},
            {"nombre": "Pedro"},
            {"nombre": "Pablo"}]

@app.get("/users/")
async def users():
    return users_list

# Función para buscar usuarios en la lista
def search_user(id: int):
    Users = filter(lambda user: user.id == id, users_list)
    try:
        return list(Users)[0]
    except:
        return {"error": "No se ha encontrado el usuario"} 
#path
@app.get("/user/{id}")
async def user(id: int):
    return search_user(id)
#query
@app.get("/userquery/")
async def user(id: int):
    return search_user(id)