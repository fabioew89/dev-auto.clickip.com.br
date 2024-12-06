from flask import Flask, render_template
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase


# Declarativa base para o SQLAlchemy
class Base(DeclarativeBase):
    pass


# Inicializando extensões
db = SQLAlchemy(model_class=Base)
login_manager = LoginManager()


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SECRET_KEY'] = 'f6b42562bc1f3ee92dbad7c9'

    # Inicializando extensões com o app
    db.init_app(app)
    login_manager.init_app(app)

    login_manager.login_view = 'auth.page_login'
    login_manager.login_message = 'Faça seu login'
    login_manager.login_message_category = 'info'

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
