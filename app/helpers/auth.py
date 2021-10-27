from flask_login import current_user


def authenticated(session):
    return session.get("user")


def current_user():
    return current_user
