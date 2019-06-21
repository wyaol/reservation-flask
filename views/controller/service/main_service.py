import json
import requests
from .db.api import sql_client
from .db import config
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
        sql_client.insert(config.TEACHER_TABLE_NAME, teacher_id=id)
    else:
        print('identity not define')


def get_open_id(code):
    url = config.GET_OPEN_ID_URL % (code, config.APPID, config.SECRET)
    page = requests.get(url)
    json_str = page.text
    return eval(json_str)['openid']


def get_reservation():
    pass