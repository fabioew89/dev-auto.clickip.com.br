from flask import request, render_template, redirect, url_for, flash
from app import app, db
from app.controllers import netmiko
from app.controllers.forms import Form_Cad_User, Form_New_Cad
from app.models.model import Tab_User, Tab_New_Users

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

# route for cad users.
@app.route('/new_user', methods=['GET', 'POST'])
def page_cad_new_user():
    form = Form_Cad_User(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        user_table = Tab_User(
            username = form.username.data,
            email = form.email.data,
        )
        db.session.add(user_table)
        db.session.commit()
        flash('Thanks for registering')
        return redirect(url_for('page_home'))
    if form.errors != {}:
        for err in form.errors.values():
            flash(f' Erro ao cadastrar usuario {err}', category='danger')
    return render_template('cadastro.html', form=form)

@app.route('/novo_cadastro', methods=['GET', 'POST'])
def page_new_cad():
    form = Form_New_Cad(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        user_table = Tab_New_Users(
            email = form.email.data,
            password_bcrypt = form.password.data,
        )
        db.session.add(user_table)
        db.session.commit()

        flash('Obrigado por cadastrar')
        return redirect(url_for('page_home'))
    if form.errors != {}:
        for err in form.errors.values():
            flash(f' Erro ao cadastrar usuario {err}', category='danger')    
    return render_template('novo_cadastro.html', form=form)    