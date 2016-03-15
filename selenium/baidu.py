from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
import HTMLTestRunner

class Baidu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(r"c:/python27/chromedriver.exe")
        self.driver.implicitly_wait(30)
        self.base_url = "http://testweb.senbaba.cn/loginpage"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_baidu(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_name("username").send_keys(u"18707148477")
        driver.find_element_by_id("pwd").send_keys(u"292819")
        driver.find_element_by_class_name("loginBtn").click()
        time.sleep(1)
        driver.maximize_window()
        time.sleep(2)

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(Baidu("aaaa"))
    results = unittest.TextTestRunner().run(suite)