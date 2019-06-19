from flask import session as flask_session


class Session:
    """
    对系统的session进行一次装饰
    """

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Session, cls).__new__(cls)
        return cls.instance

    def __init__(self, session):
        self.session = session

    def add(self, id):
        self.session['id'] = id

    def delete(self, id):
        self.session.pop(id)

    def clear(self, id):
        self.session.clear()

    def get(self, id):
        return self.session.get('id')


session = Session(flask_session).instance