from flask import Blueprint


views = Blueprint('views',__name__)


@views.route('/hello')
def show():
    return 'views.hello'