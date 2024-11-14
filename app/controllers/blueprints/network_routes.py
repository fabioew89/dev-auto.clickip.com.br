from app import db
from app.models.model import Table_Register
from app.controllers.netmiko import netmiko
from flask import Blueprint, request, render_template

network_bp = Blueprint('network',__name__)

# username = db.session.execute(db.select(Table_Register).filter_by(username=username)).scalar_one_or_none()

# Mostra a configuração de uma interface do Juniper - get_interface_configuration
@network_bp.route('/get_interface_configuration', methods=['GET','POST'])
def get_interface_configuration():
    if request.method == 'POST':
        hostname = request.form.get('hostname')
        username = request.form.get('username')
        password = request.form.get('password')
        unit = request.form.get('unit')
        output = netmiko.get_interface_summary(hostname, username, password, unit)
        return render_template('router/get_interface_configuration.html', output=output)
    return render_template('router/get_interface_configuration.html')

@network_bp.route('/get_interface_summary', methods=['GET','POST'])
def get_interface_summary():
    if request.method == 'POST':
        hostname = request.form.get('hostname')
        username = request.form.get('username')
        password = request.form.get('password')
        
        output = netmiko.get_interface_summary(hostname, username, password)
        return render_template('router/get_interface_summary.html', output=output)
    return render_template('router/get_interface_summary.html')
