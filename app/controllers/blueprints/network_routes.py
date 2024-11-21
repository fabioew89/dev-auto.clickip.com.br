<<<<<<< HEAD
from flask import Blueprint, request, render_template
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
=======
from app import app, db
from app.controllers.netmiko import netmiko
from app.models.model import Table_Register, Table_Devices
from flask import Blueprint, request, render_template

network_bp = Blueprint('network',__name__)

with app.app_context():
    users = db.session.execute(db.select(Table_Register)).scalars().all()
    devices = db.session.execute(db.select(Table_Devices)).scalars().all()

# get_interface_summary
@network_bp.route('/get_interface_summary', methods=['GET','POST'])
def get_interface_summary():
    
    output = None
    
>>>>>>> 2c0d98195d753f1a79cc745413b572c5c299943d
    if request.method == 'POST':
        hostname = request.form.get('hostname')
        username = request.form.get('username')
        password = request.form.get('password')
<<<<<<< HEAD

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
=======
        
        output = netmiko.get_interface_summary(hostname, username, password)
        
    return render_template('router/get_interface_summary.html', 
                               output=output, 
                               users=users, 
                               devices=devices)

# get_interface_configuration
@network_bp.route('/get_interface_configuration', methods=['GET','POST'])
def get_interface_configuration():
    
    output = None
    
>>>>>>> 2c0d98195d753f1a79cc745413b572c5c299943d
    if request.method == 'POST':
        hostname = request.form.get('hostname')
        username = request.form.get('username')
        password = request.form.get('password')
        unit = request.form.get('unit')
<<<<<<< HEAD

        output = netmiko.get_interface_configuration(hostname, username, password, unit)

    return render_template(
        'router/get_interface_configuration.html',
        output=output,
        users=users,
        devices=devices
    )
=======
        output = netmiko.get_interface_configuration(hostname, username, password, unit)
    return render_template('router/get_interface_configuration.html', 
                               output=output, 
                               users=users, 
                               devices=devices)
>>>>>>> 2c0d98195d753f1a79cc745413b572c5c299943d
