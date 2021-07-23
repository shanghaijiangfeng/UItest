#coding=utf-8
import random

import pymysql
import requests
from selenium import webdriver
from base.find_element import FindElement
import time
class ActionMethod():
    #打开浏览器
    #driver=webdriver.Chrome()
    def open_browser(self,browser):
        if browser == 'chrome':
            self.driver = webdriver.Chrome()
            self.driver.maximize_window()
        elif browser == 'firefox':
            self.driver = webdriver.Firefox()
            self.driver.maximize_window()
        else:
            self.driver = webdriver.Edge()
            self.driver.maximize_window()
        
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
    #获取元素文本信息操作
    def Ttext_element(self,key):
        text=self.get_element(key).text
        return text


    #js按钮点击
    def jsclick_element(self,key):
        el=self.get_element(key)
        self.driver.execute_script("arguments[0].click();", el)


    def Textassert(self):
        return self.Ttext_element()
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

    # 获取当前url
    def get_urltitle(self):
        currentPageUrl = self.driver.current_url
        return currentPageUrl

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
    #生成随机手机号
    def random_phone_number(self):
        headList = ["110", "112", "113", "115", "114", "120", "121", "123"]
        return (random.choice(headList) + "".join(random.choice("0123456789") for i in range(8)))
    #查询验证码
    def sqlselect_test_wt_uac(self):
        conn = pymysql.connect(host='192.168.95.18',port=3306,user='root',password='123456',database='wt_uac',charset='utf8')

        # 得到一个可以执行SQL语句的光标对象
        cursor = conn.cursor()  # 执行完毕返回的结果集默认以元组显示
        # 得到一个可以执行SQL语句并且将结果作为字典返回的游标
        # cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

        # 定义要执行的SQL语句
        sql = """SELECT digit_code FROM uac_sms_record  ORDER BY created_time desc LIMIT 1  """

        # 执行SQL语句
        cursor.execute(sql)
        code=cursor.fetchall()
        cd=code[0]
        cd=str(cd)


        # 关闭光标对象
        cursor.close()

        # 关闭数据库连接
        conn.close()
        return cd

action_method=ActionMethod()
if __name__ == '__main__':
    #action_method.open_browser('chrome')
    asss = action_method.random_phone_number()
    print(asss)