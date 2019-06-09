#coding:utf-8
from app import db, create_app
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
from flask_migrate import upgrade
from app.models import User, Vuln, PlatformInfo, Announcement


app = create_app()
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db',MigrateCommand)

# Jinja2 全局环境变量
#app.jinja_env.globals['xxx'] = xxx

# 上下文函数
def make_shell_context():
    return dict(db=db, User=User, Vuln=Vuln, PlatformInfo=PlatformInfo, Announcement=Announcement)

manager.add_command("shell", Shell(make_context=make_shell_context))

# 部署函数
@manager.command
def deploy(deploy_type):
    from flask_migrate import upgrade
    from app.models import User, Vuln, PlatformInfo, Announcement

    # 将数据库升级到最新版本
    upgrade()

    if deploy_type == 'up':
        try:
            PlatformInfo.insert_platform_info()
            Vuln.insert_ont_test()
            User.insert_admin('master@nefu.edu.cn', 'chenye', 'root*chenye', 'NSI')
        except:
            pass





if __name__ == '__main__':
    manager.run()