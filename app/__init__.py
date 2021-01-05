import os

from flask import Flask
from celery import Celery
from flask_sqlalchemy import SQLAlchemy

CONFIG_OBJ = 'app.config.Config'


def create_app():
    application = Flask(__name__)
    application.config.from_object(CONFIG_OBJ)
    application.app_context().push()

    initialize_extensions(application)
    register_blueprints(application)
    initialize_bootstrap(application)
    initialize_cache(application)
    return application


def initialize_extensions(application):
    from app.models.DOSCG import DOSCG

    db = SQLAlchemy(application)


def register_blueprints(application):
    from app.views import DOSCG_blueprints

    application.register_blueprint(DOSCG_blueprints)


def initialize_bootstrap(application):
    from flask_bootstrap import Bootstrap
    bootstrap = Bootstrap(application)


def initialize_cache(application):
    from app.controllers.DOSCG import cache
    cache.init_app(application, config={'CACHE_TYPE': 'simple'})


app = Flask(__name__)
app.config.from_object(CONFIG_OBJ)
db = SQLAlchemy(app)
