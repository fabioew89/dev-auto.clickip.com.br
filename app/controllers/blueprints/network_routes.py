from flask import Blueprint, request, render_template, flash, redirect, url_for
from app.controllers.forms import Network_Form
from app.controllers.netmiko import netmiko
from app.models.model import Table_Register, Table_Devices
from app import db

# Inicializa o Blueprint
network_bp = Blueprint('network', __name__)


# Rota: get_interface_summary
@network_bp.route('/get_interface_summary', methods=['GET', 'POST'])
def get_interface_summary():
    users = db.session.execute(db.select(Table_Register)).scalars().all()
    devices = db.session.execute(db.select(Table_Devices)).scalars().all()

    output = None

    if request.method == 'POST':
        hostname = request.form.get('hostname')
        username = request.form.get('username')
        password = request.form.get('password')

        output = netmiko.get_interface_summary(
            hostname, username, password
        )

    return render_template(
        'router/get_interface_summary.html',
        output=output, users=users, devices=devices
    )


# Rota: get_interface_configuration
@network_bp.route('/get_interface_configuration', methods=['GET', 'POST'])
def get_interface_configuration():
    users = db.session.execute(db.select(Table_Register)).scalars().all()
    devices = db.session.execute(db.select(Table_Devices)).scalars().all()

    output = None

    if request.method == 'POST':
        hostname = request.form.get('hostname')
        username = request.form.get('username')
        password = request.form.get('password')
        unit = request.form.get('unit')

        output = netmiko.get_interface_configuration(
            hostname, username, password, unit
        )

    return render_template(
        'router/get_interface_configuration.html',
        output=output, users=users, devices=devices
    )


# Rota: set_interface_unit
@network_bp.route('/set_interface_unit', methods=['GET', 'POST'])
def set_interface_unit():
    form = Network_Form()

    output = None

    users = db.session.execute(
        db.select(Table_Register).order_by(Table_Register.id)
    ).scalars()
    hosts = db.session.execute(
        db.select(Table_Devices).order_by(Table_Devices.id)
    ).scalars()

    form.username.choices = [
        (user.username, user.username) for user in users
    ]
    form.hostname.choices = [
        (host.ip_address, host.hostname) for host in hosts
    ]

    if form.validate_on_submit():
        hostname = form.hostname.data
        username = form.username.data
        password = form.password.data
        unit = form.unit_vlan.data
        description = form.description.data
        bandwidth = form.bandwidth.data
        ipv4_gw = form.ipv4_gw.data
        ipv6_gw = form.ipv6_gw.data
        ipv6_cli = form.ipv6_cli.data
        inet6_48 = form.ipv6_48.data

        output = netmiko.set_interface_unit(
            hostname, username, password, unit, description,
            bandwidth, ipv4_gw, ipv6_gw, ipv6_cli, inet6_48
        )

        flash('Formulário enviado com sucesso!', category='success')

    else:
        if form.errors:
            for field, errors in form.errors.items():
                for error in errors:
                    flash(f"Erro no campo {field}: {error}", category='danger')

    return render_template(
        'router/set_interface_unit.html',
        output=output,
        form=form
    )
