import os
import secrets


class Config(object):
    """Parent configuration class."""
    DEBUG = False
    TESTING = False
    # SECRET = os.getenv('SECRET')
    SECRET = secrets.token_hex(16) 


class DevelopmentConfig(Config):
    """Configurtions for Development."""
    DEBUG = True
    TESTING = True


class TestingConfig(Config):
    """Configurations for Testing """
    TESTING = True
    DEBUG = True


class ProductionConfig(Config):
    """Configuration for Production."""
    DEBUG = False
    TESTING = False


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
}