# -*- coding: utf-8 -*-
import time
from selenium import webdriver

def loginout(self):
    browser = self.browser
    time.sleep(2)
    browser.find_element_by_class_name("log-dd-trigger").click()
    time.sleep(1)
    browser.find_element_by_id("logout").click()
    time.sleep(1)
    print("----注销成功-----")
