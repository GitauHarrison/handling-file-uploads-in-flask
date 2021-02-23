from app import app
from flask import render_template, url_for, request, redirect, abort
from app.forms import UploadForm
import os
import imghdr
from werkzeug.utils import secure_filename


# new update
def validate_image(stream):
    header = stream.read(512)
    stream.seek(0)
    format = imghdr.what(None, header)
    if not format:
        return None
    return '.' + (format if format != 'jpeg' else 'jpg')


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = UploadForm()
    if request.method == 'POST':
        uploaded_file = request.files['file']
        filename = secure_filename(uploaded_file.filename)
        if filename != '':
            file_ext = os.path.splitext(filename)[1]
            # updated
            if file_ext not in app.config['UPLOAD_EXTENSIONS'] or \
                    file_ext != validate_image(uploaded_file.stream):
                # end of update
                abort(400)
            uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], filename))  # <--------- new update
        return redirect(url_for('index'))
    return render_template('index.html', title='Home', form=form)
