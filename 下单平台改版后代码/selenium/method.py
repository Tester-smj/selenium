# -*- coding: utf-8 -*-
import time

values=["type1_on","type2","type3"]
def method(browser,arg):
    #for jobtype in values:
        #browser = self.browser
        #browser.find_element_by_link_text("在线订车").click()
        #browser.find_element_by_class_name(jobtype).click()
    fromdate=browser.find_element_by_id('fromDate').send_keys("2016-12-29 21:31:20")
    time.sleep(1)
    fromdate=browser.find_element_by_id('toDate').send_keys("2016-12-30 21:31:20")
    capasel=browser.find_element_by_id("capaSel").click()
    capasel=browser.find_element_by_xpath("//select[@id='capaSel']/option[1]").click()
    fromcity=browser.find_element_by_id('fromCity').send_keys(u"深圳")
    fromaddr=browser.find_element_by_id('fromAi').send_keys(u"宝安区深圳北站")
    time.sleep(1)
    fromcity=browser.find_element_by_xpath("//div[@id='tangram-suggestion--TANGRAM__5-main']/div[2]/table/tbody/tr/td/i").click()
    tocity=browser.find_element_by_id("toCity").send_keys(u"广州")
    toai=browser.find_element_by_id("toAi").send_keys(u"越秀区越秀公园")
    time.sleep(2)
    toai=browser.find_element_by_xpath("//div[@id='tangram-suggestion--TANGRAM__o-main']/div[2]/table/tbody/tr/td/i").click()
    time.sleep(1)
    withtolls=browser.find_element_by_id("withRoll").click()
    try:
        browser.find_element_by_id("tdays").click()
        browser.find_element_by_xpath("//select[@id='tdays']/option[2]").click()
    except:
        print("非跟团不用选择天数")
        time.sleep(2)
    page1next=browser.find_element_by_id("nextBtn").click()
        #time.sleep(1)
    #判断是否为过境
    #a=browser.find_element_by_id("prevBtn").is_displayed()
    #if not a:
        #toai=browser.find_element_by_id("toAi").clear()
        #time.sleep(2)
        #toai=browser.find_element_by_id("toAi").send_keys(u"香港国际机场")
        #time.sleep(5)
        #toai=browser.find_element_by_xpath("//div[@id='tangram-suggestion--TANGRAM__o-main']/div[2]/table/tbody/tr/td/i").click()
        #time.sleep(2)
    #else:
        #return
    try:
        time.sleep(1)
        a=browser.find_element_by_id("price").clear()
        b=browser.find_element_by_id("price").send_keys("500")
        print(u"---价格自定义成功！---")
    except:
        print(u"---无权限自定义价格！---")
        time.sleep(2)
    page2next=browser.find_element_by_id("nextBtn").click()
    time.sleep(1)
    contractname=browser.find_element_by_id("contractName").send_keys(u"张三")
    contractphone=browser.find_element_by_id("contractPhone").send_keys(u"18707148477")
    time.sleep(1)
    c=browser.find_element_by_id("advanced_title").click()
    time.sleep(2)
    #browser.find_element_by_id("contr_text_user").send_keys(u"test1")
    #勾选业务属性
    d=browser.find_element_by_xpath("//*[@id='contr_checkbox_driver_info']/div[4]/input").click()
    #车辆年限选择//*[@id="contr_checkbox_driver_info"]/div[4]/input
    #
    e=browser.find_element_by_xpath("//select[@id='contr_select_bus_info']/option[2]").click()
    time.sleep(1)
    f=browser.find_element_by_id("submitBtn").click()
    time.sleep(2)
    g=browser.find_element_by_id("paybtn").click()
    time.sleep(1)
    #智能等待
    #values=['fromDate','capaSel','fromCity','fromAi','page1Next']
    #element=WebDriverWait(browser,10).until(lambda browser:browser.find_element_by_id(values))



