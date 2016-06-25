# -*- coding: utf-8 -*-
import time

from CommenMethod import Method


def fixedprice(self):
    u"""固定路线价格"""
    browser = self.browser
    browser.find_element_by_link_text(u"在线订车").click()
    time.sleep(2)
    #黑话功能
    browser.find_element_by_id("jargon_input").send_keys(u"深圳宝安到广州越秀")
    time.sleep(2)
    #jargon.click()
    #jargon.send_keys("深圳")
    select=browser.find_element_by_xpath("//*[@id='jargon_list']/div/table/tbody/tr/td").click()
    time.sleep(1)
    Method.method(browser)
    print(u"-----固定路线价格下单成功未支付-----")