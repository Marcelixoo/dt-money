from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import current_user, login_user, logout_user
from app.extensions import login_manager
from app.auth.forms import RegistrationForm, LoginForm
from app.user.models import User


blueprint = Blueprint('auth', __name__, template_folder='templates')


login_manager.login_view = 'auth.login'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('user.index'))

    form = LoginForm(meta={'csrf': False})

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).one()
        login_user(user, remember=form.remember_me.data)
        flash('Logged in successfully')
        return redirect(url_for('user.index'))
    return render_template('login.html', title='Sign In', form=form)


@blueprint.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('auth.login'))

    form = RegistrationForm(meta={'csrf': False})

    if form.validate_on_submit():
        User.create(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data
        )
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('auth.login'))
    return render_template('register.html', title='Register', form=form)


@blueprint.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
