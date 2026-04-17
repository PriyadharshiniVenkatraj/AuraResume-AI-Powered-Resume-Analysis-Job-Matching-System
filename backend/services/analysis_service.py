from flask import Blueprint, request, jsonify
from services.pipeline import run_pipeline

analysis_bp = Blueprint("analysis", __name__)

@analysis_bp.route("/analyze", methods=["POST"])
def analyze():
    file_path = request.form.get("file_path")
    job_text = request.form.get("job_description")

    result = run_pipeline(file_path, job_text)

    return jsonify(result)