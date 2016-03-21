# -*- coding: utf-8 -*-
import unittest, time, re
import method

def jiesong(self):
    u"""接送类型下单"""
    browser = self.browser
    browser.find_element_by_link_text("在线订车").click()
    browser.find_element_by_class_name("type1_on").click()
    time.sleep(1)
    method.method(browser,'a')
    print(u"-----接送下单成功未支付-----")