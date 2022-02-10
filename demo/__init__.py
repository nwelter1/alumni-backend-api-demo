from flask import Flask
from config import Config
from .api.routes import api

app = Flask(__name__)
app.register_blueprint(api)

app.config.from_object(Config)