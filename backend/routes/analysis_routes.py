from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from services.pipeline_service import run_pipeline

# ✅ MUST DEFINE THIS FIRST
analysis_bp = Blueprint("analysis", __name__)

@analysis_bp.route("/analyze", methods=["POST"])
@jwt_required()
def analyze():

   data = request.json

   file_path = data["file_path"]
   job_text = data["job_description"]
   email = data.get("email")

   result = run_pipeline(file_path, job_text, email)

   return jsonify(result)