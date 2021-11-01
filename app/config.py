from os import environ


def resolve_db_uri():
    if environ.get('DATABASE_URL'):
        return environ.get('DATABASE_URL').replace("://", "ql://", 1)
    return 'sqlite:///storage/database.db'


FLASK_ENV = 'development'
FLASK_APP = 'run'
DEBUG = True
CSRF_ENABLED = False
SECRET_KEY = 'codecademyisajoke'
SQLALCHEMY_DATABASE_URI = resolve_db_uri()
SQLALCHEMY_TRACK_MODIFICATIONS = False
