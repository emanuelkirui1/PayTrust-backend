from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from flasgger import Swagger
from database import db
from routes.auth import auth_bp
from routes.employees import employees_bp
from routes.payroll import payroll_bp
import os

app = Flask(__name__)

# =====================
# CONFIG
# =====================
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY", "super-secret")
app.config["SWAGGER"] = {
    "title": "PayTrust Payroll API",
    "uiversion": 3,
    "securityDefinitions": {
        "Bearer": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header",
            "description": "JWT Authorization header. Example: Bearer <token>"
        }
    }
}

JWTManager(app)
Swagger(app)
db.init_app(app)

# =====================
# ROUTES
# =====================
app.register_blueprint(auth_bp, url_prefix="/api/auth")
app.register_blueprint(employees_bp, url_prefix="/api/employees")
from app.routes.admin_routes import admin_bp
app.register_blueprint(admin_bp, url_prefix="/api/admin")
app.register_blueprint(payroll_bp, url_prefix="/api/payroll")

@app.route("/")
def health():
    return jsonify({"status": "PayTrust API running"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
