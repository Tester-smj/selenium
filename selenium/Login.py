# -*- coding: utf-8 -*-
import time
from selenium import webdriver

def login(self):
    self.browser = webdriver.Chrome(r"c:/python27/chromedriver.exe")
    self.browser.implicitly_wait(10)
    self.base_url = "http://www.senbaba.cn/"
    self.verificationErrors = []
    self.accept_next_alert = True
    self.browser.get(self.base_url)
    self.browser.maximize_window()
    self.browser.find_element_by_link_text("登录").click()
    time.sleep(2)
    #切换到弹出框
    change=self.browser.switch_to_frame("layui-layer-iframe1")
    self.browser.find_element_by_name("username").clear()
    self.browser.find_element_by_name("username").send_keys(u"18707148477")
    self.browser.find_element_by_name("password").clear()
    self.browser.find_element_by_name("password").send_keys(u"123456")
    self.browser.find_element_by_id("loginBtn").click()
    a=self.browser.find_element_by_class_name("userName").text
    print(a)
    print(u"-------登录成功！--------")

