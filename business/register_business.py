#coding=utf-8
from handle.register_handle import RegisterHandle
class RregisterBusiness(object):
    def __init__(self):
        self.register=RegisterHandle()
#调用handle层的具体方法执行操作，输入用户名，密码等
    def login(self):
        self.register.send_user_email()