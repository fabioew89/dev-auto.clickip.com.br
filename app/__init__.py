from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from livereload import Server

app = Flask(__name__)

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

app.config['SECRET_KEY'] = 'f6b42562bc1f3ee92dbad7c9'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
db.init_app(app)

from app.controllers import routes

# # Only for frontend!
# server = Server(app.wsgi_app)
# server.watch('app/templates/*.*')
# server.watch('app/static/**/*.*')
# server.serve(port=5000)
