# -*- coding: utf-8 -*-
import time

from CommenMethod import Method


def gentuan(self):
    u"""跟团类型下单"""
    browser = self.browser
    browser.find_element_by_link_text("在线订车").click()
    browser.find_element_by_class_name("type1").click()
    time.sleep(1)
    #调用下单公用方法
    Method.method(browser)
    print(u"-----跟团下单成功未支付-----")