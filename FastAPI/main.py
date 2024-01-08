from fastapi import FastAPI
from routers import products, users, basic_auth_users, jwt_auth_users, usersdb
from fastapi.staticfiles import StaticFiles

app = FastAPI()

#Routers
app.include_router(products.router)
app.include_router(users.router)
app.include_router(basic_auth_users.router)
app.include_router(jwt_auth_users.router)
app.include_router(usersdb.router)

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/url")
async def url():
    return {"url_curso": "https://mouredev.com/python"}

#Documentación Swagger: http://127.0.0.1:8000/docs
#Documentación Redocly: http://127.0.0.1:8000/redoc