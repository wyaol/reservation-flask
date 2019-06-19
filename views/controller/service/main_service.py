import json
from .db.api import sql
from .db.config import TEACHER_TABLE_NAME
from functools import wraps
from flask import  session


def logout():
    session.clear()
    return 'Logged out successfully!'


def login_require(func):
    @wraps(func)
    def wrapper(*argvs, **kwargs):
        if 'id' not in session:
            return json.dumps({
                'success': False,
                'redict': True,
                'msg': '您没有访问权限， 请登录'
            })
        return func(*argvs, **kwargs)
    return  wrapper


def register(identity, id):
    if identity == 'teacher':
        sql.insert(TEACHER_TABLE_NAME, teacher_id=id)