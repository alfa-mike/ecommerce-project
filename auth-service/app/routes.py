from flask import Blueprint, jsonify, request
from bcrypt import hashpw, gensalt, checkpw
from .models import User
from . import db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    
    # Validate request data
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({"error": "Username and password are required"}), 400

    user = User.query.filter_by(username=data['username']).first()
    if user and checkpw(data['password'].encode('utf-8'), user.password_hash.encode('utf-8')):
        return jsonify({"message": "Login successful"})
    
    return jsonify({"error": "Invalid username or password"}), 401



@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    
    # Validate request data
    if not data or not data.get('username') or not data.get('password') or not data.get('email'):
        return jsonify({"error": "Username, password, and email are required"}), 400

    if User.query.filter_by(username=data['username']).first() or User.query.filter_by(email=data['email']).first():
        return jsonify({"error": "User with this username or email already exists"}), 409

    hashed_password = hashpw(data['password'].encode('utf-8'), gensalt()).decode('utf-8')
    new_user = User(username=data['username'], password_hash=hashed_password, email=data['email'], role='user')
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({"message": "User registered successfully"}), 201
