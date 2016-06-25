# -*- coding: utf-8 -*-
import time

def method(browser):
    #for jobtype in values:
        #browser = self.browser
        #browser.find_element_by_link_text("在线订车").click()
        #browser.find_element_by_class_name(jobtype).click()
    print("---测试开始---")
    #黑话功能
    fromcity=browser.find_element_by_id('fromCity')
    if fromcity.get_attribute('oldvalue') != u'广州市'and fromcity.get_attribute('oldvalue') != u'深圳市' :
        print("---未选择黑话---")
        fromcity=browser.find_element_by_id('fromCity').send_keys(u"深圳")
        fromaddr=browser.find_element_by_id('fromAi').send_keys(u"宝安区深圳北站")
        time.sleep(1)
        fromcity=browser.find_element_by_xpath("//div[@id='tangram-suggestion--TANGRAM__5-main']/div[2]/table/tbody/tr/td/i").click()
        tocity=browser.find_element_by_id("toCity").send_keys(u"广州")
        toai=browser.find_element_by_id("toAi").send_keys(u"越秀区越秀公园")
        time.sleep(1)
        toai=browser.find_element_by_xpath("//div[@id='tangram-suggestion--TANGRAM__o-main']/div[2]/table/tbody/tr/td/i").click()
        time.sleep(1)
    else:
        print("---黑话已经识别---")
        #时间选择
    fromdate=browser.find_element_by_id('fromDate').send_keys("2016-12-29 21:31:20")
    time.sleep(1)
    fromdate=browser.find_element_by_id('toDate').send_keys("2016-12-30 21:31:20")
    #车类型选择
    capasel=browser.find_element_by_id("capaSel").click()
    capasel=browser.find_element_by_xpath("//select[@id='capaSel']/option[1]").click()
    #车座选择
    carTypeSel=browser.find_element_by_id("carTypeSel").click()
    carset=browser.find_element_by_xpath("//*[@id='carTypeSel']/option[1]").click()
    #车辆数选择
    vehicleCount=browser.find_element_by_id("vehicleCount")
    vehicleCount.clear()
    vehicleCount.send_keys("2")
    #添加途经点
    #addPoint=browser.find_element_by_class_name("addPoint").click()
    #city0=browser.find_element_by_id("city0").send_keys(u"深圳")
    #time.sleep(1)
    #addr0=browser.find_element_by_id("addr0").send_keys(u"深圳湾口岸")
    #time.sleep(1.5)
    #addr=browser.find_element_by_xpath("//div[@id='tangram-suggestion--TANGRAM__18-main']/div[2]/table/tbody/tr/td/i").click()
    #time.sleep(1.5)
    #withtolls=browser.find_element_by_xpath("//*[@id='orderForm']/div[1]/div[4]/div[1]/div[4]/div[1]/div/ins").click()
    #withtolls=browser.find_element_by_id("withTolls").click()
    #航班号
    hbh=browser.find_element_by_id("tagValue").send_keys("test")
    #团号
    th=browser.find_element_by_id("tripValue").send_keys("testth")
    try:
        browser.find_element_by_id("tdays").click()
        browser.find_element_by_xpath("//select[@id='tdays']/option[2]").click()
    except:
        print("-----非跟团不用选择天数---")
    try:
        addltion=browser.find_element_by_xpath("//*[@id='orderForm']/div[1]/div[4]/div[1]/div[4]/div[2]/div/ins").click()
    except:
        print("----非送关帐号无加点---")
    page1next=browser.find_element_by_id("nextBtn").click()
    time.sleep(1)
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
    # try:
    #     time.sleep(1)
    #     price=browser.find_element_by_id("price")
    #     price.clear()
    #     price.send_keys("500")
    #     time.sleep(1)
    #     print(u"------价格自定义成功！---")
    # except:
    #     print(u"-------无权限自定义价格！---")
    # time.sleep(1.5)
    # FixedPrice=price.get_attribute('value')
    # if price.get_attribute('value') == '1700':
    #     print(u"当前价格为:"+FixedPrice)
    # else:
    #     print(u"---固定价格设置失效---")
    #     print(u"当前价格为:"+FixedPrice)
    #下一步
    time.sleep(3)
    #议价选择
    # js="var q=document.getElementsByClassName('icheckbox_square-croci')[2].setAttribute('class','icheckbox_square-croci checked');"
    # js1="var q=document.getElementsByClassName('content confirmBox')"
    # print(js1)
    # #调用js  icheckbox_square-croci check   icheckbox_square-croci checked
    # browser.execute_script(js)
    ccc=browser.find_element_by_xpath("//*[@id='orderForm']/div[2]/div[5]/div[3]/div").click()
    # time.sleep(5)
    sure1=browser.find_element_by_xpath("//*[@id='layui-layer2']/span/a").click()
    # time.sleep(15)
    #browser.switch_to_frame("layui-layer-content")
    #sure=browser.find_element_by_text(u"确定").click()
    #print(u"非月结无议价选项")
    page2next=browser.find_element_by_id("checkBtn").click()
    time.sleep(1)
    contractname=browser.find_element_by_id("contractName").send_keys(u"张三")
    contractphone=browser.find_element_by_id("contractPhone").send_keys(u"18707148477")
    remark=browser.find_element_by_id("remark").send_keys("test")
    time.sleep(0.5)
    c=browser.find_element_by_id("advanced_title").click()
    time.sleep(0.5)
    #browser.find_element_by_id("contr_text_user").send_keys(u"test1")
    #勾选业务属性
    d=browser.find_element_by_xpath("//*[@id='contr_checkbox_driver_info']/div[3]/div/ins").click()
    #车辆年限选择//*[@id="contr_checkbox_driver_info"]/div[2]/div/ins
    e=browser.find_element_by_xpath("//select[@id='contr_select_bus_info']/option[2]").click()
    time.sleep(1)
    v=browser.find_element_by_id("viewBtn").click()
    time.sleep(1)
    f=browser.find_element_by_id("submitBtn").click()
    time.sleep(0.5)
    g=browser.find_element_by_id("paybtn").click()
    time.sleep(0.5)
    #智能等待
    #values=['fromDate','capaSel','fromCity','fromAi','page1Next']
    #element=WebDriverWait(browser,10).until(lambda browser:browser.find_element_by_id(values))
    #print(u"---下单失败！---")



