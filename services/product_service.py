import json
import os
from app.models.product import Product

DATA_FILE = "app/storage/products.json"


def load_products():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_products(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def add_product(product: Product):
    products = load_products()
    product.id = len(products) + 1
    products.append(product.dict())
    save_products(products)
    return product


def delete_product(pid: int):
    products = load_products()
    products = [p for p in products if p["id"] != pid]
    save_products(products)
