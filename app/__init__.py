from os import environ
from flask import Flask, render_template, Blueprint
from flask_session import Session
from app.models.user import User
from config import config
from app import db
from app.resources import issue
from app.resources import user
from app.resources import auth
from app.resources.api.issue import issue_api
from app.helpers import handler
from app.helpers import auth as helper_auth
from app.helpers.login import set_login


def create_app(environment="production"):

    # Configuración inicial de la app
    app = Flask(__name__)
    app.secret_key = b'a7114859260f52e390e77ac5e319d15acacf527cc7c63b60c72d7e2c966ede14'

    # Carga de la configuración
    env = environ.get("FLASK_ENV", environment)
    app.config.from_object(config[env])

    # Server Side session
    app.config["SESSION_TYPE"] = "filesystem"
    Session(app)

    # Configure db
    db.init_app(app)

    # Start Flask-Login manager
    set_login(app)

    # Funciones que se exportan al contexto de Jinja2
    app.jinja_env.globals.update(is_authenticated=helper_auth.authenticated)
    app.jinja_env.globals.update(current_user=helper_auth.current_user)
    app.jinja_env.globals.update(check_permission=User.check_permission)

    # Autenticación
    app.add_url_rule("/iniciar_sesion", "auth_login", auth.login)
    app.add_url_rule("/cerrar_sesion", "auth_logout", auth.logout)
    app.add_url_rule(
        "/autenticacion", "auth_authenticate", auth.authenticate, methods=["POST"]
    )

    # Rutas de Consultas
    app.add_url_rule("/consultas", "issue_index", issue.index)
    app.add_url_rule("/consultas", "issue_create",
                     issue.create, methods=["POST"])
    app.add_url_rule("/consultas/nueva", "issue_new", issue.new)

    # Rutas de Usuarios
    app.add_url_rule("/usuarios", "user_index", user.index)
    app.add_url_rule("/usuarios", "user_create", user.create, methods=["POST"])
    app.add_url_rule("/usuarios/nuevo", "user_new", user.new)
    app.add_url_rule("/usuarios/editar", "user_edit",
                     user.edit, methods=['POST'])
    app.add_url_rule("/usuarios/editar/confirmado", "user_update",
                     user.update, methods=['POST'])
    app.add_url_rule("/usuarios/eliminar", "user_destroy",
                     user.destroy, methods=["POST"])
    app.add_url_rule("/usuarios/cambiar_estado_<string:user_email>", "user_toggle",
                     user.toggle, methods=["GET"])

    # Ruta para el Home (usando decorator)

    @app.route("/")
    def home():
        return render_template("home.html")

    # Rutas de API-REST (usando Blueprints)
    api = Blueprint("api", __name__, url_prefix="/api")
    api.register_blueprint(issue_api)

    app.register_blueprint(api)

    # Handlers
    app.register_error_handler(404, handler.not_found_error)
    app.register_error_handler(401, handler.unauthorized_error)
    # Implementar lo mismo para el error 500

    # Retornar la instancia de app configurada
    return app
