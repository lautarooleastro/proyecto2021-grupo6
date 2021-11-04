from app.resources import meeting_point


def set_routes(app):
    app.add_url_rule("/puntos_de_encuentro",
                     "meeting_point_index", meeting_point.index)
    app.add_url_rule("/puntos_de_encuentro/nuevo",
                     "meeting_point_new", meeting_point.new)
    app.add_url_rule("/puntos_de_encuentro",
                     "meeting_point_create", meeting_point.create, methods=["POST"])
