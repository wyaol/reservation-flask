import json
from flask import Blueprint


views = Blueprint('views',__name__)


@views.route('/hello')
def show():
    return 'views.hello'


@views.route('/register_teacher')
def register_teacher():
    ret = {
        'success': True,

    }
    return json.dumps(ret, ensure_ascii=False)