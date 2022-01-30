from app.resources import issue


def set_routes(app):
    app.add_url_rule("/denuncias", "issue_index", issue.index)
    app.add_url_rule("/denuncias", "issue_create",
                     issue.create, methods=["POST"])
    app.add_url_rule("/denuncias/nueva", "issue_new", issue.new)
    app.add_url_rule("/denuncias/detalle", "issue_show", issue.show)
