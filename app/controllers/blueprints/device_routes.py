from flask import Blueprint, request, render_template, redirect, url_for, flash
from app import db
from app.models.model import Table_Devices
from app.controllers.forms import Form_Devices

device_bp = Blueprint('device', __name__)


# Rota para registrar um novo dispositivo
@device_bp.route('/create', methods=['GET', 'POST'])
def page_register_device():
    form_device = Form_Devices(request.form)
    table = db.session.execute(db.select(Table_Devices)).scalars().all()

    if form_device.validate_on_submit():
        # Insere um novo dispositivo na tabela
        new_device = Table_Devices(
            hostname=form_device.hostname.data,
            ip_address=form_device.ip_address.data
        )
        db.session.add(new_device)
        db.session.commit()
        flash('Novo dispositivo cadastrado com sucesso!', category='success')
        return redirect(url_for('device.page_register_device'))

    # Exibe mensagens de erro do formulário, se existirem
    for errors in form_device.errors.values():
        for error in errors:
            flash(f'Erro ao cadastrar dispositivo: {error}', category='danger')

    return render_template(
        'device/page_register_device.html',
        form=form_device,
        table=table)


# Rota para editar os dados de um dispositivo existente
@device_bp.route('/<int:id>/edit', methods=['GET', 'POST'])
def page_edit_device(id):
    # Localiza o dispositivo pelo ID
    device = db.session.execute(
        db.select(Table_Devices).filter_by(id=id)
    ).scalar_one_or_none()
    if device is None:
        flash(f'Dispositivo com ID {id} não encontrado.', category='danger')
        return redirect(url_for('device.page_register_device'))

    # Preenche o formulário com os dados do dispositivo localizado
    form = Form_Devices(obj=device)

    if form.validate_on_submit():
        # Atualiza os dados do dispositivo na tabela
        device.hostname = form.hostname.data
        device.ip_address = form.ip_address.data
        db.session.commit()
        flash('Dispositivo atualizado com sucesso!', category='success')
        return redirect(url_for('device.page_register_device'))

    return render_template(
        'device/page_edit_device.html',
        device=device,
        form=form)


# Rota para remover um dispositivo existente
@device_bp.route('/<int:id>/del')
def remove_device(id):
    # Localiza o dispositivo pelo ID
    device = db.session.execute(
        db.select(Table_Devices).filter_by(id=id)
    ).scalar_one_or_none()

    if device:
        # Remove o dispositivo localizado
        db.session.delete(device)
        db.session.commit()
        flash('Dispositivo removido com sucesso!', category='success')
    else:
        # Informa que o dispositivo não foi encontrado
        flash('Dispositivo não encontrado.', category='danger')

    return redirect(url_for('device.page_register_device'))
