from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

# Configuração básica do app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///application.db'
app.config['SECRET_KEY'] = 'f6b42562bc1f3ee92dbad7c9'

# Base declarativa do SQLAlchemy
class Base(DeclarativeBase):
    pass

# Inicializando o banco de dados e login manager
db = SQLAlchemy(model_class=Base)
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'page_home'
login_manager.login_message = 'Faça seu login'
login_manager.login_message_category = 'info'

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
