from fastapi import APIRouter

router = APIRouter(prefix="/products", responses={404: {"mensaje": "No encontrado", }}, tags=["products"])

products_list = ["producto 1", "producto 2", "producto 3"]

@router.get("/")
async def products():
    return products_list

@router.get("/{id}")
async def products(id: int):
    return products_list[id]