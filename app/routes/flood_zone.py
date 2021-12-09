from app.resources import flood_zone


def set_routes(app):
    app.add_url_rule("/zonas_inundables/<int:page>",
                     "flood_zone_index", flood_zone.index)
    app.add_url_rule("/zonas_inundables/ver/<int:id>",
                     "flood_zone_show", flood_zone.show, methods=['POST', 'GET'])
    app.add_url_rule("/zonas_inundables/eliminar", "flood_zone_destroy",
                     flood_zone.destroy, methods=["POST"])
    app.add_url_rule("/zonas_inundables/nuevo", "flood_zone_new",
                     flood_zone.new)
    app.add_url_rule("/zonas_inundables/add", "flood_zone_add",
                     flood_zone.create, methods=["POST"])
    app.add_url_rule("/zonas_inundables/editar/<int:id>",
                     "flood_zone_edit", flood_zone.edit, methods=['POST'])
    app.add_url_rule("/zonas_inundables/mod",
                     "flood_zone_modify", flood_zone.modify, methods=['POST'])
    app.add_url_rule("/zonas_inundables/importar", "flood_zone_import",
                     flood_zone.importZones)    
    app.add_url_rule("/zonas_inundables/importar", "flood_zone_imported_zones",
                     flood_zone.importedZones, methods=['POST'])   
    app.add_url_rule("/zonas_inundables/shearch", "flood_zone_filtrar",
                     flood_zone.filtrar, methods=['POST', 'GET'])