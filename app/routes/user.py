from app.resources import user


def set_routes(app):
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
