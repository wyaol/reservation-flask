from flask import Flask
from views.views import views
from views.controller.service.session import login_manager
import config


app = Flask(__name__)
app.register_blueprint(views, url_prefix='/api')
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
login_manager.login_message = 'Access denied.'
login_manager.init_app(app)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(config.HOST, debug=config.DEBUG, port=config.PORT, ssl_context=config.SSL_CONTEXT)