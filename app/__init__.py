from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from app.controllers.blueprints.user_routes import user_bp

app = Flask(__name__)

app.register_blueprint(user_bp)

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///application.db'
app.config['SECRET_KEY'] = 'f6b42562bc1f3ee92dbad7c9'

db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'page_home'
login_manager.login_message = 'Faça seu login'
login_manager.login_message_category = 'info'

from app.controllers import routes

# # Only for frontend!
# from livereload import Server
# server = Server(app.wsgi_app)
# server.watch('app/templates/*.*')
# server.watch('app/static/**/*.*')
# server.serve(port=5000)
