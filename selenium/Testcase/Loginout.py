# -*- coding: utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

def loginout(self):
    time.sleep(1.5)
    browser = self.browser
    a=browser.find_element_by_class_name("userIcon")
    b=browser.find_element_by_id("logout")
    action=ActionChains(browser)
    action.move_to_element(a)
    time.sleep(2)
    action.click(b).perform()
    time.sleep(2)
    print("----注销成功-----")

#menu = driver.find_element_by_css_selector(".nav")
#hidden_submenu = driver.find_element_by_css_selector(".nav #submenu1")

#actions = ActionChains(driver)
#actions.move_to_element(menu)
#actions.click(hidden_submenu)
#actions.perform()
