# 这个文件是自己写的认证组件
from flask import request,session,redirect

class Auth(object):
    def __init__(self,app = None):
        self.app = app
        if app:
            self.init_app(app)

    def init_app(self,app):
        app.auth_manager = self     #将Auth的对象封装到app,在视图中可以通过current_app取出当前app,然后在执行.login方法就可以把写入到session
        self.app = app
        app.before_request(self.check_login)    #请求过来的时候没有到达视图函数的时候进行验证
        app.context_processor(self.context_processor)    #将用户当前用户的用户名放入到应用上下文中

    def check_login(self):
        '''
        检查用户是否已经登录
        :return:
        '''
        if request.path == '/login':
            return

        user = session.get('user')
        if not user:
            return redirect('/login')

    def context_processor(self):
        '''
        从cookie中获取cookie的值,为了在用户登录成功之后访问其他页面时可以在页面右上角显示当前用户的用户名
        :return:
        '''
        user = session.get('user')
        return dict(current_user=user)

    def login(self,data):
        '''
        将用户登录信息,放入session
        :param data:
        :return:
        '''
        session['user'] = data

    def logout(self):
        '''
        用户注销登录时,删除session
        :return:
        '''
        del session['user']








