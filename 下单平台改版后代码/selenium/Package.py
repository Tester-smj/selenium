#test
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0

def element(browser,arg):
    index=browser.find_element_by_link_text(u'首页')
    fromdate=browser.find_element_by_id('fromDate').send_keys("2016-12-29 21:31:20")
    #wait = WebDriverWait(browser, 10)
    #elements = wait.until(EC.element_to_be_clickable((By.ID,'fromDate')))
    jobtype=browser.find_element_by_id('jobType').click()
    #chexing=browser.find_element_by_xpath(arg["//option[@value='0']"])
    browser.find_element_by_id("fromCity").click()
    fromcity=browser.find_element_by_id('fromCity').send_keys(u"深圳")
    fromaddr=browser.find_element_by_id('fromAddr').send_keys(u"宝安区深圳北站")
    #cityselecte=browser.find_element_by_xpath(arg["//div[@id='tangram-suggestion--TANGRAM__3-main']/div[2]/table/tbody/tr/td/i"])
    #return index,fromdate,fromaddr,fromcity,jobtype,chexing,cityselecte