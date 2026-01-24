from fastapi import APIRouter
from app.models.product import Product
from app.services.product_service import add_product, delete_product

router = APIRouter()

@router.post("/products")
def create_product(product: Product):
    return add_product(product)

@router.delete("/products/{pid}")
def remove_product(pid: int):
    delete_product(pid)
    return {"message": "Produto removido"}
