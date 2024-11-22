from flask import render_template
from app import app
from app.models.model import *

@app.route('/')
def page_home():
    return render_template('home.html')