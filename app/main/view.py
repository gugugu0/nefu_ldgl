#coding:utf-8
from flask import render_template, request, current_app, redirect,\
    url_for
from . import main
from ..models import Vuln, PlatformInfo
from .. import db

@main.route('/index')
def index():
    platformInfo = PlatformInfo.query.first()
    about = platformInfo.about
    help = platformInfo.help
    title = platformInfo.title
    return render_template('index.html', help=help, about=about, title=title)

@main.route('/')
def index0():
    return redirect(url_for('main.index'))


@main.route('/about')
def about():
        return render_template('about.html')


@main.route('/help')
def about():
        return render_template('help.html')
