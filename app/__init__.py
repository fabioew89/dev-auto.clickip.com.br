from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Configuração inicial do Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///application.db'
app.config['SECRET_KEY'] = 'f6b42562bc1f3ee92dbad7c9'

# Instância de extensões
db = SQLAlchemy()
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'page_home'
login_manager.login_message = 'Faça seu login'
login_manager.login_message_category = 'info'

# Registro de blueprints (mover para o final para evitar importação circular)
def register_blueprints():
    from app.controllers.blueprints.auth_routes import auth_bp
    from app.controllers.blueprints.user_routes import user_bp
    from app.controllers.blueprints.device_routes import device_bp
    from app.controllers.blueprints.network_routes import network_bp
    
    app.register_blueprint(network_bp,  url_prefix='/network')
    app.register_blueprint(auth_bp,     url_prefix='/auth')
    app.register_blueprint(user_bp,     url_prefix='/user')
    app.register_blueprint(device_bp,   url_prefix='/device')

# Registro de rotas gerais (mover para o final para evitar importação circular)
def register_routes():
    from app.controllers import routes

# Registrando blueprints e rotas ao final
register_blueprints()
register_routes()
