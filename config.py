#coding:utf-8
'''
配置文件
'''
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@219.217.199.209:3306/test2?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    VULNERABILITY_PER_PAGE = 10
    SECRET_KEY = 'MySecretKey996'
    # WTF_CSRF_SECRET_KEY = str(os.urandom(12))

    @staticmethod
    def init_app(app):
        pass
