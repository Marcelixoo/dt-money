from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app.extensions import db


class AuthenticatedUserMixin(UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, index=True)
    email = db.Column(db.String(120), unique=True, index=True)
    password_hash = db.Column(db.String(60), nullable=False)

    def __init__(self, password, **kwargs):
        super(AuthenticatedUserMixin, self).__init__(**kwargs)
        self.set_password(password)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password_to_check):
        return check_password_hash(self.password_hash, password_to_check)

    def __repr__(self):
        return '<User {}>'.format(self.username)
