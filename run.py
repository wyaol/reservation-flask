from flask import Flask
from views.identity_control_views import identity_control_views
from views.reservate_views import reservate_views
from datetime import timedelta
import config


app = Flask(__name__)
app.register_blueprint(identity_control_views, url_prefix='/api/identity')
app.register_blueprint(identity_control_views, url_prefix='/api/reservate')
app.secret_key = '123456'
app.permanent_session_lifetime = timedelta(days=1) #设置session的保存时间。


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(config.HOST, debug=config.DEBUG, port=config.PORT, ssl_context=config.SSL_CONTEXT)