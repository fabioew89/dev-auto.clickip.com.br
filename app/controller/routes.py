from flask import render_template, request
from app.controller.netmiko import sh_int_terse
from app import app


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        host = request.form.get('host')
        username = request.form.get('username')
        password = request.form.get('password')

        output = sh_int_terse(host, username, password)

        return render_template('index.html', output=output)
    
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')
