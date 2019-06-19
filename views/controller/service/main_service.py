import json
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