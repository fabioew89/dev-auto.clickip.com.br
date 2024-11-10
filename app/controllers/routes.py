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

##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 
##### ##### ##### ##### REGISTER ## ##### ##### ##### ##### 
##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 

@app.route('/register', methods=['GET', 'POST'])
def page_register():
    form = Form_Register()
    if form.validate_on_submit():
        
        user = Tab_Register(
            username = form.username.data,
            password = generate_password_hash(form.password.data, method='pbkdf2:sha256')
        )
        db.session.add(user)
        db.session.commit()
        flash('Thanks for registering', category='success')
        return redirect(url_for('page_register'))
    
    if form.errors != {}:
        for err in form.errors.values():
            flash(f' Erro ao cadastrar usuario {err}', category='danger')
    
    return render_template('page_register_user.html', form=form, table=Tab_Register())

##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 
##### ##### ##### ##### ## LOGIN ## ##### ##### ##### ##### 
##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 

from werkzeug.security import check_password_hash
from flask_login import login_user

@app.route('/login', methods=['GET', 'POST'])
def page_login():
    form = Form_Login()
    
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        
        # Obter o usuário pelo nome de usuário
        user = db.session.execute(db.select(Tab_Register).filter_by(username=username)).scalar_one_or_none()

        if user and check_password_hash(user.password, password):  # Verifique se a senha corresponde ao hash
            login_user(user)  # Passa o objeto do usuário, não o nome de usuário
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
##### ##### ##### ### REGISTER DEVICE ### ##### ##### ##### 
##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 

@app.route('/device', methods=['GET', 'POST'])
def page_register_device():
    form_device = Form_Devices(request.form)
    table = db.session.execute(db.select(Table_Devices)).scalars().all()
    if form_device.validate_on_submit():
        new_device_on_table = Table_Devices(
            hostname = form_device.hostname.data,
            ip_address = form_device.ip_address.data
        )
        
        db.session.add(new_device_on_table)
        db.session.commit()
        flash(f'Thanks for registering a new device!', category='success')
        return redirect(url_for('page_register_device'))
    
    if form_device.errors != {}:
        for err in form_device.errors.values():
            flash(f' Erro ao cadastrar usuario {err}', category='danger')
    return render_template('page_register_device.html', form=form_device, table=table)

##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 

@app.route('/<int:id>/edit_device', methods=['GET', 'POST'])
def page_edit_device(id):
    device = db.session.execute(db.select(Table_Devices).filter_by(id=id)).scalar_one_or_none()
    form = Form_Devices(obj=device)
    
    if device is None:
        flash(f'Device with ID {id} not found.', category='danger')
        return redirect(url_for('page_home'))
    
    if form.validate_on_submit():
        device.hostname = form.hostname.data
        device.ip_address = form.ip_address.data
        
        db.session.commit()
        flash('Dispositivo atualizado com sucesso!', category='success')
        return redirect(url_for('page_register_device', id=id))
    
    return render_template('page_edit_device.html', device=device, form=form)

##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 

@app.route('/<int:id>/remove_device')
def page_remove_device(id):
    device = db.session.execute(db.select(Table_Devices).filter_by(id=id)).scalar_one_or_none()
    
    if device:
        db.session.delete(device)
        db.session.commit()
        flash('Device excluído com sucesso.', category='success')
    else:
        flash('Device não encontrado.', category='danger')

    return redirect(url_for('page_register_device'))


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
