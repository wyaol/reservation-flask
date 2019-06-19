from .api import sql_client

class TeacherDB:

    def __init__(self):
        self.sql_client = sql_client