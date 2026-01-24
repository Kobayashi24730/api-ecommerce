from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import products, admin

app = FastAPI(title="E-commerce API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"] ,
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"status": "API online 🚀"}

app.include_router(products.router, prefix="/products", tags=["Products"])
app.include_router(admin.router, prefix="/admin", tags=["Admin"])
