from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager

from database.db import init_db

# create app
app = Flask(__name__)
CORS(app)

# 🔐 JWT CONFIG
app.config["JWT_SECRET_KEY"] = "secret-key"
jwt = JWTManager(app)

# import blueprints AFTER app creation
from routes.analysis_routes import analysis_bp
from routes.resume_routes import resume_bp
from routes.history_routes import history_bp
from auth import auth_bp

# register blueprints
app.register_blueprint(analysis_bp, url_prefix="/analysis")
app.register_blueprint(resume_bp, url_prefix="/resume")
app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(history_bp, url_prefix="/api")


@app.route("/")
def home():
    return {"message": "Backend running"}

if __name__ == "__main__":
    init_db()   # ✅ FIXED HERE
    app.run(debug=True)