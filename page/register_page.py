#coding=utf-8
from base.find_element import FindElement
class RegisterPage():
    def __init__(self,driver):
        self.fd=FindElement(driver)
    #page层从配置文件取出元素定位方式及元素位置
    #获取元素
    def get_email_element(self):
        return self.fd.get_element("user_email")
    #获取用户名
    def get_email_element(self):
        return self.fd.get_element("user_name")
    #获取密码定位方式及元素位置
    def get_password_element(self):
        return self.fd.get_element("user_password")
        # 获取验证码位置

    def get_code_element(self):
        return self.fd.get_element("code_text")
    #获取错误提示语
    def get_email_error_element(self):
        return self.fd.get_element("user_email_error")
    def get_password_error_element(self):
        return self.fd.get_element("password_error")
    def get_name_error_element(self):
        return self.fd.get_element("user_name_error")
    def get_code_text_error_element(self):
        return self.fd.get_element("user_email_error")

    #点击注册按钮，点击事件
    def get_button_element(self):
        return self.fd.get_element("register_button")