from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config  # <----------- new

app = Flask(__name__)
app.config.from_object(Config)  # <----------- new
bootstrap = Bootstrap(app)

from app import routes, errors
