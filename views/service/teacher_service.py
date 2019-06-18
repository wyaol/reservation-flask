from .db.teacher import TeacherDB
from .db.config import TEACHER_TABLE_NAME


class TeacherService:

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(TeacherService, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.db = TeacherDB()

    def register_teacher(self, teacher_id, password):
        """
        注册用户
        :param teacher_id: 用户工号
        :param password:  用户密码
        :return:
        """
        self.db.sql.insert(TEACHER_TABLE_NAME, teacher_id=teacher_id, password=password)


teacher_service = TeacherService().instance