from flask import render_template, request
from app import app


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        host = request.form['host']
        username = request.form['username']
        password = request.form['password']
        result = sh_int_terse('host','username','password')

        return render_template('index.html', result=result)

    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')
