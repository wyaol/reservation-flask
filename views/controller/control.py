from flask import session
from .service.teacher_service import teacher_service
from .service.finance_service import finance_service
from .service import main_service
from .controller_exception import IdentityNotExistException


def login(code):
    open_id = main_service.get_open_id(code)
    session['open_id'] = open_id
    teacher_id = teacher_service.get_teacher_id(open_id)
    if teacher_id is not None:
        set_session('teacher', teacher_id)
        return True
    finance_id = finance_service.get_finance_id(open_id)
    if finance_id is not None:
        set_session('finance', finance_id)
        return True
    return False


def set_session(identity, id):
    session['identity'] = identity
    session['id'] = id


def register(identity, id, open_id):
    session['open_id'] = open_id
    set_session(identity, id)
    if identity == 'teacher':
        return teacher_service.register(id, open_id)
    elif identity == 'finance':
        return finance_service.register(id, open_id)
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
        assert name is not None or sex is not None or phone_number is not None
        if name is not None:
            set['name'] = name
        if sex is not None:
            set['sex'] = sex
        if phone_number is not None:
            set['phone_number'] = phone_number
        return teacher_service.set_info(where=where, set=set)
    raise IdentityNotExistException('identity not found, your identity is %s'%identity)


def get_info(id, identity):
    if identity == 'teacher':
        return  teacher_service.get_info(id)
    # elif identity == 'finance':
    #     return
    raise IdentityNotExistException('identity not found, your identity is %s' % identity)

def get_task(finance_id: str):
    if finance_service.has_task(finance_id) is False:
        return finance_service.get_task(finance_id)
    return '任务正在进行中'