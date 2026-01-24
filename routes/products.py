from fastapi import APIRouter
from app.services.product_service import load_products

router = APIRouter()

@router.get("/")
def get_products():
    return load_products()

@router.get("/category/{category}")
def get_by_category(category: str):
    products = load_products()
    return [p for p in products if p.get("category", "").lower() == category.lower()]
