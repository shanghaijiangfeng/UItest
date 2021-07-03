#coding=utf-8
from business.register_business import RregisterBusiness
class FirstCase(object):
    def __init__(self, driver):
        self.login=RregisterBusiness(driver)
    def test_login_email_error(self):
        self.login.login_email_error()
        pass
    def test_login_username_error(self):
        pass
    def test_login_code_error(self):
        pass
    def test_login_succes(self):
        pass