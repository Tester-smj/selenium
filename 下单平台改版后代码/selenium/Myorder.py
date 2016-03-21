# -*- coding: utf-8 -*-
import time
from selenium import webdriver

def myorder(self):
    browser = self.browser
    time.sleep(2)
    browser.find_element_by_class_name("log-dd-trigger").click()
    time.sleep(1)
    browser.find_element_by_link_text(u"我的订单").click()
    time.sleep(1)
    browser.find_element_by_link_text("待安排").click()
    time.sleep(1)
    print("----我的订单-----")
