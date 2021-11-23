from app.routes import auth, issue, user, helper, handler, meeting_point, flood_zone, evacuation_route, configuration
from flask import render_template


def set_routes(app):
    auth.set_routes(app)
    issue.set_routes(app)
    user.set_routes(app)
    helper.set_routes(app)
    handler.set_routes(app)
    meeting_point.set_routes(app)
    flood_zone.set_routes(app)
    evacuation_route.set_routes(app)
    configuration.set_routes(app)

    @app.route("/")
    def home():
        return render_template("home.html")
