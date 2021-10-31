import requests
from flask import Flask, render_template

from app.auth import auth
from app.user import user
from app.extensions import db, login_manager


def create_app(config):
    """Returns an initialized Flask application."""
    app = Flask(__name__, static_url_path='', static_folder='static')
    app.config.from_object(config)

    register_extensions(app)
    register_blueprints(app)
    register_errorhandlers(app)

    return app


def register_extensions(app):
    """Register extensions with the Flask application."""
    db.init_app(app)
    login_manager.init_app(app)


def register_blueprints(app):
    """Register blueprints with the Flask application."""
    app.register_blueprint(auth)
    app.register_blueprint(user)


def register_errorhandlers(app):
    """Register error handlers with the Flask application."""

    def render_error(e):
        return render_template('errors/%s.html' % e.code), e.code

    for e in [
        requests.codes.INTERNAL_SERVER_ERROR,
        requests.codes.NOT_FOUND,
        requests.codes.UNAUTHORIZED,
    ]:
        app.errorhandler(e)(render_error)
