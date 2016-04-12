# -*- coding: utf-8 -*-
import time

from CommenMethod import Method


def jargon(self):
    u"""黑话下单"""
    browser = self.browser
    browser.find_element_by_link_text(u"在线订车").click()
    time.sleep(2)
    #黑话功能
    browser.find_element_by_id("jargon_input").send_keys(u"深圳")
    time.sleep(2)
    #jargon.click()
    #jargon.send_keys("深圳")
    select=browser.find_element_by_xpath("//*[@id='jargon_list']/div/table/tbody/tr[2]/td").click()
    time.sleep(1)
    Method.method(browser)
    print(u"-----过境下单成功未支付-----")