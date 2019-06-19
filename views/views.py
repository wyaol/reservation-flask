import json
import pymysql
from flask_login import login_required
from flask import Blueprint, request, session
from .controller.service.teacher_service import teacher_service
from .controller.service.main_service import logout as service_logout
from .controller import control
from .controller.service.main_service import login_require
from .controller.controller_exception import LoginFailException


views = Blueprint('views',__name__)


@views.route('/hello')
@login_require
def show():
    return 'views.hello'


@views.route('/register_teacher', methods=['POST'])
def register_teacher():
    teacher_id = request.form.get('teacher_id')
    password = request.form.get('password')
    try:
        assert teacher_id is not None and password is not None, '传入参数不合法！'
        teacher_service.register(teacher_id, password)
        ret = {
            'success': True
        }
    except pymysql.err.IntegrityError as e:
        ret = {
            'success': False,
            'msg': str(e),
        }
    except AssertionError as e:
        ret = {
            'success': False,
            'msg': str(e),
        }
    return json.dumps(ret, ensure_ascii=False)


@views.route('/login', methods=['POST'])
def login():
    identity = request.form.get('identity')
    id = request.form.get('id')
    password = request.form.get('password')
    try:
        assert id is not None or password is not None or identity is None, '传入参数不合法！'
        control.login(identity, id, password)
        ret = {
            'success': True
        }
        return json.dumps(ret, ensure_ascii=False)
    except AssertionError as e:
        ret = {
            'success': False,
            'msg': e,
        }
        return json.dumps(ret, ensure_ascii=False)
    except LoginFailException as e:
        ret = {
            'success': False,
            'msg': str(e),
        }
        return json.dumps(ret, ensure_ascii=False)


@views.route('/logout')
@login_require
def logout():
    service_logout()
    ret = {
        'success': True
    }
    return json.dumps(ret, ensure_ascii=False)