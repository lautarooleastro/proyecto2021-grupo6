from flask_login import LoginManager
from app.models.user import User

login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
    return User.with_id(user_id)
