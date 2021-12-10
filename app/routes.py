from app import app
from flask import render_template
from app.forms import UserForm


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = UserForm()    
    return render_template(
                           'index.html',
                           form=form,
                           title='User Form',
                           )
