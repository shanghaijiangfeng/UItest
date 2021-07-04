# coding=utf-8
import sys
import os

basepath = os.getcwd()
sys.path.append(basepath)
from business.register_business import RregisterBusiness
from selenium import webdriver
import unittest
import HTMLTestRunner



class FirstCase(unittest.TestCase):
    # 前置函数，打开浏览器，访问测试地址
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.5itest.cn/register')
        self.driver.maximize_window()
        self.login = RregisterBusiness(self.driver)
        # 邮箱、用户名、密码、验证码、错误信息定位元素、错误提示信息
        # 后置函数，关闭浏览器

    def tearDown(self):
        self.driver.close()
    def test_login_email_error(self):
        email_error = self.login.login_email_error('1314@qq.com','user1111@qq.com','111111')
        return self.assertFalse(email_error,"测试失败")

    def test_login_username_error(self):
        username_error = self.login.login_name_error('12123@qq.com', 't1', '111111', '1231')
        self.assertTrue(username_error,"通过")

    def test_login_code_error(self):
        code_error = self.login.login_code_error('11121@qq.com', 'ss22212', '111111', '1231')
        self.assertFalse(code_error,"通过")

    def test_login_password_error(self):
        password_error = self.login.login_password_error('11311@qq.com', 'ss23222', '111111', '1231')
        self.assertFalse(password_error,"通过")

    def test_login_success(self):
        success = self.login.user_base('12221@qq.com', '2321', '111111', '1231')
        self.assertFalse(success,"通过")
        # self.assert


'''
def main():
        first = FirstCase()
        first.test_login_email_error()
        first.test_login_password_error()
        first.test_login_username_error()

        first.test_login_code_error()


        first.test_login_success()
'''
if __name__ == '__main__':
        #

        file_path = os.path.join(os.getcwd() + "\\report\\" + "first_case.html")
        print("sss"+file_path)
        f = open(file_path, 'wb')
        suite = unittest.TestSuite()
        suite.addTest(FirstCase('test_login_success'))
        # suite.addTest(FirstCase('test_login_code_error'))
        suite.addTest(FirstCase('test_login_email_error'))
        suite.addTest(FirstCase('test_login_username_error'))
        # unittest.TextTestRunner().run(suite)
        # suite = unittest.TestLoader().loadTestsFromTestCase(FirstCase)
        runner = HTMLTestRunner.HTMLTestRunner(stream=f, title="This is first123 report", description=u"这个是我们第一次测试报告",verbosity=2)
        runner.run(suite)