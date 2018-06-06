from flask import blueprints, render_template,session,request,current_app,redirect
from flask_directory_example import db
from .. import models

ac = blueprints.Blueprint('ac', __name__)




@ac.route('/login', methods=['GET', 'POST'])
def login():
    if request.method=='GET':
        return render_template('login.html')
    else:
        user = request.form.get('user')
        pwd = request.form.get('pwd')

        obj = db.session.query(models.Users).filter(models.Users.name==user,models.Users.pwd==pwd).first()
        db.session.remove() #在请求结束时删除数据库会话
        if not obj:
            return render_template('login.html')
        current_app.auth_manage.login(user) #用户验证成功设置session
        return redirect('/index')

@ac.route('/logout')
def logout():
    current_app.auth_manage.logout()
    return redirect('/login')