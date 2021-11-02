from app.resources import meeting_point


def set_routes(app):
    app.add_url_rule("/puntos_de_encuentro",
                     "meeting_point_index", meeting_point.index)
