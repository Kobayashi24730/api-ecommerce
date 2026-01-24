from flask import Blueprint, jsonify
from services.product_service import get_all_products

products_bp = Blueprint("products", __name__)

@products_bp.route("/products", methods=["GET"])
def products():
    return jsonify(get_all_products())
