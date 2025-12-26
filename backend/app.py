from flask import Flask
from flask_jwt_extended import JWTManager
from database import init_db
from swagger import init_swagger

# Blueprints
from routes.auth import auth_bp
from routes.employees import employees_bp
from routes.payroll import payroll_bp
from routes.twofa import twofa_bp  # 2FA

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = "SUPER_SECRET_JWT_KEY"

jwt = JWTManager(app)
init_db()
init_swagger(app)

# ROUTES REGISTRATION (no duplicates!)
app.register_blueprint(auth_bp, url_prefix="/api/auth")
app.register_blueprint(employees_bp, url_prefix="/api/employees")
app.register_blueprint(payroll_bp, url_prefix="/api/payroll")
app.register_blueprint(twofa_bp, url_prefix="/api/auth/2fa")

@app.route("/")
def home():
    return {"message": "PayTrust API Running", "status": "OK"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
