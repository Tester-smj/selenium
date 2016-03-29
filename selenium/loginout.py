# -*- coding: utf-8 -*-
import time
from selenium import webdriver

def loginout(self):
    time.sleep(1.5)
    browser = self.browser
    browser.find_element_by_class_name("log-dd-trigger").click()
    time.sleep(2)
    browser.find_element_by_id("logout").click()
    time.sleep(1.5)
    print("----注销成功-----")
