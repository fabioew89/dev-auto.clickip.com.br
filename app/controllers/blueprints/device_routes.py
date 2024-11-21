<<<<<<< HEAD
from flask import Blueprint, request, render_template, redirect, url_for, flash
from app import db
from app.models.model import Table_Devices
from app.controllers.forms import Form_Devices

device_bp = Blueprint('device', __name__)

# Página de registro de dispositivos
@device_bp.route('/device', methods=['GET', 'POST'])
def page_register_device():
    form_device = Form_Devices(request.form)
    table = db.session.execute(db.select(Table_Devices)).scalars().all()

    if form_device.validate_on_submit():
        # Adicionando novo dispositivo
        new_device = Table_Devices(
            hostname=form_device.hostname.data,
            ip_address=form_device.ip_address.data
        )
        db.session.add(new_device)
        db.session.commit()
        flash('Novo dispositivo cadastrado com sucesso!', category='success')
        return redirect(url_for('device.page_register_device'))

    # Exibindo erros do formulário, se existirem
    for errors in form_device.errors.values():
        for error in errors:
            flash(f'Erro ao cadastrar dispositivo: {error}', category='danger')

    return render_template('device/page_register_device.html', form=form_device, table=table)

# Página de edição de dispositivos
@device_bp.route('/<int:id>/edit_device', methods=['GET', 'POST'])
def page_edit_device(id):
    # Busca o dispositivo pelo ID
    device = db.session.execute(db.select(Table_Devices).filter_by(id=id)).scalar_one_or_none()
    if device is None:
        flash(f'Dispositivo com ID {id} não encontrado.', category='danger')
        return redirect(url_for('device.page_register_device'))

    # Preenche o formulário com os dados do dispositivo
    form = Form_Devices(obj=device)

    if form.validate_on_submit():
        # Atualizando os dados do dispositivo
=======
from flask import Blueprint, flash, redirect, url_for, render_template, request
from app import db
from app.controllers.forms import Form_Devices
from app.models.model import Table_Devices

device_bp = Blueprint('device', __name__)

##### ##### ##### ##### ##### ##### ##### ##### ##### #####

@device_bp.route('/register', methods=['GET', 'POST'])
def page_register_device():
    form_device = Form_Devices(request.form)
    table = db.session.execute(db.select(Table_Devices)).scalars().all()
    
    if form_device.validate_on_submit():
        new_device_on_table = Table_Devices(
            hostname=form_device.hostname.data,
            ip_address=form_device.ip_address.data
        )
        db.session.add(new_device_on_table)
        db.session.commit()
        flash('Thanks for registering a new device!', category='success')
        return redirect(url_for('device.page_register_device'))
    
    if form_device.errors != {}:
        for err in form_device.errors.values():
            flash(f'Erro ao cadastrar usuario {err}', category='danger')
    
    return render_template('page_register_device.html', form=form_device, table=table)

##### ##### ##### ##### ##### ##### ##### ##### ##### #####

@device_bp.route('/<int:id>/edit', methods=['GET', 'POST'])
def page_edit_device(id):
    device = db.session.execute(db.select(Table_Devices).filter_by(id=id)).scalar_one_or_none()
    form = Form_Devices(obj=device)
    
    if device is None:
        flash(f'Device with ID {id} not found.', category='danger')
        return redirect(url_for('page_home'))
    
    if form.validate_on_submit():
>>>>>>> 2c0d98195d753f1a79cc745413b572c5c299943d
        device.hostname = form.hostname.data
        device.ip_address = form.ip_address.data
        db.session.commit()
        flash('Dispositivo atualizado com sucesso!', category='success')
<<<<<<< HEAD
        return redirect(url_for('device.page_register_device'))

    return render_template('device/page_edit_device.html', device=device, form=form)

# Rota para remoção de dispositivos
@device_bp.route('/<int:id>/remove_device')
def remove_device(id):
    # Busca o dispositivo pelo ID
=======
        return redirect(url_for('device.page_register_device', id=id))
    
    return render_template('page_edit_device.html', device=device, form=form)

##### ##### ##### ##### ##### ##### ##### ##### ##### #####

@device_bp.route('/<int:id>/remove')
def remove_device(id):
>>>>>>> 2c0d98195d753f1a79cc745413b572c5c299943d
    device = db.session.execute(db.select(Table_Devices).filter_by(id=id)).scalar_one_or_none()
    
    if device:
        db.session.delete(device)
        db.session.commit()
<<<<<<< HEAD
        flash('Dispositivo removido com sucesso!', category='success')
    else:
        flash('Dispositivo não encontrado.', category='danger')

=======
        flash('Device excluído com sucesso.', category='success')
    else:
        flash('Device não encontrado.', category='danger')
    
>>>>>>> 2c0d98195d753f1a79cc745413b572c5c299943d
    return redirect(url_for('device.page_register_device'))
