from flask import Blueprint
from app.resources.api.issue import issue_api


def set_routes(app):
    # Rutas de API-REST (usando Blueprints)
    api = Blueprint("api", __name__, url_prefix="/api")
    api.register_blueprint(issue_api)

    app.register_blueprint(api)
