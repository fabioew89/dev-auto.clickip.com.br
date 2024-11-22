from flask import Blueprint, flash, url_for, redirect, render_template
from app import db
from app.controllers.forms import Form_Register
from app.models.model import Table_Register
from werkzeug.security import generate_password_hash

user_bp = Blueprint('user', __name__)

# Página para registro de usuários
@user_bp.route('/create', methods=['GET', 'POST'])
def page_register():
    form = Form_Register()
    table = db.session.execute(db.select(Table_Register)).scalars().all()
    
    if form.validate_on_submit():
        # Criação de um novo usuário com senha criptografada
        user = Table_Register(
            username=form.username.data,
            password=generate_password_hash(form.password.data, method='pbkdf2:sha256')
        )
        db.session.add(user)
        db.session.commit()
        flash('Usuário cadastrado com sucesso!', category='success')
        return redirect(url_for('user.page_register'))
    
    # Exibe mensagens de erro do formulário, se houver
    for errors in form.errors.values():
        for error in errors:
            flash(f'Erro ao cadastrar usuário: {error}', category='danger')
    
    return render_template('user/page_register_user.html', form=form, table=table)

# Página para edição de usuários
@user_bp.route('/<int:id>/edit', methods=['GET', 'POST'])
def page_edit_user(id):
    # Busca o usuário no banco de dados
    user = db.session.execute(db.select(Table_Register).filter_by(id=id)).scalar_one_or_none()
    if user is None:
        flash(f'Usuário com ID {id} não encontrado.', category='danger')
        return redirect(url_for('user.page_register'))

    # Preenche o formulário com os dados do usuário
    form = Form_Register(obj=user)
    
    if form.validate_on_submit():
        # Atualização dos dados do usuário
        user.username = form.username.data
        if form.password.data:  # Atualiza a senha apenas se for fornecida
            user.password = generate_password_hash(form.password.data, method='pbkdf2:sha256')
        db.session.commit()
        flash('Usuário atualizado com sucesso!', category='success')
        return redirect(url_for('user.page_register'))

    return render_template('user/page_edit_user.html', user=user, form=form)

# Página para remoção de usuários
@user_bp.route('/<int:id>/del')
def remove_user(id):
    # Busca o usuário no banco de dados
    user = db.session.execute(db.select(Table_Register).filter_by(id=id)).scalar_one_or_none()
    
    if user:
        # Remove o usuário do banco de dados
        db.session.delete(user)
        db.session.commit()
        flash('Usuário excluído com sucesso!', category='success')
    else:
        flash('Usuário não encontrado.', category='danger')
    
    return redirect(url_for('user.page_register'))
