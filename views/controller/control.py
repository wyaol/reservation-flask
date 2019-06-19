from .service.teacher_service import teacher_service
from .controller_exception import LoginFailException


def login(identity: str, id, password):
    if identity == 'teacher':
        if teacher_service.check_login(id, password) is True:
            teacher_service.login(id)
        else:
            raise LoginFailException('登录错误 当前用户名%s 当前密码%s'%(id, password))
    else:
        print(identity)