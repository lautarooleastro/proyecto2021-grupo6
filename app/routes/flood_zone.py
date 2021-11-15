from app.resources import flood_zone


def set_routes(app):
    app.add_url_rule("/zonas_inundables",
                     "flood_zone_index", flood_zone.index)
    app.add_url_rule("/zonas_inundables/ver/<int:id>",
                     "flood_zone_show", flood_zone.show, methods=['POST', 'GET'])
    app.add_url_rule("/zonas_inundables/eliminar", "flood_zone_destroy",
                     flood_zone.destroy, methods=["POST"])