# -*- coding: utf-8 -*-
from selenium import webdriver
import time

values=['s','b',u"大石"]
for serch in values:
    driver=webdriver.Chrome()
    driver.get("http://www.baidu.com")
    driver.find_element_by_id("kw").send_keys(serch)
    time.sleep(2)
    driver.find_element_by_id("su").click()
    result=driver.find_element_by_id("kw").is_displayed()
    print(result)
    driver.quit()