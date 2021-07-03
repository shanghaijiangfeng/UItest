# coding=utf-8
import sys
import os
basepath=os.getcwd()
sys.path.append(basepath)
from selenium import webdriver
import time
import random
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from PIL import Image

driver = webdriver.Chrome()

driver.maximize_window()
driver.get("http://www.5itest.cn/register")
time.sleep(3)
print(EC.title_contains("注册"))


"判断元素是否可见，即元素等待方式"
element = driver.find_elements_by_class_name("controls")
"by方法包内，显示等待，传入定位方式及元素"
locator = (By.CLASS_NAME, "controls")
"传入dirver，等待时间，以及元素位置"
WebDriverWait(driver,1).until(EC.visibility_of_element_located(locator))

"生成随机字符串,random返回的是list，所以要join一下，转成字符串"
user_email = ''.join(random.sample('1234567890abcdefg',8))+"@163.com"
print(user_email)

email_name = driver.find_element_by_id("register_email")
email_name.send_keys("jiangfeng_94@163.com")
"selenium保存图片"
driver.save_screenshot(basepath+"\\Image\\image.png")
"获取验证码元素位置"
code_element = driver.find_element_by_id("getcode_num")
print(code_element.location)#{"x":123,"y":345}
"通过元素的左上角坐标，算出其他几个坐标点"
left = code_element.location['x']
top = code_element.location['y']
right = code_element.size['width']+left
height = code_element.size['height']+top
im = Image.open(basepath+"\\Image\\image.png")
"根据坐标裁剪出验证码图片"
img = im.crop((left,top,right,height))
"保存验证码图片"
img.save(basepath+"\\Image\\image2.png")




"获取此时输入框的值"
print(email_name.get_attribute("value"))

"先查找父节点，查找出父节点后再查出父节点下的子节点"
user_name_element_node = driver.find_elements_by_class_name("controls")[1]
"子节点获取元素是list"
user_element = user_name_element_node.find_element_by_class_name("form-control")
user_element.send_keys("saa1231saf")

driver.find_element_by_name("password").send_keys("sahfkhj123123")
driver.find_element_by_xpath("//*[@id='captcha_code']").send_keys("111111")
driver.close()
