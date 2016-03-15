# -*- coding: utf-8 -*-
from selenium import webdriver #引入webdriver和time类
import time
import runtestcase #引入登录模块

#driver = webdriver.Chrome() #启动浏览器
#driver.maximize_window()    #最大化浏览器
#driver.get("http://weibo.com") #打开微博
#runtestcase.login() #调用登录模块


#登录模块
#def login():
driver = webdriver.Chrome() #启动浏览器
driver.maximize_window()    #最大化浏览器
driver.get("http://www.senbaba.cn/loginpage") #打开微博
time.sleep(2)
driver.find_element_by_name("username").send_keys(u"18707148477")
driver.find_element_by_id("pwd").send_keys(u"123456")
driver.find_element_by_class_name("loginBtn").click()
cookie=driver.get_cookies()
print cookie
#elem=driver.find_element_by_xpath("//*[@id='pl_login_form']/div[2]/div[1]/div/a[2]").click() #找到微博登录界面
#uname=driver.find_element_by_xpath("//*[@id='pl_login_form']/div[2]/div[3]/div[1]/div/input").send_keys(u"811504083@qq.com") #输入帐号
#pwd=driver.find_element_by_xpath("//*[@id='pl_login_form']/div[2]/div[3]/div[2]/div/input").send_keys("292819smj")#输入密码
#login=driver.find_element_by_xpath("//*[@id='pl_login_form']/div[2]/div[3]/div[6]/a").click()#点击登录
#driver.add_cookie({'name':'Uname','value':'18707148477'})
#driver.add_cookie({'name':'Upwd','value':'123456'})
#driver.get("http://www.senbaba.cn/")

