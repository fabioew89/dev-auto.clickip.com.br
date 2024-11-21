from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
<<<<<<< HEAD
from flask_login import LoginManager

# Configuração inicial do Flask
=======
from sqlalchemy.orm import DeclarativeBase

# Configuração básica do app
>>>>>>> 2c0d98195d753f1a79cc745413b572c5c299943d
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///application.db'
app.config['SECRET_KEY'] = 'f6b42562bc1f3ee92dbad7c9'

<<<<<<< HEAD
# Instância de extensões
db = SQLAlchemy()
=======
# Base declarativa do SQLAlchemy
class Base(DeclarativeBase):
    pass

# Inicializando o banco de dados e login manager
db = SQLAlchemy(model_class=Base)
>>>>>>> 2c0d98195d753f1a79cc745413b572c5c299943d
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'page_home'
login_manager.login_message = 'Faça seu login'
login_manager.login_message_category = 'info'

<<<<<<< HEAD
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
=======
# Registrando blueprints - **importando os blueprints depois da configuração do app**
from app.controllers.blueprints.user_routes import user_bp
from app.controllers.blueprints.device_routes import device_bp
from app.controllers.blueprints.network_routes import network_bp
from app.controllers.blueprints.auth_routes import auth_bp

app.register_blueprint(user_bp, url_prefix='/user')
app.register_blueprint(device_bp, url_prefix='/device')
app.register_blueprint(network_bp, url_prefix='/network')
app.register_blueprint(auth_bp, url_prefix='/auth')

# Importando rotas adicionais se necessário
from app.controllers import routes

# Configuração opcional para desenvolvimento (Livereload)
# Somente para o frontend!
# from livereload import Server
# server = Server(app.wsgi_app)
# server.watch('app/templates/*.*')
# server.watch('app/static/**/*.*')
# server.serve(port=5000)
>>>>>>> 2c0d98195d753f1a79cc745413b572c5c299943d
