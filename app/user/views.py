from flask import request, render_template, flash, redirect, url_for, abort
from flask_login import current_user, login_required
from app.user import user
from app.extensions import db, login_manager
from app.user.models import User, Post
from app.user.forms import DestinationForm


@user.route('/')
def index():
    posts = Post.query.all() or []
    return render_template('index.html', posts=posts)


@user.route('/user/<username>', methods=['GET', 'POST'])
@login_required
def planner(username):
    if current_user.username != username:
        return redirect(url_for('auth.login'))
    user = User.query.filter_by(username=current_user.username).first()
    posts = Post.query.filter_by(user_id=user.id) or []

    form = DestinationForm(meta={'csrf': False})

    if request.method == 'POST' and form.validate():
        new_destination = Post(
            city=form.city.data,
            country=form.country.data,
            description=form.description.data,
            user_id=current_user.id
        )
        db.session.add(new_destination)
        db.session.commit()
    else:
        for field, errors in form.errors.items():
            flash(f"[{field}] {''.join(errors)}")
    return render_template('planner.html', user=user, posts=posts, form=form)
