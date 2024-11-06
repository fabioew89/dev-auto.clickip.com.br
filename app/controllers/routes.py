from flask import request, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from app import app, db
from app.controllers import netmiko
from app.controllers.forms import *
from app.models.model import *
from werkzeug.security import generate_password_hash, check_password_hash

##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 
##### ##### ##### ##### ## INDEX ## ##### ##### ##### ##### 
##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 

@app.route('/')
def page_home():
    return render_template('home.html')

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
#     table = db.session.execute(db.select(Tab_Register)).scalars().all()
#     return render_template('home.html', table=table)

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

##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 
##### ##### ##### ##### REGISTER ## ##### ##### ##### ##### 
##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 

@app.route('/register', methods=['GET', 'POST']) #register users?
@login_required
def page_register_user():
    form = Form_Register(request.form)
    if form.validate_on_submit():
        
        new_user = Tab_Register(
            email = form.email.data,
            password = generate_password_hash(form.password.data, method='pbkdf2:sha256')
        )
        db.session.add(new_user)
        db.session.commit()
        flash('Thanks for registering')
        return redirect(url_for('page_home'))
    if form.errors != {}:
        for err in form.errors.values():
            flash(f' Erro ao cadastrar usuario {err}', category='danger')
    return render_template('page_register_user.html', form=form)

@app.route('/device', methods=['GET', 'POST'])
def page_register_device():
    form_device = Form_Devices(request.form)
    if form_device.validate_on_submit():
        new_device_on_table = Table_Devices(
            device_name = form_device.device_name.data,
            ip_address = form_device.ip_address.data
        )
        db.session.add(new_device_on_table)
        db.session.commit()
        flash(f'Thanks for registering a new device!')
        redirect(url_for('page_home'))
    
    if form_device.errors != {}:
        for err in form_device.errors.values():
            flash(f' Erro ao cadastrar usuario {err}', category='danger')        
    render_template('page_register_device.html', form=form_device)

##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 
##### ##### ##### ##### ## LOGIN ## ##### ##### ##### ##### 
##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 

@app.route('/login', methods=['GET', 'POST']) # login users?
def page_login():
    form = Form_Login()
    
    if form.validate_on_submit():  # Valida os dados do formulário
        email = form.email_login.data
        password = form.password_login.data
        
        # Tenta encontrar o usuário no banco de dados
        loged_user = Tab_Register.query.filter_by(email=email).first()

        # Verifica a senha usando check_password_hash
        if loged_user and check_password_hash(loged_user.password, password):
            login_user(loged_user)
            flash(f'Sucesso ao logar {loged_user.email}', category='success')
            return redirect(url_for('page_home'))
        else:
            flash('Email ou senha incorretos', category='danger')
    
    # Exibe erros de validação, se houver
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
##### ##### ##### ##### ### END ### ##### ##### ##### ##### 
##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 
