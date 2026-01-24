from flask import Blueprint, request, jsonify
from services.product_service import add_product, delete_product

admin_bp = Blueprint("admin", __name__)

@admin_bp.route("/admin/products", methods=["POST"])
def create_product():
    data = request.json
    product = add_product(data)
    return jsonify(product), 201

@admin_bp.route("/admin/products/<int:pid>", methods=["DELETE"])
def remove_product(pid):
    delete_product(pid)
    return jsonify({"success": True})
