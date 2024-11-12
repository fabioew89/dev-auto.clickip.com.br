from flask import request, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from app import app, db
from app.models.model import *
from app.controllers.forms import *
from app.controllers import netmiko
from werkzeug.security import generate_password_hash, check_password_hash

@app.route('/')
def page_home():
    return render_template('home.html')

##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 
##### ##### ##### ##### ## LOGIN ## ##### ##### ##### ##### 
##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 

@app.route('/login', methods=['GET', 'POST'])
def page_login():
    form = Form_Login()
    
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        
        user = db.session.execute(db.select(Table_Register).filter_by(username=username)).scalar_one_or_none()

        if user and check_password_hash(user.password, password):
            login_user(user)
            flash(f'Sucesso ao logar {username}', category='success')
            return redirect(url_for('page_home'))
        else:
            flash('Email ou senha incorretos', category='danger')
    
    if form.errors:
        for field_name, err_messages in form.errors.items():
            for err in err_messages:
                flash(f'Erro no campo {field_name}: {err}', category='danger')

    return render_template('login.html', form=form)

##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 
##### ##### ##### ##### ## LOGOUT # ##### ##### ##### ##### 
##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 

@app.route('/logout')
def page_logout():
    logout_user()
    flash(f'Deslogado!!!', category='info')
    return redirect(url_for('page_home'))

##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 
##### ##### ##### ##### # NETMIKO # ##### ##### ##### ##### 
##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 

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

# @app.route('/', methods=['GET', 'POST'])
# def page_home():
#     if request.method == 'POST':
#         host = request.form.get('host')
#         username = request.form.get('username')
#         password = request.form.get('password')
#         output = netmiko.sh_int_terse(host, username, password)
#         return render_template('home.html', output=output)
#     return render_template('home.html')

##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 
##### ##### ##### ##### ## HOME ### ##### ##### ##### ##### 
##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 

# @app.route('/')
# def page_home():

##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 
##### ##### ##### ##### ### END ### ##### ##### ##### ##### 
##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 
