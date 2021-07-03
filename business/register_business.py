#coding=utf-8
from handle.register_handle import RegisterHandle
class RregisterBusiness(object):
    def __init__(self):
        self.register_h=RegisterHandle()
#调用handle层的具体方法执行操作，输入用户名，密码等
    def login(self,email,name,password,code):
        self.register_h.send_user_email(email)
        if self.register_h.get_uesr_text("请输入有效的电子邮件地址"):
            print("检验成功")
            return True
        elif self.register_h.send_user_name(name):
            print("用户名校验成功")
            return True
        elif self.register_h.send_user_password(password):
            return True
        elif self.send_user_code(code):
            return True
