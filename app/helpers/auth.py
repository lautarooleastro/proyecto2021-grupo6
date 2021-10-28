from flask_login import current_user


def authenticated():
    return current_user.is_authenticated


def logged_user():
    return current_user
