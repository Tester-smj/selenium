# -*- coding: utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

def myorder(self):
    time.sleep(1.5)
    browser = self.browser
    a=browser.find_element_by_class_name("log-dd-trigger")
    b=browser.find_element_by_xpath("//*[@id='headerDiv']/div/ul[2]/li/ul/li[2]/a")
    time.sleep(1)
    ActionChains(browser).move_to_element(a).click(b).perform()
    time.sleep(1.5)
    #browser.find_element_by_xpath("//*[@id='headerDiv']/div/ul[2]/li/ul/li[2]/a").click()
    #browser.find_element_by_link_text("待安排").click()
    #time.sleep(1)
    #browser.find_element_by_xpath("//*[@id='statustr'']/td[7]/p/a[1]").click()
    #browser.find_element_by_class_name("pay").click()
    #time.sleep(1)
    #browser.find_element_by_id("paybtn").click()
    #time.sleep(1)
    print("----我的订单支付成功-----")
