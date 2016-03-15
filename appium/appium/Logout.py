#coding=utf-8
from appium import webdriver
import time

def logout(self):
    button2=self.driver.find_element_by_id("mineRd").click()
    exit1=self.driver.find_element_by_id("com.senbaba.senbacust:id/exitBtn").click()
    ensure5=self.driver.find_element_by_id("com.senbaba.senbacust:id/ensureTv").click()
    print(u"---帐号退出成功---")