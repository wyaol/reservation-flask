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
        self.db_name = TEACHER_TABLE_NAME

    def register(self, teacher_id):
        """
        注册用户
        :param teacher_id: 用户工号
        :return:
        """
        open_id = session['open_id']
        return self.db.sql_client.insert(self.db_name, teacher_id=teacher_id, open_id = open_id)

    def get_teacher_id(self, open_id):
        data = self.db.sql_client.select(self.db_name, ['teacher_id'], open_id=open_id)
        if len(data) == 0:
            return None
        return data[0][0]

    def set_info(self, where: dict, set: dict):
        """
        更新用户信息
        :param where: 过滤条件
        :param set: 更新内容
        :return:
        """
        return self.db.sql_client.update(self.db_name, set=set, where=where)

    def get_info(self, id):
        return self.db.sql_client.select(self.db_name, ['*'], teacher_id=id)


teacher_service = TeacherService().instance