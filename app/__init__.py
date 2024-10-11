from flask import Flask
from livereload import Server

app = Flask(__name__)

from app.controllers import routes

server = Server(app.wsgi_app)
server.watch('app/templates/*.*')
server.watch('app/static/*.*')
server.serve(port=5000)