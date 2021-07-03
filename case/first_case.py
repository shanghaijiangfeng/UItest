#coding=utf-8
import sys
import os
basepath=os.getcwd()
sys.path.append(basepath)
from business.register_business import RregisterBusiness
from selenium import webdriver

class FirstCase(object):
    def __init__(self):
        driver = webdriver.Chrome()
        driver.get('http://www.5itest.cn/register')
        driver.maximize_window()
        self.login=RregisterBusiness(driver)
        # 邮箱、用户名、密码、验证码、错误信息定位元素、错误提示信息

    def test_login_email_error(self):
        email_error = self.login.login_email_error('1314@qq.com', 'user1111@qq.com', '111111','1231')
        return self.assertFalse(email_error, "测试失败")

    def test_login_username_error(self):
        username_error = self.login.login_name_error('12123@qq.com', 't1', '111111','1231')
        self.assertTrue(username_error)

    def test_login_code_error(self):
        code_error = self.login.login_name_error('11121@qq.com', 'ss22212', '111111','1231')
        self.assertFalse(code_error)

    def test_login_password_error(self):
        password_error = self.login.login_name_error('11311@qq.com', 'ss23222', '111111','1231')
        self.assertFalse(password_error)

    def test_login_success(self):
        success = self.login.user_base('12221@qq.com', '2321', '111111', '1231')
        self.assertFalse(success)
        # self.assert

def main():
        first = FirstCase()
        first.test_login_code_error()
        first.test_login_email_error()
        first.test_login_password_error()
        first.test_login_username_error()
        first.test_login_success()

if __name__ == '__main__':
        main()




