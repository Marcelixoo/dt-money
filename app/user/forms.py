from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import ValidationError, DataRequired
from app.user.models import User


class DestinationForm(FlaskForm):
    city = StringField('city', validators=[DataRequired()])
    country = StringField('country', validators=[DataRequired()])
    description = StringField('description')
    submit = SubmitField('Post')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError(
                'Username already taken! Please use a different username.'
            )

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()

        if user is not None:
            raise ValidationError(
                'Email already taken! Please use a different email address.'
            )
