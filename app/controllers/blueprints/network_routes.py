from flask import Blueprint, request, render_template, flash
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

        output = netmiko.get_interface_summary(hostname, username, password)

    return render_template(
        'router/get_interface_summary.html',
        output=output,
        users=users,
        devices=devices
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
        output=output,
        users=users,
        devices=devices
    )


# Rota: set_interface_unit
@network_bp.route('/set_interface_unit', methods=['GET', 'POST'])
def set_interface_unit():
    form = Network_Form()

    output = None

    # list users and devices in database
    users = db.session.execute(
        db.select(Table_Register).order_by(Table_Register.id)
    ).scalars()

    devices = db.session.execute(
        db.select(Table_Devices).order_by(Table_Devices.id)
    ).scalars()

    # create a tupla for users and devices
    form.username.choices = [
        (username.username, username.username) for username in users
    ]

    form.device.choices = [
        (device.ip_address, device.hostname) for device in devices
    ]

    if form.validate_on_submit():
        # selected_device = form.device.data
        flash('', )

    return render_template(
        'router/set_interface_unit.html',
        output=output,
        form=form
    )
