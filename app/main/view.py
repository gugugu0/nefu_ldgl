#coding:utf-8
from flask import render_template, request, current_app, redirect,\
    url_for
from . import main
from ..models import Vuln#, PlatInfo
from .. import db

@main.route('/index')
def index():
    # Vuln.add_view(db)
    #bloginfo = PlatInfo.query.first()
    #title = bloginfo.title
    #gongao =
    return render_template('index.html', endpoint='.index')