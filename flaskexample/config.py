import os


class Config(object):
    TESTING = False
    # python -c 'import secrets; print(secrets.token_hex())'
    SECRET_KEY = '192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf'

class DevelopmentConfig(Config):
    """Development"""
    DATABASE_URI = "sqlite:////tmp/foo.db"
    DATABASE = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'instance')), 'flaskexample.sqlite')
    SQLALCHEMY_ECHO = True

class TestingConfig(Config):
    """测试环境"""
    TESTING = True
    DATABASE_URI = 'sqlite:///:memory:'

class UatConfig(Config):
    """Production"""

class ProductionConfig(Config):
    """Production"""
    DATABASE_URI = 'mysql://user@localhost/foo'


config_dict = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'uat': UatConfig,
    'production': ProductionConfig,
}