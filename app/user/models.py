from datetime import datetime
from app.extensions import db
from app.auth.models import AuthenticatedUserMixin


class User(AuthenticatedUserMixin, db.Model):
    __table_args__ = {'extend_existing': True}

    posts = db.relationship('Post', backref='author', lazy='dynamic')

    @classmethod
    def create(cls, password, **kwargs):
        instance = cls(password, **kwargs)
        return instance.save()

    def save(self, commit=True):
        db.session.add(self)
        if commit:
            db.session.commit()
        return self


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(140))
    country = db.Column(db.String(140))
    description = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.description)
