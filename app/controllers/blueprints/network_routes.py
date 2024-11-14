from flask import Blueprint, request, render_template
from app.controllers.netmiko import netmiko

network_bp = Blueprint('network',__name__)


@network_bp.route('/unit', methods=['GET', 'POST'])
def sh_config_int_unit():
    if request.method == 'POST':
        host = request.form.get('fhost')
        username = request.form.get('fusername')
        password = request.form.get('fpassword')
        unit = request.form.get('funit')
        output = netmiko.sh_config_int_unit(host, username, password, unit)
        return render_template('router/sh_config_int_unit.html', output=output)
    return render_template('router/sh_config_int_unit.html')

# @app.route('/', methods=['GET', 'POST'])
# def page_home():
#     if request.method == 'POST':
#         host = request.form.get('host')
#         username = request.form.get('username')
#         password = request.form.get('password')
#         output = netmiko.sh_int_terse(host, username, password)
#         return render_template('home.html', output=output)
#     return render_template('home.html')