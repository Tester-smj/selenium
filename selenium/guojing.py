# -*- coding: utf-8 -*-
import unittest, time, re
import method

def guojing(self):
    u"""接送类型下单"""
    browser = self.browser
    browser.find_element_by_link_text("在线订车").click()
    browser.find_element_by_id("jobType").click()
    time.sleep(1)
    browser.find_element_by_xpath("//option[@value='3']").click()
    time.sleep(1)
    method.method(browser,'a')
    print(u"-----过境下单成功未支付-----")