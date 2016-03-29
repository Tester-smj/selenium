# -*- coding: utf-8 -*-
import time
from selenium import webdriver

def myorder(self):
    time.sleep(1.5)
    browser = self.browser
    browser.find_element_by_class_name("log-dd-trigger").click()
    time.sleep(2)
    browser.find_element_by_link_text("我的订单").click()
    time.sleep(1.5)
    #browser.find_element_by_link_text("待安排").click()
    time.sleep(1)
    #browser.find_element_by_xpath("//*[@id='statustr'']/td[7]/p/a[1]").click()
    browser.find_element_by_class_name("pay").click()
    time.sleep(1)
    browser.find_element_by_id("paybtn").click()
    time.sleep(1)
    print("----我的订单支付成功-----")
