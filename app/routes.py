from app import app
from flask import render_template, url_for, request, redirect
from app.forms import UploadForm


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = UploadForm()
    return render_template('index.html', title='Home', form=form)
