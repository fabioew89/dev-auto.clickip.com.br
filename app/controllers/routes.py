from flask import request, render_template, redirect, url_for, flash
from app import app, db
from app.models.model import *
from app.controllers import netmiko

@app.route('/')
def page_home():
    return render_template('home.html')