from flask import render_template, jsonify
from app import app


@app.route('/')
def index():
	return render_template('index.html')


@app.route('/dashboard')
def dashboard():
	return render_template('dashboard.html')


@app.route('/group')
def group():
	return jsonify({"name": "Google Developer Group - Belo Horizonte"})


@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404
