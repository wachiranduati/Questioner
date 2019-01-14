import os
from flask import Flask
from Instance.config import app_config
from flask_restplus import Api, Resource


def create_app(config_name):
    """ Method creating the flask application """
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    api = Api(app)

    from app.api.v1.views.Admin_Views import admin
    from app.api.v1.views.user_views import users
    app.register_blueprint(admin)
    app.register_blueprint(users)

    return app
