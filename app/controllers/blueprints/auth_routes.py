from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from app import app, db
from app.models.model import *
from app.controllers.forms import *
from app.controllers import netmiko
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint('auth',__name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def page_login():
    form = Form_Login()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = db.session.execute(db.select(Table_Register).filter_by(username=username)).scalar_one_or_none()
        
        if user and check_password_hash(user.password, password):
            login_user(user)
            flash(f'Sucesso ao logar {username}', category='success')
            return redirect(url_for('page_home'))
        else:
            flash('Email ou senha incorretos', category='danger')
    
    if form.errors:
        for field_name, err_messages in form.errors.items():
            for err in err_messages:
                flash(f'Erro no campo {field_name}: {err}', category='danger')
    
    return render_template('login.html', form=form)

@auth_bp.route('/logout')
def page_logout():
    logout_user()
    flash(f'Deslogado!!!', category='info')
    return redirect(url_for('page_home'))