# coding=utf-8
from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.5itest.cn/register")
time.sleep(3)
print(EC.title_contains("注册"))
driver.find_element_by_id("register_email").send_keys("jiangfeng_94@163.com")

"先查找父节点，查找出父节点后再查出父节点下的子节点"
user_name_element_node = driver.find_elements_by_class_name("controls")[1]
"子节点获取元素是list"
user_element = user_name_element_node.find_element_by_class_name("form-control")
user_element.send_keys("saa1231saf")

driver.find_element_by_name("password").send_keys("sahfkhj123123")
driver.find_element_by_xpath("//*[@id='captcha_code']").send_keys("111111")
