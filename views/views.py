import json
import pymysql
from flask import Blueprint, request
from .service.teacher_service import teacher_service


views = Blueprint('views',__name__)


@views.route('/hello')
def show():
    return 'views.hello'


@views.route('/register_teacher', methods=['POST'])
def register_teacher():
    teacher_id = request.form.get('teacher_id')
    password = request.form.get('password')
    try:
        teacher_service.register_teacher(teacher_id, password)
        ret = {
            'success': True
        }
    except pymysql.err.IntegrityError as e:
        ret = {
            'success': False,
            'msg': str(e),
        }
    return json.dumps(ret, ensure_ascii=False)