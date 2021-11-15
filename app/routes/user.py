from app.resources import user


def set_routes(app):
    app.add_url_rule("/usuarios", "user_index", user.index)
    app.add_url_rule("/usuarios", "user_create", user.create, methods=["POST"])
    app.add_url_rule("/usuarios/nuevo", "user_new", user.new)
    app.add_url_rule("/usuarios/editar/<int:id>", "user_edit",
                     user.edit, methods=['POST', 'GET'])
    app.add_url_rule("/usuarios/actualizar/<int:id>", "user_update",
                     user.update, methods=['POST'])
    app.add_url_rule("/usuarios/eliminar", "user_destroy",
                     user.destroy, methods=["POST"])
    app.add_url_rule("/usuarios/cambiar_estado_<string:user_email>", "user_toggle",
                     user.toggle, methods=["GET"])
    app.add_url_rule("/usuarios/mi-perfil", "user_profile", user.profile)
    app.add_url_rule("/usuarios/mi-perfil/editar",
                     "user_profile_edit", user.profile_edit)
    app.add_url_rule("/usuarios/mi-perfil/editar/confirmado",
                     "user_profile_update", user.profile_update, methods=['POST'])
