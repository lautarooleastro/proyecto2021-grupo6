from app.resources import issue


def set_routes(app):
    app.add_url_rule("/consultas", "issue_index", issue.index)
    app.add_url_rule("/consultas", "issue_create",
                     issue.create, methods=["POST"])
    app.add_url_rule("/consultas/nueva", "issue_new", issue.new)
