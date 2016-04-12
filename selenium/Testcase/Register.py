# -*- coding: utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

def regist(self):
    browser = self.browser
    a=browser.find_element_by_class_name("log-dd-trigger")
    b=browser.find_element_by_id("logout")
    ActionChains(browser).move_to_element(a).click(b).perform()
    time.sleep(1.5)
    self.browser.find_element_by_link_text("注册").click()
    time.sleep(2)
    #切换到弹出框
    change=self.browser.switch_to_frame("layui-layer-iframe1")
    time.sleep(1)
    self.browser.find_element_by_name("username").clear()
    self.browser.find_element_by_name("username").send_keys(u"张二宝")
    self.browser.find_element_by_id("phone").send_keys("18707148477")
    self.browser.find_element_by_id("reglister_input").send_keys("1245")
    self.browser.find_element_by_name("password").clear()
    self.browser.find_element_by_name("password").send_keys("123456")
    self.browser.find_element_by_id("pwdcomfirm").send_keys("123456")
    self.browser.find_element_by_xpath("/html/body/div/ul/li[7]/div/div/div/div/ins").click()
    self.browser.find_element_by_id("reglister").click()
    time.sleep(2)
    #a=self.browser.find_element_by_class_name("userName").text
    #print(a)
    print(u"-------登录成功！--------")

