from app import app, db
from flask import render_template, flash, redirect, url_for
from app.forms import UserForm
from app.models import User
from werkzeug.utils import secure_filename
import os


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    users = User.query.all()
    form = UserForm()
    if form.validate_on_submit():
        admin = User(
            username=form.username.data,
            email=form.email.data,
            about_me=form.about_me.data
        )
        uploaded_file = form.avatar.data
        filename = secure_filename(uploaded_file.filename)
        avatar_path = os.path.join(app.config['UPLOAD_PATH'], filename)
        uploaded_file.save(avatar_path)
        admin.avatar = avatar_path
        path_list = admin.avatar.split('/')[1:]
        new_path = '/'.join(path_list)
        admin.avatar = new_path
        db.session.add(admin)
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('index'))
    return render_template(
                           'index.html',
                           form=form,
                           title='User Form',
                           users=users
                           )
