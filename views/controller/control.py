from flask import session
from .service.teacher_service import teacher_service
from .service import main_service
from .controller_exception import IdentityNotExistException


def login(code):
    open_id = main_service.get_open_id(code)
    teacher_id = teacher_service.get_teacher_id(open_id)
    session['open_id'] = open_id
    if teacher_id is not None:
        teacher_service.login(teacher_id=teacher_id)
        return True
    return False


def register(identity, id):
    if identity == 'teacher':
        return teacher_service.register(id)
    raise IdentityNotExistException('identity not found, your identity is %s'%identity)

