import os
from flask import Flask

from .config import Config
from .apis import api
from .extensions import db, env, jwt, mail, migrate


def create_app():

    app = Flask(__name__)

    # set config
    app_env = os.getenv('APP_ENV', 'development')
    app.config.from_object(Config)
    env.init_app(app)

    # initialise extensions
    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)
    mail.init_app(app)

    api.init_app(app)

    return app
