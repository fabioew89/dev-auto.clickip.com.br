from flask import Flask, render_template, url_for, redirect, request
from app.controllers import netmiko
from app.controllers.forms import CadastroForm
from app.models.model import User
from app import app, db


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        host = request.form.get('host')
        username = request.form.get('username')
        password = request.form.get('password')
        output = netmiko.sh_int_terse(host, username, password)
        return render_template('index.html', output=output)
    return render_template('index.html')

@app.route('/unit', methods=['GET', 'POST'])
def sh_config_int_unit():
    if request.method == 'POST':
        host = request.form.get('fhost')
        username = request.form.get('fusername')
        password = request.form.get('fpassword')
        unit = request.form.get('funit')

        output = netmiko.sh_config_int_unit(host, username, password, unit)
        return render_template('sh_config_int_unit.html', output=output)
    return render_template('sh_config_int_unit.html')

@app.route('/about')
def about():
    return 'about'


@app.route('/cadastro_usuarios', methods=['GET', 'POST'])
def page_cadastro():
    form = CadastroForm() # form instance

    if form.validate_on_submit():
