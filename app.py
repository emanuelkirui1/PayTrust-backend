from flask import Flask
from flask_jwt_extended import JWTManager
from flask_swagger_ui import get_swaggerui_blueprint
from config import Config
from database import Base, engine

from routes.auth import auth_bp
from routes.employees import employees_bp
from routes.payroll import payroll_bp

app = Flask(__name__)
app.config.from_object(Config)
JWTManager(app)

Base.metadata.create_all(bind=engine)

app.register_blueprint(auth_bp)
app.register_blueprint(employees_bp)
app.register_blueprint(payroll_bp)

SWAGGER_URL = "/api/docs"
API_URL = "/static/swagger.json"

swagger_bp = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={"app_name": "PayTrust API"}
)

app.register_blueprint(swagger_bp)

@app.route("/")
def home():
    return {"status": "PayTrust Backend Running"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
