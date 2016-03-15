#coding=utf-8
from appium import webdriver
import time

def gentuan(self):
    #id实例化，避免重复声明
    button=self.driver.find_element_by_id("indexRd").click()
    #订车类型选择
    type=self.driver.find_element_by_id("bcRL").click()
    #车类型选择，通过坐标滑动来实现
    cartype=self.driver.find_element_by_id("carTypeL").click()
    time.sleep(2)
    #ct=self.driver.find_element_by_id("com.senbaba.senbacust:id/largeTypePicker").scroll_to(u"中港两地")
    largeTypePicker1=self.driver.swipe(317, 1442, 350, 1688, 200)
    time.sleep(2)
    SmallTypePicker1=self.driver.swipe(950, 1500, 930, 1600, 200)
    time.sleep(2)
    ensure=self.driver.find_element_by_id("com.senbaba.senbacust:id/ensureTv")
    ensure.click()
    #用车时间选择，通过坐标滑动来实现
    time1=self.driver.find_element_by_id("orderCarTimeTv")
    time1.click()
    TimePicker1=self.driver.swipe(500, 1800, 500, 1660, 220)
    time.sleep(1)
    ensure.click()
    #用车天数选择
    #useday=self.driver.find_element_by_id("com.senbaba.senbacust:id/dayNumTv")
    #useday.click()
    #daypicker=self.driver.swipe(700, 1760, 700, 1660, 200)
    #time.sleep(1.5)
    #ensure.click()
    #起点终点地址选择
    starTv=self.driver.find_element_by_id("com.senbaba.senbacust:id/startTv")
    starTv.click()
    textview=self.driver.find_element_by_id("com.senbaba.senbacust:id/area")
    textview.send_keys(u"深圳北站")
    time.sleep(3)
    starid=self.driver.tap([(300,320)],)
    time.sleep(2)
    endTv=self.driver.find_element_by_id("com.senbaba.senbacust:id/endTv")
    endTv.click()
    textview.send_keys(u"广州市南站")
    time.sleep(2)
    endid=self.driver.tap([(300,320)],)
    time.sleep(2)
    #点击下一步，获取价格
    nextbtn=self.driver.find_element_by_id("com.senbaba.senbacust:id/nextBtn")
    nextbtn.click()
    try:
        nextbtn=self.driver.find_element_by_id("com.senbaba.senbacust:id/nextBtn")
        nextbtn.click()
        highOptionT=self.driver.find_element_by_id("com.senbaba.senbacust:id/highOptionT")
        highOptionT.click()
    except:
        print(u"---跨市跟团不可半日游！---")
        #用车天数选择1天
        useday=self.driver.find_element_by_id("com.senbaba.senbacust:id/dayNumTv")
        useday.click()
        daypicker=self.driver.swipe(700, 1760, 700, 1660, 200)
        time.sleep(1.5)
        ensure.click()
        #再次提交订单
        nextbtn=self.driver.find_element_by_id("com.senbaba.senbacust:id/nextBtn")
        nextbtn.click()
        print(u"---价格获取成功---")
        #截图，不含路费
        savepng=self.driver.get_screenshot_as_file("F:\\test_case\\erro_png\\withooutoll.png")
        time.sleep(2)
        #返回去选择含路费
        backbtn=self.driver.back()
        lf=self.driver.find_element_by_id("com.senbaba.senbacust:id/hanlufeiCb")
        lf.click()
        #点击下一步
        nextbtn=self.driver.find_element_by_id("com.senbaba.senbacust:id/nextBtn")
        nextbtn.click()
        time.sleep(2)
        savepng=self.driver.get_screenshot_as_file("F:\\test_case\\erro_png\\withtoll.png")
        #点击下一步
        nextbtn.click()
        time.sleep(2)
        #高级选项
        highOptionT=self.driver.find_element_by_id("com.senbaba.senbacust:id/highOptionT")
        highOptionT.click()
        #业务属性
        t=self.driver.find_element_by_name(u"送关").click()
        #yewu.click()
        #车辆新旧程度选择
        ct=self.driver.find_element_by_name(u"全部").click()
        #cartime=self.driver.find_element_by_id("com.senbaba.senbacust:id/contentTv").click()
        time.sleep(1)
        yearpicker=self.driver.swipe(700, 1760, 700, 1660, 200)
        time.sleep(1)
        ensure=self.driver.find_element_by_id("com.senbaba.senbacust:id/ensureTv").click()
        savepng=self.driver.get_screenshot_as_file("F:\\test_case\\erro_png\\highOption.png")
        #点击确定
        print(u"---高级属性设置成功!---")
        nextbtn=self.driver.find_element_by_id("com.senbaba.senbacust:id/nextBtn")
        nextbtn.click()
        #提交订单
        nextbtn.click()
    print(u"---订单提交成功---")
    #判断当前有未支付订单,未避免出错异常处理
    try:
        if self.driver.find_element_by_id("com.senbaba.senbacust:id/titleTv").text != "":
            #print(u"---当前有未支付订单！---")
            ensure=self.driver.find_element_by_id("com.senbaba.senbacust:id/ensureTv")
            ensure.click()
    except:
        #print(u"当前无未支付订单！")
        savepng=self.driver.get_screenshot_as_file("F:\\test_case\\erro_png\\nopayment.png")
        #backbtn=self.driver.find_element_by_id("com.senbaba.senbacust:id/back").click()
        #ensure5=self.driver.tap([(800,1050)],)
        #支付宝支付截图
        paybtn=self.driver.find_element_by_id("com.senbaba.senbacust:id/payBtn")
        paybtn.click()
        time.sleep(3)
        self.driver.get_screenshot_as_file("F:\\test_case\\erro_png\\zfbpay.png")
        self.driver.back()
        #yes=self.driver.tap([(550,1100)],)
        #微信支付截图
        time.sleep(2)
        wxpay=self.driver.find_element_by_id("com.senbaba.senbacust:id/wxCb")
        wxpay.click()
        paybtn=self.driver.find_element_by_id("com.senbaba.senbacust:id/payBtn")
        paybtn.click()
        time.sleep(2)
        self.driver.get_screenshot_as_file("F:\\test_case\\erro_png\\wxpay.png")
    else:
        savepng=self.driver.get_screenshot_as_file("F:\\test_case\\erro_png\\nopayment.png")
        #支付宝支付截图
        paybtn=self.driver.find_element_by_id("com.senbaba.senbacust:id/payBtn")
        paybtn.click()
        time.sleep(5)
        self.driver.get_screenshot_as_file("F:\\test_case\\erro_png\\zfbpay.png")
        self.driver.back()
        #微信支付截图
        time.sleep(1)
        wxpay=self.driver.find_element_by_id("com.senbaba.senbacust:id/wxCb")
        wxpay.click()
        paybtn=self.driver.find_element_by_id("com.senbaba.senbacust:id/payBtn")
        paybtn.click()
        time.sleep(5)
        self.driver.get_screenshot_as_file("F:\\test_case\\erro_png\\wxpay.png")
        #paybtn=self.driver.find_element_by_id("com.senbaba.senbacust:id/payBtn")
        #paybtn.click()
        #time.sleep(4)
        #self.driver.get_screenshot_as_file("F:\\test_case\\erro_png\\pay2.png")
    #退出帐号
    #button2=self.driver.find_element_by_id("mineRd").click()
    #exit1=self.driver.find_element_by_id("com.senbaba.senbacust:id/exitBtn").click()
    #ensure5=self.driver.find_element_by_id("com.senbaba.senbacust:id/ensureTv").click()
    backbtn=self.driver.back()
    backbtn=self.driver.back()
    gupay=self.driver.find_element_by_id("com.senbaba.senbacust:id/ensureTv").click()
    print(u"---跟团类型下单成功未支付！---")