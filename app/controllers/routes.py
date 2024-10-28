from flask import request, render_template, redirect, url_for, flash
from app import app, db
from app.controllers import netmiko
from app.controllers.forms import Form_Register
from app.models.model import Tab_Register

@app.route('/', methods=['GET', 'POST'])
def page_home():
    if request.method == 'POST':
        host = request.form.get('host')
        username = request.form.get('username')
        password = request.form.get('password')
        output = netmiko.sh_int_terse(host, username, password)
        return render_template('index.html', output=output)
    return render_template('index.html')

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

@app.route('/register', methods=['GET', 'POST']) #register users?
def page_register():
    form = Form_Register(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        table_user = Tab_Register(
            email = form.email.data,
            password_bcrypt = form.password.data,
        )
        db.session.add(table_user)
        db.session.commit()
        flash('Thanks for registering')
        return redirect(url_for('page_home'))
    if form.errors != {}:
        for err in form.errors.values():
            flash(f' Erro ao cadastrar usuario {err}', category='danger')
    return render_template('register.html', form=form)

@app.route('/login')
def page_login():
    return render_template('login.html')