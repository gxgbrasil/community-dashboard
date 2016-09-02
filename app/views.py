from flask import render_template, request
from app import app


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/dashboard/', methods=['GET'])
def dashboard():
    return render_template('dashboard.html', urlname=request.args['urlname'])


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
