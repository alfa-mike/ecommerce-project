from flask import Blueprint, jsonify

product_bp = Blueprint('products', __name__)

@product_bp.route('/', methods=['GET'])
def get_products():
    return jsonify({"message": "Get all products"})

@product_bp.route('/', methods=['POST'])
def create_product():
    return jsonify({"message": "Create product"})
