from flask import Blueprint
from flask_swagger_ui import get_swaggerui_blueprint

docs_bp = get_swaggerui_blueprint(
    "/api/docs",
    "/static/swagger.json",
    config={"app_name": "PayTrust API"}
)
