from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

products = [
    {
        "id": 1,
        "name": "Notebook Gamer",
        "text": "Notebook gamer com placa de vídeo",
        "price": 3500,
        "img": "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=400"
    },
    {
        "id": 2,
        "name": "Celular",
        "text": "Celular com câmera 64MP",
        "price": 2500,
        "img": "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=400"
    }
]

#  Listar todos os produtos
@app.get("/products")
def get_products():
    return products

#  Buscar produto por ID
@app.get("/products/{product_id}")
def get_product(product_id: int):
    for product in products:
        if product["id"] == product_id:
            return product
    return {"error": "Produto não encontrado"}
