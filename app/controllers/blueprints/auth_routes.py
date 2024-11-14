from flask import Blueprint, flash, redirect, url_for, render_template
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from app import db 
from app.controllers.forms import Form_Login
from app.models.model import Table_Register 

auth_bp = Blueprint('auth', __name__)

# Faz o login na aplicação.
@auth_bp.route('/login', methods=['GET', 'POST'])
def page_login():
    form = Form_Login()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        # Verificando se o usuário existe no banco de dados
        user = db.session.execute(db.select(Table_Register).filter_by(username=username)).scalar_one_or_none()

        if user and check_password_hash(user.password, password):
            login_user(user)
            flash(f'Sucesso ao logar {username}', category='success')
            return redirect(url_for('page_home'))
        else:
            flash('Email ou senha incorretos', category='danger')

    # Exibindo os erros dos campos do formulário, caso haja
    if form.errors:
        for field_name, err_messages in form.errors.items():
            for err in err_messages:
                flash(f'Erro no campo {field_name}: {err}', category='danger')

    return render_template('login.html', form=form)

# Faz o logout na aplicação.
@auth_bp.route('/logout')
def page_logout():
    logout_user()
    flash(f'Deslogado!!!', category='info')
    return redirect(url_for('page_home'))
