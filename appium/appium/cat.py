#coding=utf-8
from appium import webdriver
import time
import unittest

class NiujiabangApp(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1'
        desired_caps['deviceName'] = 'm1 note'
        desired_caps['appPackage'] = 'com.niuhome.jiazheng'
        desired_caps['appActivity'] = '.LoadingActivity'
        desired_caps["unicodeKeyboard"] = "True"
        desired_caps["resetKeyboard"] = "True"
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        time.sleep(5)

    def test_normalclean(self):
        nc=self.driver.find_element_by_id("com.niuhome.jiazheng:id/ordinary_clean_line").click()
        time.sleep(1)
        yy=self.driver.find_element_by_id("com.niuhome.jiazheng:id/resever_bt").click()
        time.sleep(1)
        uname=self.driver.find_element_by_id("com.niuhome.jiazheng:id/login_username").send_keys(u"18707148477")
        time.sleep(1)
        pwd=self.driver.find_element_by_id("com.niuhome.jiazheng:id/login_password").send_keys(u"123465")
        time.sleep(1)
        login=self.driver.find_element_by_id("com.niuhome.jiazheng:id/login_button").click()
        backbtn=self.driver.back()
        backbtn=self.driver.back()
        backbtn=self.driver.back()
        backbtn=self.driver.back()

if __name__ == "__main__":
      suite = unittest.TestSuite()
      suite.addTest(NiujiabangApp("asd"))
      results = unittest.TextTestRunner().run(suite)
