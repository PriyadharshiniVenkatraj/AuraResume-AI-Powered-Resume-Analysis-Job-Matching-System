from flask import Blueprint, request, jsonify
from flask_bcrypt import Bcrypt
from flask_jwt_extended import create_access_token

auth_bp = Blueprint("auth", __name__)
bcrypt = Bcrypt()

# fake in-memory user store (upgrade later to DB)
users = {}

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.json
    email = data["email"]
    password = bcrypt.generate_password_hash(data["password"]).decode("utf-8")

    users[email] = password
    return jsonify({"message": "User created"})

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    email = data["email"]

    if email not in users:
        return jsonify({"error": "User not found"}), 401

    if not bcrypt.check_password_hash(users[email], data["password"]):
        return jsonify({"error": "Wrong password"}), 401

    token = create_access_token(identity=email)
    return jsonify({"token": token})