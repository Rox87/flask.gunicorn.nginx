from flask import Flask,render_template
server = Flask(__name__)

@server.route('/')
def hello_world():
    return render_template('index.html')