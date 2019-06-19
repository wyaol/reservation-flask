from flask_login import UserMixin
from flask_login import LoginManager


login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
    print(user_id)
    return Session(user_id)

class Session(UserMixin):

    def __init__(self, id):
        self.id = id