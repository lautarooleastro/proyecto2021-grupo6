from app.helpers import handler


def set_routes(app):
    # Handlers
    app.register_error_handler(404, handler.not_found_error)
    app.register_error_handler(401, handler.unauthorized_error)
    app.register_error_handler(500, handler.internal_error)
