from flask import Blueprint, request, jsonify
import os

resume_bp = Blueprint("resume", __name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
@resume_bp.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]

    path = os.path.join("uploads", file.filename)
    file.save(path)

    return {"file_path": path}