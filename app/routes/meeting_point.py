from app.resources import meeting_point


def set_routes(app):
    app.add_url_rule("/puntos_de_encuentro",
                     "meeting_point_index", meeting_point.index)
    app.add_url_rule("/puntos_de_encuentro/nuevo",
                     "meeting_point_new", meeting_point.new)
    app.add_url_rule("/puntos_de_encuentro",
                     "meeting_point_create", meeting_point.create, methods=["POST"])

    app.add_url_rule("/puntos_de_encuentro/detalle/<int:id>",
                     "meeting_point_detail", meeting_point.detail, methods=["GET"])
    app.add_url_rule("/puntos_de_encuentro/eliminar/<int:id>",
                     "meeting_point_destroy", meeting_point.delete, methods=["POST"])

    app.add_url_rule("/puntos_de_encuentro/editar/<int:id>",
                     "meeting_point_edit", meeting_point.edit, methods=["POST"])
    app.add_url_rule("/puntos_de_encuentro/actualizar/<int:id>", "meeting_point_update", meeting_point.update, methods=["POST"])
