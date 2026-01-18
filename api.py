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
    "category": "camisas",
    "name": "Camisa Floral Masculina",
    "price": 50.72,
    "text": "Camisa masculina de manga curta com estampa floral, tecido leve e confortável.",
    "images": [
      "https://api-ecommerce-jywi.onrender.com/static/img/camisa-floral-1.jpg",
      "https://api-ecommerce-jywi.onrender.com/static/img/camisa-floral-2.jpg",
      "https://api-ecommerce-jywi.onrender.com/static/img/camisa-floral-3.jpg"
    ],
    "variants": [
      { "size": "P", "stock": 5 },
      { "size": "M", "stock": 3 },
      { "size": "G", "stock": 0 },
      { "size": "GG", "stock": 2 }
    ]
  },

  {
    "id": 2,
    "category": "camisas",
    "name": "Camisa Social Slim",
    "price": 89.90,
    "text": "Camisa social slim fit ideal para ocasiões formais ou trabalho.",
    "images": [
      "https://api-ecommerce-jywi.onrender.com/static/img/camisa-social-1.jpg",
      "https://api-ecommerce-jywi.onrender.com/static/img/camisa-social-2.jpg"
    ],
    "variants": [
      { "size": "P", "stock": 2 },
      { "size": "M", "stock": 6 },
      { "size": "G", "stock": 4 }
    ]
  },

  {
    "id": 3,
    "category": "sapatos",
    "name": "Tênis Casual Urbano",
    "price": 189.90,
    "text": "Tênis casual com design moderno e solado confortável.",
    "images": [
      "https://api-ecommerce-jywi.onrender.com/static/img/tenis-urbano-1.jpg",
      "https://api-ecommerce-jywi.onrender.com/static/img/tenis-urbano-2.jpg"
    ],
    "variants": [
      { "size": "38", "stock": 4 },
      { "size": "39", "stock": 2 },
      { "size": "40", "stock": 0 },
      { "size": "41", "stock": 6 },
      { "size": "42", "stock": 1 }
    ]
  },

  {
    "id": 4,
    "category": "sapatos",
    "name": "Sapato Social Masculino",
    "price": 249.90,
    "text": "Sapato social em couro sintético, ideal para eventos e trabalho.",
    "images": [
      "https://api-ecommerce-jywi.onrender.com/static/img/sapato-social-1.jpg",
      "https://api-ecommerce-jywi.onrender.com/static/img/sapato-social-2.jpg"
    ],
    "variants": [
      { "size": "39", "stock": 3 },
      { "size": "40", "stock": 1 },
      { "size": "41", "stock": 0 },
      { "size": "42", "stock": 2 }
    ]
  },

  {
    "id": 5,
    "category": "roupas",
    "name": "Calça Jeans Slim",
    "price": 129.90,
    "text": "Calça jeans slim fit com elastano e ótimo caimento.",
    "images": [
      "https://api-ecommerce-jywi.onrender.com/static/img/calca-jeans-1.jpg",
      "https://api-ecommerce-jywi.onrender.com/static/img/calca-jeans-2.jpg"
    ],
    "variants": [
      { "size": "38", "stock": 5 },
      { "size": "40", "stock": 3 },
      { "size": "42", "stock": 0 },
      { "size": "44", "stock": 2 }
    ]
  },

  {
    "id": 6,
    "category": "roupas",
    "name": "Jaqueta Corta Vento",
    "price": 159.90,
    "text": "Jaqueta corta vento impermeável, ideal para dias frios e chuvosos.",
    "images": [
      "https://api-ecommerce-jywi.onrender.com/static/img/jaqueta-1.jpg",
      "https://api-ecommerce-jywi.onrender.com/static/img/jaqueta-2.jpg"
    ],
    "variants": [
      { "size": "P", "stock": 1 },
      { "size": "M", "stock": 4 },
      { "size": "G", "stock": 2 }
    ]
  },

  {
    "id": 7,
    "category": "eletronicos",
    "name": "Fone de Ouvido Bluetooth",
    "price": 99.90,
    "text": "Fone bluetooth com cancelamento de ruído e bateria de longa duração.",
    "images": [
      "https://api-ecommerce-jywi.onrender.com/static/img/fone-1.jpg",
      "https://api-ecommerce-jywi.onrender.com/static/img/fone-2.jpg"
    ],
    "variants": [
      { "size": "Preto", "stock": 10 },
      { "size": "Branco", "stock": 0 },
      { "size": "Azul", "stock": 4 }
    ]
  },

  {
    "id": 8,
    "category": "eletronicos",
    "name": "Smartwatch Fitness",
    "price": 199.90,
    "text": "Smartwatch com monitor cardíaco, contador de passos e notificações.",
    "images": [
      "https://api-ecommerce-jywi.onrender.com/static/img/smartwatch-1.jpg",
      "https://api-ecommerce-jywi.onrender.com/static/img/smartwatch-2.jpg"
    ],
    "variants": [
      { "size": "Preto", "stock": 3 },
      { "size": "Cinza", "stock": 5 },
      { "size": "Rosa", "stock": 1 }
    ]
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
