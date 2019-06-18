import json
import pymysql
from flask import Blueprint, request
from .controller.service.teacher_service import teacher_service


views = Blueprint('views',__name__)


@views.route('/hello')
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


@views.route('/login_teacher', methods=['POST'])
def login_teacher():
    teacher_id = request.form.get('teacher_id')
    password = request.form.get('password')
    assert teacher_id is not None and password is not None, '传入参数不合法！'
    teacher_service.login(teacher_id, password)
    ret = {
        'success': True
    }
    return json.dumps(ret, ensure_ascii=False)