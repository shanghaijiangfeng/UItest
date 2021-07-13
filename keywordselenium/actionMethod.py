#coding=utf-8
from selenium import webdriver
from base.find_element import FindElement
import time
class ActionMethod():
    #打开浏览器
    #driver=webdriver.Chrome()
    def open_browser(self,browser):
        if browser == 'chrome':
            self.driver = webdriver.Chrome()
        elif browser == 'firefox':
            self.driver = webdriver.Firefox()
        else:
            self.driver = webdriver.Edge()
        
    #输入地址
    def get_url(self,url):
        self.driver.get(url)
    
    #定位元素
    def get_element(self,key):
        find_element = FindElement(self.driver)
        element = find_element.get_element(key)
        return element
    
    #输入元素
    def element_send_keys(self,value,key):
        element = self.get_element(key)
        element.send_keys(value)
    
    #点击元素
    def click_element(self,key):
        self.get_element(key).click()
    
    #等待
    def sleep_time(self):
        time.sleep(3)
    
    #关闭浏览器
    def close_browser(self):
        self.driver.close()
    
    #获取title
    def get_title(self):
        title = self.driver.title
        return title
    # 获取预期结果值
    def get_except_result_value(self, data):
        return data.split('=')

    def run_method(self, method, send_value='', handle_value=''):
        method_value = getattr(action_method, method)
        if send_value == '' and handle_value != '':
            result = method_value(handle_value)
        elif send_value == '' and handle_value == '':
            result = method_value()
        elif send_value != '' and handle_value == '':
            result = method_value(send_value)
        else:
            result = method_value(send_value, handle_value)
        return result

action_method=ActionMethod()
if __name__ == '__main__':
    #action_method.open_browser('chrome')
    asss = action_method.get_except_result_value('sada=asdasd')
    print(asss)