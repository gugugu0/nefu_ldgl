from app import db #, create_app
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
from flask_migrate import upgrade

# 上下文函数
def make_shell_context():
    return dict(db=db)


app = create_app()
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('ab',MigrateCommand)

manager.add_command("shell", Shell(make_context=make_shell_context))

# 部署函数
@manager.command
def deploy(deploy_type):
    from flask_migrate import upgrade
    from app.models import Vuln

    upgrade()

    if deploy_type == 'test':
        Vuln.insert_one_test()



if __name__ == '__main__':
    manager.run()