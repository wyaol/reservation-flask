from flask import session
from .service.teacher_service import teacher_service
from .service import main_service
from .controller_exception import IdentityNotExistException


def login(code):
    open_id = main_service.get_open_id(code)
    teacher_id = teacher_service.get_teacher_id(open_id)
    session['open_id'] = open_id
    if teacher_id is not None:
        session['identity'] = 'teacher'
        session['id'] = teacher_id
        return True
    return False


def register(identity, id):
    if identity == 'teacher':
        return teacher_service.register(id)
    raise IdentityNotExistException('identity not found, your identity is %s'%identity)


def reservate(date:str, time: str, id):
    if main_service.is_reservated(date, time) is not True:
        return main_service.reservate(date, time, id)
    return None


def set_info(id, name, sex, phone_number):
    identity = session['identity']
    if identity == 'teacher':
        where = {
            'teacher_id': id
        }
        set = {}
        if name != None:
            set['name'] = name
        if sex != None:
            set['sex'] = sex
        if phone_number != None:
            set['phone_number'] = phone_number
        return teacher_service.set_info(where=where, set=set)
    raise IdentityNotExistException('identity not found, your identity is %s'%identity)


def get_info(id, identity):
    if identity == 'teacher':
        return  teacher_service.get_teacher_id(id)
    raise IdentityNotExistException('identity not found, your identity is %s' % identity)