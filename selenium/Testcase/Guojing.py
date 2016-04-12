# -*- coding: utf-8 -*-
import time

from CommenMethod import Method


def guojing(self):
    u"""过境类型下单"""
    browser = self.browser
    browser.find_element_by_link_text("在线订车").click()
    browser.find_element_by_class_name("type3").click()
    time.sleep(1)
    Method.method(browser)
    print(u"-----过境下单成功未支付-----")