#coding=utf-8
from appium import webdriver
import time
import unittest
import gentuan
import jiesong
import guojing
import Login
import method

class SenbabaApp(unittest.TestCase):
    def setUp(self):
        Login.login(self)

    def test_xiadan(self):
        method.method(self)

if __name__ == "__main__":
      suite = unittest.TestSuite()
      suite.addTest(SenbabaApp("login"))
      results = unittest.TextTestRunner().run(suite)


