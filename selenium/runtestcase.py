# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
import jiesong
import gentuan
import enterprises
import guojing
import loginout
import HTMLTestRunner
import two

class Senbaba(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(r"c:/python27/chromedriver.exe")
        self.browser.implicitly_wait(10)
        self.base_url = "http://www.senbaba.cn/"
        self.verificationErrors = []
        self.accept_next_alert = True
        self.browser.get(self.base_url)
        self.browser.maximize_window()
        self.browser.find_element_by_link_text("登录").click()
        self.browser.find_element_by_name("username").send_keys(u"18707148477")
        self.browser.find_element_by_id("pwd").send_keys(u"123456")
        self.browser.find_element_by_class_name("loginBtn").click()
        print(u"-------登录成功！--------")

    def test_jiesong(self):
        jiesong.jiesong(self)

    def test_gentuan(self):
        gentuan.gentuan(self)

    def test_guojing(self):
        guojing.guojing(self)

    def test_enterprise(self):
        #two.login('a')
        enterprises.enterprises(self)

    def test_loginout(self):
        loginout.loginout(self)

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
    suite.addTest(Senbaba("test_guojing"))

    filename='F:\\test_case\\erro_png\\result1.html'
    fp=file(filename,'wb')

    runner=HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title='Report_title',
        description='Report_description'
    )

    runner.run(suite)