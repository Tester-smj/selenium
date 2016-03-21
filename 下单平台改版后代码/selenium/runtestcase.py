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
import sys
import Myorder
import Login
import method

class Senbaba(unittest.TestCase):
    def setUp(self):
        Login.login(self)

    def test_jiesong(self):
        u"""接送类型下单"""
        jiesong.jiesong(self)

    def test_gentuan(self):
        u"""跟团类型下单"""
        gentuan.gentuan(self)

    def test_guojing(self):
        u"""过境类型下单"""
        guojing.guojing(self)

    def test_enterprise(self):
        u"""企业加入"""
        #two.login('a')
        enterprises.enterprises(self)

    def test_loginout(self):
        u"""用户退出"""
        loginout.loginout(self)

    def test_myoder(self):
        u"""我的订单"""
        Myorder.myorder(self)

    #def test_order(self):
        #method.method(self)

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
    reload(sys)
    sys.setdefaultencoding('utf8')
    suite = unittest.TestSuite()
    suite.addTest(Senbaba("test_jiesong"))
    suite.addTest(Senbaba("test_gentuan"))
    suite.addTest(Senbaba("test_guojing"))
    suite.addTest(Senbaba("test_enterprise"))
    suite.addTest(Senbaba("test_loginout"))
    suite.addTest(Senbaba("test_myoder"))
    filename='F:\\test_case\\erro_png\\webresult.html'
    fp=file(filename,'wb')
    runner =HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u'下单平台web测试报告',
        description=u'用例执行情况：')
    runner.run(suite)