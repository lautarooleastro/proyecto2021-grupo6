from app.resources import configuration


def set_routes(app):
    app.add_url_rule("/configuracion",
                     "configuration_index", configuration.index)
    app.add_url_rule("/configuracion/editar",
                     "configuration_edit", configuration.edit)
    app.add_url_rule("/configuracion/actualizar",
                     "configuration_update", configuration.update, methods=['POST'])
