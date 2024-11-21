from flask import request, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from app import app, db
from app.models.model import *
from app.controllers.forms import *
from app.controllers import netmiko
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





##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 



##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 
##### ##### ##### ##### ## LOGIN ## ##### ##### ##### ##### 
##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 



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
def remove_device(id):
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



##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 
##### ##### ##### ##### # NETMIKO # ##### ##### ##### ##### 
##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 

##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 
##### ##### ##### ##### ### END ### ##### ##### ##### ##### 
##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 
