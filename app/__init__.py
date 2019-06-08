#coding:utf-8
from flask import Flask, url_for, request, redirect, render_template
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf.csrf import CsrfProtect


# app = Flask(__name__)
# app.config.from_object(Config)
# db = SQLAlchemy(app)
#
# from app import models


db = SQLAlchemy()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    Config.init_app(app)
    CsrfProtect(app)

    db.init_app(app)

    login_manager.init_app(app)

    # 蓝图注册
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)


    return app