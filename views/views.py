import json
import pymysql
from flask_login import login_required
from flask import Blueprint, request, session
from .controller.service.teacher_service import teacher_service
from .controller.service import main_service
from .controller import control
from .controller.controller_exception import LoginFailException


views = Blueprint('views',__name__)


@views.route('/hello')
@main_service.login_require
def show():
    return 'views.hello'


@views.route('/register', methods=['POST'])
def register():
    identity = request.form.get('identity')
    id = request.form.get('id')
    print(request.form)
    assert id is not None and identity is not None, '传入参数不合法！'
    main_service.register(identity, id)
    ret = {
        'success': True
    }
    return json.dumps(ret, ensure_ascii=False)


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
        assert id is not None or password is not None and identity is not None, '传入参数不合法！'
        control.login(identity, id, password)
        ret = {
            'success': True
        }
    except AssertionError as e:
        ret = {
            'success': False,
            'msg': e,
        }
    except LoginFailException as e:
        ret = {
            'success': False,
            'msg': str(e),
        }
    return json.dumps(ret, ensure_ascii=False)


@views.route('/logout')
@main_service.login_require
def logout():
    main_service.logout()
    ret = {
        'success': True
    }
    return json.dumps(ret, ensure_ascii=False)


@views.route('/login_test')
def login_test():
    try:
        from .controller.service.teacher_service import teacher_service
        teacher_service.login('123456')
        ret = {
            'success': True
        }
    except AssertionError as e:
        ret = {
            'success': False,
            'msg': e,
        }
    except LoginFailException as e:
        ret = {
            'success': False,
            'msg': str(e),
        }
    return json.dumps(ret, ensure_ascii=False)