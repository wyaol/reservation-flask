from flask import  session
from .db.config import TEACHER_TABLE_NAME
from .db.api import sql_client


class TeacherService:

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(TeacherService, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.sql_client = sql_client
        self.db_name = TEACHER_TABLE_NAME

    def register(self, teacher_id, name, email, open_id):
        """
        注册用户
        :param teacher_id: 用户工号
        :return:
        """
        return self.sql_client.insert(self.db_name, teacher_id=teacher_id, open_id = open_id, name=name, email=email)

    def get_teacher_id(self, open_id):
        data = self.sql_client.select(self.db_name, ['teacher_id'], open_id=open_id)
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
        return self.sql_client.update(self.db_name, set=set, where=where)

    def get_info(self, id):
        res_data = self.sql_client.select(self.db_name, ['name', 'sex', 'phone_number'], teacher_id=id)
        # print(res_data)
        return {'name': res_data[0][0], 'sex': res_data[0][1], 'phone_number': res_data[0][2]}

    def get_email(self, teacher_id):
        res_data = self.sql_client.select(self.db_name, ['email', 'name'], teacher_id=teacher_id)
        if len(res_data) == 0: return None
        return {'email': res_data[0][0], 'name': res_data[0][1]}


teacher_service = TeacherService().instance