from flask import Flask, request, render_template, Response, redirect, url_for, session
from functools import wraps
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
import random
from flask import jsonify
from sqlalchemy.orm import load_only
import datetime
import json
from serializer import *
import flask_login
import os
from flask_login import current_user, login_user

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):

	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
	SQLALCHEMY_TRACK_MODIFICATIONS = False

	DEBUG = True
	SECRET_KEY = 'W9xJeJKrUqiG9cONoM4O9ZtpZ1k4wrRJXexHtP8V'

app = Flask(__name__, static_url_path='/static')
app.config.from_object(Config)
login = flask_login.LoginManager(app)
login_required = flask_login.login_required
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import *

@login.user_loader
def load_user(id):
	return User.query.get(int(id))

@app.route('/<path:path>')
def static_file(path):
	return app.send_static_file(path)


from flask_wtf import FlaskForm


@app.route('/login', methods=['GET', 'POST'])
def login():

	if current_user.is_authenticated:
		return redirect(url_for('home'))

	user = User.query.filter_by(name=request.form['username']).first()
	if user is None or not user.check_password(request.form['password']):

		flash('Invalid username or password')
		return redirect(url_for('login'))
	login_user(user, remember=True)
	return redirect(url_for('home'))

	return render_template('login.html', form=form)


@app.route('/', methods=['GET'])
def login_page():

	if 'username' in session:
		return redirect(url_for('home'))

	return render_template('login.html')


@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('login_page'))



@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def home():
	users = User.query.all()
	data = {'users': users}
	return render_template('index.html', data=data)


@app.before_first_request
def create_users():

	user = User.query.get(1)

	if user is not None:
		return

	for i in ['maciek', 'patryk', 'wojtek', 'dawid']:
		u = User(name=i)
		u.set_password('1234')
		db.session.add(u)
	db.session.commit()


if __name__ == '__main__':
	db.create_all()
	
	db.init_app(app)

	app.run(host='0.0.0.0', port=5000)