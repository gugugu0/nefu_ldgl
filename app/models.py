#coding:utf-8
from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
import datetime

class Vuln(db.Model):
    __tablename__ = 'vulns'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), index=True)
    describe = db.Column(db.Text, nullable=True)
    fix_describe = db.Column(db.Text, nullable=True)
    rank = db.Column(db.Integer)
    type = db.Column(db.Integer)
    publish_date = db.Column(db.Date, index=True, default=datetime.datetime.now())
    fix_date = db.Column(db.Date, index=True, default=datetime.datetime.now())
    organization = db.Column(db.String(64), default=u'unknown')
    status = db.Column(db.Integer, default=0, index=True)
    annex = db.Column(db.Text) # 附件名



    @staticmethod
    def insert_ont_test():
        vuln = Vuln(title=u'test vuln 1', describe=u'this is a test vuln',\
                    fix_date=datetime.datetime.now(),publish_date=datetime.datetime.now(), \
                    rank=1, type=1, organization='NSI', status=0, annex='fujian.doc')
        db.session.add(vuln)
        db.session.commit()


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    organization = db.Column(db.String(64), default=u'unknown')
    priority = db.Column(db.Integer, default=1)

    @staticmethod
    def insert_admin(email, username, password, organization):
        user = User(email=email, username=username, password=password, priority=0, organization=organization)
        db.session.add(user)
        db.session.commit()

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)

class PlatformInfo(db.Model):
    __tablename__ = 'platform_info'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))
    about = db.Column(db.Text)
    help = db.Column(db.Text)

    @staticmethod
    def insert_platform_info(about=u'None', help=u'None', title=u'NEFU漏洞管理平台'):
        info = PlatformInfo(about=about, help=help, title=title)
        db.session.add(info)
        db.session.commit()

class Announcement(db.Model):
    __tablename__ = 'announcements'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), index=True)
    announce = db.Column(db.Text)
    date = db.Column(db.Date, index=True, default=datetime.datetime.now())
    rank = db.Column(db.Integer, index=True, default=4)

    @staticmethod
    def insert_announce():
        info = PlatformInfo(title=u'None', announce=u'None', date=datetime.datetime.now())
        db.session.add(info)
        db.session.commit()