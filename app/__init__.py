from flask import Flask, url_for, request, redirect, render_template
from config import Config
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

from app import models
# def create_app():
#     app = Flask(__name__)
#     app.config.from_object(Config)
#
#     Config.init_app(app)
#
#     db.init_app(app)
#
#     return app