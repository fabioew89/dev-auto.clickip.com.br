from flask import Flask

app = Flask(__name__)

@app.route('/')
def principal(debug=True):
    return "<h1>Hello Wolrd!</h1>"