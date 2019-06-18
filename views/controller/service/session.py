from flask_login import UserMixin
from flask_login import LoginManager


login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
    session = Session.query_session(user_id)
    if session is not None:
        return session

class Session(UserMixin):

    sessions = []

    def __init__(self, id):
        self.id = id
        Session.sessions.append(self)

    @classmethod
    def query_session(cls, id):
        for e in cls.sessions:
            if e.id == id:
                return e