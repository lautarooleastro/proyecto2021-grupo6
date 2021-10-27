from app.helpers import auth as helper_auth
from app.helpers.permission import check_permission


def set_routes(app):
    # Funciones que se exportan al contexto de Jinja2
    app.jinja_env.globals.update(is_authenticated=helper_auth.authenticated)
    app.jinja_env.globals.update(current_user=helper_auth.current_user)
    app.jinja_env.globals.update(check_permission=check_permission)
