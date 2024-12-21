from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, login_user, logout_user
from app import db
from app.models import Users
from app.controllers.forms import LoginForm
from werkzeug.security import check_password_hash
from cryptography.fernet import Fernet

f = Fernet(Fernet.generate_key())

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = db.session.execute(
            db.select(Users).filter_by(username=username)
        ).scalar_one_or_none()

        if user and check_password_hash(user.password, password):
            login_user(user, remember=True)
            flash(f'Sucesso ao logar {username}', category='success')
            return redirect(url_for('network.interface_summary'))
        else:
            flash('Email ou senha incorretos', category='danger')

    if form.errors:
        for field_name, err_messages in form.errors.items():
            for err in err_messages:
                flash(f'Erro no campo {field_name}: {err}', category='danger')

    return render_template('login.html', form=form)


@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Deslogado!!!', category='info')
    return redirect(url_for('auth.login'))
