from flask import Flask


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run('0.0.0.0', debug=True, port=443, ssl_context=('server.crt', 'server.key'))