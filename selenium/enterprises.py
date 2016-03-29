#-*- coding:utf-8 -*-
import httpreques
from PIL import Image
import pytesseract
import ImageEnhance
import ImageFilter
import sys
from selenium import webdriver
from pytesser import *
import  time, re
import picture
from selenium.webdriver.common.action_chains import ActionChains

def enterprises(self):
    u"""企业加入"""
    browser = self.browser
    #picture.getverify1(self)
    browser.find_element_by_link_text("企业加入").click()
    time.sleep(2)
    #code=browser.find_element_by_id("randImg")
    right=browser.find_element_by_id("randImg")
    #ActionChains(browser).context_click(right).perform()
    #code=browser.find_element_by_id("randImg").send_keys(KeyboardInterrupt.V)
    time.sleep(2)
    browser.find_element_by_id("enterpriseName").send_keys(u"测试公司")
    browser.find_element_by_id("enterpriseAddress").send_keys(u"测试地址")
    browser.find_element_by_id("enterprisePhone").send_keys("07558888888")
    browser.find_element_by_id("enterpriseContacts").send_keys(u"测试")
    browser.find_element_by_id("verificationCode").send_keys(picture.getverify1('2.jpg'))
    browser.find_element_by_id("submt").click()
    time.sleep(2)
    print(u"-----企业加入成功-----")