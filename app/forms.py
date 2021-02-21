from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import SubmitField


class UploadForm(FlaskForm):
    file = FileField('Upload File', render_kw={"class": "dropzone"})
    submit = SubmitField('Submit')