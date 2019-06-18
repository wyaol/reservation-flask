from flask import Flask
from views.views import views
import config


app = Flask(__name__)
app.register_blueprint(views, url_prefix='/api')


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(config.HOST, debug=config.DEBUG, port=config.PORT, ssl_context=config.SSL_CONTEXT)