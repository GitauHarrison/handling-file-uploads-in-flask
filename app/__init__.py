from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__)
boostrap = Bootstrap(app)

from app import routes, errors
