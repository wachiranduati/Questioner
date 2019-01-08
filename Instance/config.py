""" Flask configurations """

import os
import secrets


class Config(object):
    """Parent configuration class."""
    DEBUG = False
    TESTING = False
    # SECRET = os.getenv('SECRET')
    SECRET = secrets.token_hex(16) 


class DevelopmentConfig(Config):
    """Configurations for Development."""
    DEBUG = True
    TESTING = True


class TestingConfig(Config):
    """Configurations for Testing, with a separate test database."""
    TESTING = True
    DEBUG = True


class ProductionConfig(Config):
    """Configurations for Production."""
    DEBUG = False
    TESTING = False


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
}