from app.resources import issue


def set_routes(app):
    app.add_url_rule("/denuncias", "issue_index", issue.index)
    app.add_url_rule("/denuncias", "issue_create",
                     issue.create, methods=["POST"])
    app.add_url_rule("/denuncias/nueva", "issue_new", issue.new)
    app.add_url_rule("/denuncias/detalle/<int:id>", "issue_show", issue.show, methods=['POST', 'GET'])
    
    app.add_url_rule("/denuncias/nueva", "issue_edit", issue.new)
    app.add_url_rule("/denuncias/nueva", "issue_destroy", issue.new)