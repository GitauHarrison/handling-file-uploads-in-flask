import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    # Form
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    # Database
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', '').replace(
        'postgres://', 'postgresql://') or\
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # File Upload
    UPLOAD_PATH = os.environ.get('UPLOAD_PATH') or 'app/static/uploads'

    # Heroku logs
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')
