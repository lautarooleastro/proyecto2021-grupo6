from app.resources import evacuation_route


def set_routes(app):
    app.add_url_rule("/recorridos_de_evacuacion",
                     "evacuation_route_index", evacuation_route.index)
    app.add_url_rule("/recorrido_de_evacuacion/nueva",
                     "evacuation_route_new", evacuation_route.new)
    app.add_url_rule("/recorrido_de_evacuacion",
                     "evacuation_route_create", evacuation_route.create, methods=['POST'])
    app.add_url_rule("/recorrido_de_evacuacion/detalle/<int:id>",
                     "evacuation_route_detail", evacuation_route.detail, methods=['POST'])
    app.add_url_rule("/recorrido_de_evacuacion/eliminar",
                     "evacuation_route_destroy", evacuation_route.destroy, methods=['POST'])
    app.add_url_rule("/recorrido_de_evacuacion/editar/<int:id>",
                     "evacuation_route_edit", evacuation_route.edit)
    app.add_url_rule("/recorrido_de_evacuacion/editar/<int:id>",
                     "evacuation_route_update", evacuation_route.update)
