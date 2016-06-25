# -*- coding: utf-8 -*-
import time
from selenium import webdriver
values=["18707148477","15323746097"]
# number = int(raw_input("raw_input: "))
# print(number)
def login(self):
    # number = int(raw_input("raw_input: "))
    # print(number)
    self.browser = webdriver.Chrome(r"c:/python27/chromedriver.exe")
    self.browser.implicitly_wait(10)
    self.base_url = "http://www.senbaba.cn"
    self.verificationErrors = []
    self.accept_next_alert = True
    self.browser.get(self.base_url)
    self.browser.maximize_window()
    self.browser.find_element_by_link_text("登录").click()
    time.sleep(2)
    #切换到弹出框
    change=self.browser.switch_to_frame("layui-layer-iframe1")
    # for search in values:
    self.browser.find_element_by_name("username").clear()
    self.browser.find_element_by_name("username").send_keys(u"15323746097")
    self.browser.find_element_by_name("password").clear()
    self.browser.find_element_by_name("password").send_keys(u"123456")
    self.browser.find_element_by_id("loginBtn").click()
    a=self.browser.find_element_by_class_name("userName").text
    if a==u'您好!石梦杰':
        print(u"-------登录成功！--------")
    else:
        print(u"---登录失败---")
    time.sleep(1)

