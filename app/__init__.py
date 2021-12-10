from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

boostrap = Bootstrap(app)

from app import routes, errors
