from flask import Blueprint, jsonify

order_bp = Blueprint('orders', __name__)

@order_bp.route('/', methods=['GET'])
def get_orders():
    return jsonify({"message": "Get all orders"})

@order_bp.route('/', methods=['POST'])
def create_order():
    return jsonify({"message": "Create order"})
