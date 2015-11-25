# encoding: utf-8

from flask.ext.sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from flask.ext.login import LoginManager
login_manager = LoginManager()

from flask.ext.marshmallow import Marshmallow
marshmallow = Marshmallow()

from . import api

from .auth import OAuth2Provider
oauth2 = OAuth2Provider()


def init_app(app):
    for extension in (
        db,
        login_manager,
        marshmallow,
        api,
        oauth2,
    ):
        extension.init_app(app)

    class AlembicDatabaseMigrationConfig(object):
        def __init__(self, database, directory='migrations', **kwargs):
            self.db = database
            self.directory = directory
            self.configure_args = kwargs
    app.extensions['migrate'] = AlembicDatabaseMigrationConfig(db, compare_type=True)

    from sqlalchemy_utils import force_auto_coercion, force_instant_defaults
    force_auto_coercion()
    force_instant_defaults()
