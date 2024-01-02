from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/url")
async def url():
    return {"url_curso": "https://mouredev.com/python"}

#Documentación Swagger: http://127.0.0.1:8000/docs
#Documentación Redocly: http://127.0.0.1:8000/redoc