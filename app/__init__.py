from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from flask_login import LoginManager
from flask_admin import Admin


# Declarativa base para o SQLAlchemy
class Base(DeclarativeBase):
    pass


# Inicializando extensões
db = SQLAlchemy(model_class=Base)
lm = LoginManager()
admin = Admin(name='auto.clickip.local', template_mode='bootstrap4')


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    # Inicializando extensões com o app
    db.init_app(app)
    lm.init_app(app)
    admin.init_app(app)

    lm.login_view = 'auth.page_login'
    lm.login_message = 'Please log in to access this page.'
    lm.login_message_category = 'info'
    lm.session_protection = "strong"
    lm.refresh_view = "accounts.reauthenticate"
    lm.needs_refresh_message = (
        u"To protect your account, please reauthenticate to access this page."
    )
    lm.needs_refresh_message_category = "info"

    # Registrando blueprints
    from app.controllers.blueprints.user_routes import user_bp
    from app.controllers.blueprints.device_routes import device_bp
    from app.controllers.blueprints.network_routes import network_bp
    from app.controllers.blueprints.auth_routes import auth_bp

    app.register_blueprint(user_bp, url_prefix='/user')
    app.register_blueprint(device_bp, url_prefix='/device')
    app.register_blueprint(network_bp, url_prefix='/network')
    app.register_blueprint(auth_bp, url_prefix='/auth')

    # Rota básica para teste
    @app.route('/')
    def page_home():
        return render_template('home.html')

    return app
