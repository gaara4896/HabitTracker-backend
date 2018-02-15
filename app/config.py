import os
import urllib.parse
from datetime import timedelta

from .extensions import env

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
env = os.path.join(base_dir, '.env')


class Config(object):
    """ Configure application with envionment variables. """

    @classmethod
    def init_app(self, app):
        env = DotEnv()
        env.init_app(app, env_file=env, verbose_mode=True)

    DEBUG = os.environ.get('DEBUG')
    TESTING = os.environ.get('TESTING')

    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get(
        'SQLALCHEMY_TRACK_MODIFICATIONS')
    SQLALCHEMY_POOL_SIZE = 100
    SQLALCHEMY_POOL_RECYCLE = 3600
    SQLALCHEMY_POOL_TIMEOUT = 1800

    SECRET_KEY = os.environ.get('SECRET_KEY')

    MSEARCH_BACKEND = 'whoosh'
    MSEARCH_ENABLE = True

    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=24)
    UPLOAD_FOLDER = 'upload/'
    MAX_CONTENT_PATH = 26214400

    # Flask Mail: https://pythonhosted.org/Flask-Mail/
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = os.environ.get('MAIL_PORT')
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS')
    MAIL_USE_SSL = os.environ.get('MAIL_USE_SSL')
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER')

    # EMAIL_SUBJECT_PREFIX = '[{}]'.format(APP_NAME)
