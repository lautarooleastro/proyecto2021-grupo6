from app.resources import issue


def set_routes(app):
    app.add_url_rule("/denuncias", "issue_index", issue.index)
    app.add_url_rule("/denuncias", "issue_create",
                     issue.create, methods=["POST"])
    app.add_url_rule("/denuncias/nueva", "issue_new", issue.new)
    app.add_url_rule("/denuncias/detalle/<int:id>", "issue_show", issue.show, methods=['POST', 'GET'])    
    app.add_url_rule("/denuncias/edit/<int:id>", "issue_edit", issue.edit, methods=['POST', 'GET'])
    app.add_url_rule("/denuncias/modificar/<int:id>", "issue_modify",
                     issue.modify, methods=["POST"])
    app.add_url_rule("/denuncias/eliminar", "issue_destroy", issue.destroy, methods=["POST"])