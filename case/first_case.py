# coding=utf-8
import sys
import os

from log.user_log import UserLog


from business.register_business import RregisterBusiness
from selenium import webdriver
import unittest
import HTMLTestRunner
import time
basepath = os.getcwd()



class FirstCase(unittest.TestCase):
    # 前置函数，打开浏览器，访问测试地址
    @classmethod
    def setUpClass(cls):
        cls.log = UserLog()
        cls.logger = cls.log.get_log()
        cls.file_name = basepath+"\\Image\\image2222.png"
        cls.driver = webdriver.Chrome()
        cls.driver.get('http://www.5itest.cn/register')

        cls.driver.maximize_window()
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.5itest.cn/register')
        self.driver.maximize_window()
        self.login = RregisterBusiness(self.driver)
        # 邮箱、用户名、密码、验证码、错误信息定位元素、错误提示信息
        # 后置函数，关闭浏览器

    def tearDown(self):
        time.sleep(2)
        # if sys.exc_info()[0]:
        for method_name, error in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                file_path = os.path.join(os.getcwd() + "/report/" + case_name + ".png")
                self.driver.save_screenshot(file_path)
        self.driver.close()
    def test_login_email_error(self):
        email_error = self.login.login_email_error('1314@qq.com','user1111@qq.com','111111','23123')
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
        # 测试报告路径
        file_path = os.path.join(os.getcwd() + "\\report\\" + "first_case.html")
        # 以读写模式打开测试报告
        f = open(file_path, 'wb')
        #添加用例到测试套件
        suite = unittest.TestSuite()
        suite.addTest(FirstCase('test_login_success'))
        suite.addTest(FirstCase('test_login_code_error'))
        suite.addTest(FirstCase('test_login_email_error'))
        suite.addTest(FirstCase('test_login_username_error'))
        # unittest.TextTestRunner().run(suite)
        # suite = unittest.TestLoader().loadTestsFromTestCase(FirstCase)
        # Htmlrunner驱动测试套件执行生成报告
        runner = HTMLTestRunner.HTMLTestRunner(stream=f, title="This is first123 report", description=u"这个是我们第一次测试报告",verbosity=2)
        runner.run(suite)