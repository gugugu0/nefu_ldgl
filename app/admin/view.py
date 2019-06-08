#coding:utf-8

from flask import render_template, redirect, flash, \
    url_for, request, current_app, jsonify
import json
from flask_login import  login_required, current_user
from . import admin
from ..models import Vuln, User, PlatformInfo, Announcement
from .forms import SubmitVulnsForm


@admin.route('/admin')
@login_required
def manager():
    return render_template('admin/admin.html')