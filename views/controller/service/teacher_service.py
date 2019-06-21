from flask import  session
from .db.teacher import TeacherDB
from .db.config import TEACHER_TABLE_NAME


class TeacherService:

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(TeacherService, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.db = TeacherDB()

    def register(self, teacher_id):
        """
        注册用户
        :param teacher_id: 用户工号
        :return:
        """
        open_id = session['open_id']
        return self.db.sql_client.insert(TEACHER_TABLE_NAME, teacher_id=teacher_id, open_id = open_id)

    def login(self, teacher_id):
        session['id'] = teacher_id

    def get_teacher_id(self, open_id):
        data = self.db.sql_client.select(TEACHER_TABLE_NAME, ['teacher_id'], open_id=open_id)
        if len(data) == 0:
            return None
        return data[0][0]

teacher_service = TeacherService().instance