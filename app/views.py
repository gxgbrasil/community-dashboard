from flask import render_template, jsonify, request
from app import app
from meetupapi import MeetupAPI


@app.route('/')
def index():
	return render_template('index.html')


@app.route('/dashboard/', methods=['GET'])
def dashboard():
	return render_template('dashboard.html', urlname=request.args['urlname'])


@app.route('/group')
def group():
	meetup_api = MeetupAPI()
	return jsonify(meetup_api.get_group('GDG-BH'))


@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404
