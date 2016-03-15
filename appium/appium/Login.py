#coding=utf-8
from appium import webdriver
import time

def login(self):
    desired_caps = {}
    #平台
    desired_caps['platformName'] = 'Android'
    #版本号
    desired_caps['platformVersion'] = '5.1'
    #设备名
    desired_caps['deviceName'] = 'm1 note'
    #待测试的app的Package名字
    desired_caps['appPackage'] = 'com.senbaba.senbacust'
    #待测试的app的Activity名字
    desired_caps['appActivity'] = '.LaunchActivity'
    #正常使用中文输入法
    desired_caps["unicodeKeyboard"] = "True"
    desired_caps["resetKeyboard"] = "True"
    #启动设备
    self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    self.driver.implicitly_wait(30)
    button=self.driver.find_element_by_id("tranRd").click()
    #判断用户是否为登录状态
    try:
        if self.driver.find_element_by_id("com.senbaba.senbacust:id/indexRd").text !="":
            print(u"用户已登录！")
            button=self.driver.find_element_by_id("indexRd").click()
    except:
        print(u"用户未登录！")
        savepng=self.driver.get_screenshot_as_file("F:\\test_case\\erro_png\\login.png")
        uname1=self.driver.find_element_by_id("userNameEd").clear()
        uname=self.driver.find_element_by_id("userNameEd").send_keys(u"18707148477")
        uname1=self.driver.find_element_by_id("pwdEd").clear()
        pwd=self.driver.find_element_by_id("pwdEd").send_keys("123456")
        #rmbpwd=self.driver.find_element_by_id("com.senbaba.senbacust:id/rememberPwd").click()
        self.driver.get_screenshot_as_file("F:\\test_case\\erro_png\\login1.png")
        logbtn1=self.driver.find_element_by_id("loginBt").click()
        print(u"登录成功！")
    else:
        return