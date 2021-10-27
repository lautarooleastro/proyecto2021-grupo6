from app.routes import auth, issue, user


def set_routes(app):
    auth.set_routes(app)
    issue.set_routes(app)
    user.set_routes(app)
