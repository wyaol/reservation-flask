from flask import Flask
from views.views import views


app = Flask(__name__)
app.register_blueprint(views, url_prefix='/api')


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True, port=443, ssl_context=('server.crt', 'server.key'))