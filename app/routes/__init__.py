from app.routes import auth, issue, user, helper, handler
from flask import render_template


def set_routes(app):
    auth.set_routes(app)
    issue.set_routes(app)
    user.set_routes(app)
    helper.set_routes(app)
    handler.set_routes(app)

    @app.route("/")
    def home():
        return render_template("home.html")
