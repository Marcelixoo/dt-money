from os import environ

if environ.get('DATABASE_URL'):
    SQLALCHEMY_DATABASE_URI = (
        environ.get('DATABASE_URL').replace("://", "ql://", 1))
else:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///storage/database.db'

DEBUG = True
CSRF_ENABLED = False
SECRET_KEY = 'codecademyisajoke'
SQLALCHEMY_TRACK_MODIFICATIONS = False
