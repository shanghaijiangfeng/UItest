#coding=utf-8
from page.register_page import RegisterPage
class RegisterHandle:
    def __init__(self):
        self.register_p=RegisterPage()
    #输入邮箱
    def send_user_email(self,email):
        self.register_p.get_email_element().send_keys(email)

    #输入用户名
    def send_user_name(self):
        pass
    #输入密码
    def send_user_password(self):
        pass
    #输入验证码
    def send_user_code(self):
        pass
    #获取页面文字信息,判断错误提示是哪个
    def get_uesr_text(self,userinfo):
        pass
