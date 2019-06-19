from .service.teacher_service import teacher_service
from .controller_exception import LoginFailException


def login(identity: str, id, password):
    if identity == 'teacher':
        if teacher_service.check_login(id, password) is True:
            teacher_service.login(id)
        else:
            raise LoginFailException(id, password)
    else:
        print(identity)