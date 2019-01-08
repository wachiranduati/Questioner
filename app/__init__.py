import os
from flask import Flask
from Instance.config import app_config

def create_app(config_name):
	""" Method creating the flask application """
	app = Flask(__name__)
	app.config.from_object(app_config[config_name])

	@app.route('/')
	def home():
		return 'this is home'

	return app
