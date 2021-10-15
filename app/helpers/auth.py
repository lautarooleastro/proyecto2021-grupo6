from app.models.user import User


def authenticated(session):
    return session.get("user")


def current_user(session):
    return User.with_email(authenticated(session))
