# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
import HTMLTestRunner

class Senbaba(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(r"c:/python27/chromedriver.exe")
        self.browser.implicitly_wait(30)
        self.base_url = "http://www.senbaba.cn/"
        self.verificationErrors = []
        self.accept_next_alert = True
        self.browser.get(self.base_url)
        self.browser.maximize_window()
        self.browser.find_element_by_link_text("登录").click()
        self.browser.find_element_by_name("username").send_keys(u"18707148477")
        time.sleep(1)
        self.browser.find_element_by_id("pwd").send_keys(u"123456")
        time.sleep(1)
        self.browser.find_element_by_class_name("loginBtn").click()
        time.sleep(2)
    
    def test_jiesong(self):
        u"""接送类型下单"""
        browser = self.browser
        browser.find_element_by_link_text("首页").click()
        time.sleep(2)
        browser.find_element_by_id("fromDate").send_keys(u"2016-12-29 21:31:20")
        time.sleep(2)
        browser.find_element_by_id("jobType").click()
        time.sleep(1)
        browser.find_element_by_xpath("//option[@value='0']").click()
        time.sleep(1)
        browser.find_element_by_id("fromCity").send_keys(u"深圳")
        time.sleep(2)
        browser.find_element_by_id("fromAddr").send_keys(u"宝安区深圳北站")
        time.sleep(2)
        browser.find_element_by_xpath("//div[@id='tangram-suggestion--TANGRAM__3-main']/div[2]/table/tbody/tr/td/i").click()
        time.sleep(1)
        browser.find_element_by_id("bookBtn").click()
        time.sleep(1)
        browser.find_element_by_id("carTypeSel").click()
        time.sleep(1)
        browser.find_element_by_xpath("//select[@id='carTypeSel']/option[4]").click()
        time.sleep(1)
        browser.find_element_by_id("endDates").send_keys(u"2016-12-30 21:31:20")
        time.sleep(1)
        #因为时间控件无法自动消失，所以选择车座让控件隐藏
        browser.find_element_by_id("capaSel").click()
        time.sleep(1)
        browser.find_element_by_xpath("//select[@id='capaSel']/option[3]").click()
        time.sleep(1)
        browser.find_element_by_id("toCity").send_keys(u"广州")
        time.sleep(1)
        browser.find_element_by_id("toAi").send_keys(u"越秀区越秀公园")
        time.sleep(2)
        browser.find_element_by_xpath("//div[@id='tangram-suggestion--TANGRAM__o-main']/div[2]/table/tbody/tr/td/i").click()
        time.sleep(1)
        browser.find_element_by_id("withTolls").click()
        time.sleep(1)
        browser.find_element_by_id("page1Next").click()
        time.sleep(3)
        browser.find_element_by_id("page2next").click()
        time.sleep(1)
        browser.get_screenshot_as_file("F:\\test_case\\erro_png\\page2next.png")
        time.sleep(1)
        browser.find_element_by_id("contractName").send_keys(u"张三")
        time.sleep(1)
        browser.find_element_by_id("contractPhone").send_keys(u"18707148477")
        time.sleep(1)
        #高级选项
        browser.find_element_by_id("img").click()
        #browser.find_element_by_id("contr_text_user").send_keys(u"test1")
        #勾选业务属性
        browser.find_element_by_xpath("//li[@id='contr_checkbox_driver_info']/label[2]").click()
        #车辆年限选择
        browser.find_element_by_xpath("//select[@id='contr_select_bus_info']/option[2]").click()
        time.sleep(2)
        browser.find_element_by_id("formSubmit").click()
        time.sleep(3)
        browser.find_element_by_id("paybtn").click()
        time.sleep(3)
        browser.get_screenshot_as_file("F:\\test_case\\erro_png\\jiesong.png")

    def test_gentuan(self):
        u"""跟团类型下单"""
        browser = self.browser
        browser.find_element_by_link_text("在线订车").click()
        time.sleep(2)
        browser.find_element_by_id("jobType").click()
        time.sleep(1)
        browser.find_element_by_xpath("//option[@value='1']").click()
        time.sleep(1)
        browser.find_element_by_id("fromDate").send_keys(u"2016-12-29 21:31:20")
        time.sleep(2)
        #因为时间控件无法自动消失，所以选择车型让控件隐藏
        browser.find_element_by_id("carTypeSel").click()
        time.sleep(1)
        browser.find_element_by_xpath("//select[@id='carTypeSel']/option[4]").click()
        time.sleep(1)
        #browser.find_element_by_id("fromCity").click()
        #time.sleep(2)
        browser.find_element_by_id("fromCity").send_keys(u"深圳")
        time.sleep(2)
        browser.find_element_by_id("fromAi").send_keys(u"宝安区深圳北站")
        time.sleep(2)
        browser.find_element_by_xpath("//div[@id='tangram-suggestion--TANGRAM__5-main']/div[2]/table/tbody/tr/td/i").click()
        #time.sleep(1)
        #browser.find_element_by_id("bookBtn").click()
        #time.sleep(1)
        browser.find_element_by_id("endDates").send_keys(u"2016-12-30 21:31:20")
        time.sleep(1)
        #因为时间控件无法自动消失，所以选择车座让控件隐藏
        browser.find_element_by_id("capaSel").click()
        time.sleep(1)
        browser.find_element_by_xpath("//select[@id='capaSel']/option[3]").click()
        time.sleep(1)
        browser.find_element_by_id("toCity").send_keys(u"深圳")
        time.sleep(1)
        browser.find_element_by_id("toAi").send_keys(u"宝安区梅林海关")
        time.sleep(2)
        browser.find_element_by_xpath("//div[@id='tangram-suggestion--TANGRAM__o-main']/div[2]/table/tbody/tr/td/i").click()
        time.sleep(1)
        browser.find_element_by_id("tdays").click()
        time.sleep(3)
        browser.find_element_by_xpath("//select[@id='tdays']/option[2]").click()
        time.sleep(2)
        browser.find_element_by_id("withTolls").click()
        time.sleep(1)
        browser.find_element_by_id("page1Next").click()
        time.sleep(3)
        browser.find_element_by_id("page2next").click()
        time.sleep(1)
        browser.find_element_by_id("contractName").send_keys(u"张三")
        time.sleep(1)
        browser.find_element_by_id("contractPhone").send_keys(u"18707148477")
        time.sleep(1)
        #高级选项
        browser.find_element_by_id("img").click()
        #browser.find_element_by_id("contr_text_user").send_keys(u"test1")
        #勾选业务属性
        browser.find_element_by_xpath("//li[@id='contr_checkbox_driver_info']/label[1]").click()
        #车辆年限选择
        browser.find_element_by_xpath("//select[@id='contr_select_bus_info']/option[3]").click()
        time.sleep(2)
        browser.find_element_by_id("formSubmit").click()
        time.sleep(3)
        browser.find_element_by_id("paybtn").click()
        time.sleep(3)
        browser.get_screenshot_as_file("F:\\test_case\\erro_png\\gentuan.png")

    def is_element_present(self, how, what):
        try: self.browser.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True

    def is_alert_present(self):
        try: self.browser.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.browser.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.browser.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    suite = unittest.TestSuite()

    suite.addTest(Senbaba("test_jiesong"))
    suite.addTest(Senbaba("test_gentuan"))

    filename='F:\\test_case\\erro_png\\result1.html'
    fp=file(filename,'wb')

    runner=HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title='Report_title',
        description='Report_description'
    )

    runner.run(suite)