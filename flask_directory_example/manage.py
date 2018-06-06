from flask_directory_example import create_app,db
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from flask_directory_example.models import Users #注意要把models中的表名引入到manage.py中
'''
1.数据库迁移的时候，如果manage.py里没有导入Users，模型对应表结构，迁移脚本拿不到模型，就会删除数据库里对应的表。这地方掉坑里好久。
2.在创建数据库的时候也需要导入模型Users
'''



app = create_app()
manager = Manager(app)



Migrate(app, db)
"""
# 数据库迁移命名
    python manage.py db init
    python manage.py db migrate # makemigrations
    python manage.py db upgrade # migrate
"""
manager.add_command('db', MigrateCommand)




@manager.command
def custom(arg):
    """
    自定义命令
    python manage.py custom 123
    :param arg:
    :return:
    """
    print(arg)


@manager.option('-n', '--name', dest='name')
@manager.option('-u', '--url', dest='url')
def cmd(name, url):
    """
    自定义命令
    执行： python manage.py  cmd -n wupeiqi -u http://www.oldboyedu.com
    执行： python manage.py  cmd --name wupeiqi --url http://www.oldboyedu.com
    :param name:
    :param url:
    :return:
    """
    print(name, url)


if __name__ == '__main__':
    # app.run()
    manager.run()