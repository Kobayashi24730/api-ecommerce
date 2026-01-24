from flask import Flask, jsonify, request
from flask_cors import CORS
from asgiref.wsgi import WsgiToAsgi
import json
import os

app = Flask(__name__)
CORS(app)

DATA_FILE = "products.json"

def load_products():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_products(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

@app.route("/")
def home():
    return jsonify({"status": "API online 🚀"})

@app.route("/products", methods=["GET"])
def get_products():
    return jsonify(load_products())

@app.route("/admin/products", methods=["POST"])
def add_product():
    data = request.json
    products = load_products()
    data["id"] = len(products) + 1
    products.append(data)
    save_products(products)
    return jsonify({"message": "Produto adicionado com sucesso", "product": data})

@app.route("/admin/products/<int:pid>", methods=["DELETE"])
def delete_product(pid):
    products = load_products()
    products = [p for p in products if p["id"] != pid]
    save_products(products)
    return jsonify({"message": "Produto removido com sucesso"})

asgi_app = WsgiToAsgi(app)
