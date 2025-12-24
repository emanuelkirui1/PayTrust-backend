from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, get_jwt_identity
from config import Config
from database import Base, engine
from routes.auth import auth_bp
from routes.employees import employees_bp
from routes.payroll import payroll_bp
from routes.companies import companies_bp
from routes.docs import docs_bp
from services.audit import log_action

app = Flask(__name__)
app.config.from_object(Config)

jwt = JWTManager(app)
Base.metadata.create_all(bind=engine)

@app.after_request
def audit(response):
    try:
        user = get_jwt_identity()
        if user:
            log_action(user["id"], request.method, request.path)
    except:
        pass
    return response

app.register_blueprint(auth_bp, url_prefix="/api/auth")
app.register_blueprint(employees_bp, url_prefix="/api/employees")
app.register_blueprint(payroll_bp, url_prefix="/api/payroll")
app.register_blueprint(companies_bp, url_prefix="/api/companies")
app.register_blueprint(docs_bp)

@app.route("/")
def index():
    return jsonify({"message": "PayTrust API running"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

from routes.docs import docs_bp
app.register_blueprint(docs_bp)

from flask import request
from flask_jwt_extended import get_jwt_identity
from services.audit import log_action

@app.after_request
def audit_middleware(response):
    try:
        user = get_jwt_identity()
        if user:
            log_action(user["id"], request.method, request.path)
    except:
        pass
    return response
