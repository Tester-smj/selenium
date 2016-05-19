#coding=utf-8
import time

values=["jsRB","bcRB","sgRB"]
def method(self):
    button=self.driver.find_element_by_id("indexRd").click()
    #订车类型选择
    for search in values:
        type=self.driver.find_element_by_id(search).click()
        c2nextbtn=self.driver.find_element_by_id("com.senbaba.senbacust:id/nextBtn").click()
        #车类型选择，通过坐标滑动来实现
        #cartype=self.driver.find_element_by_id("capacityTv").click()
        #time.sleep(2)
        #largeTypePicker1=self.driver.swipe(317, 1442, 350, 1688, 200)
        #time.sleep(2)
        #SmallTypePicker1=self.driver.swipe(950, 1500, 930, 1600, 200)
        #time.sleep(2)
        #ensure.click()
        #用车时间选择，通过坐标滑动来实现
        time1=self.driver.find_element_by_id("orderCarTimeTv")
        time1.click()
        #小米
        #TimePicker1=self.driver.swipe(200, 1000, 200, 1120, 220)
        #魅族
        TimePicker1=self.driver.swipe(300, 1500, 300, 1700, 200)
        time.sleep(0.5)
        ensure=self.driver.find_element_by_id("com.senbaba.senbacust:id/ensureTv")
        ensure.click()
        try:
            #用车天数选择
            useday=self.driver.find_element_by_id("com.senbaba.senbacust:id/dayNumTv")
            useday.click()
            #小米
            #daypicker=self.driver.swipe(550, 1000, 550, 1200, 200)
            #魅族
            daypicker=self.driver.swipe(950, 1500, 930, 1600, 200)
            ensure.click()
        except:
            print(u"---非跟团不需要选择天数---")
        #起点终点地址选择
        starTv=self.driver.find_element_by_id("com.senbaba.senbacust:id/startTv")
        starTv.click()
        textview=self.driver.find_element_by_id("com.senbaba.senbacust:id/area")
        textview.send_keys(u"深圳北站")
        time.sleep(1.5)
        starid=self.driver.tap([(300,320)],)
        time.sleep(0.5)
        endTv=self.driver.find_element_by_id("com.senbaba.senbacust:id/endTv")
        endTv.click()
        textview.send_keys(u"广州市南站")
        time.sleep(1.5)
        endid=self.driver.tap([(300,320)],)
        time.sleep(0.5)
        #点击下一步，获取价格
        nextbtn=self.driver.find_element_by_id("com.senbaba.senbacust:id/nextBtn")
        nextbtn.click()
        #try:
            #self.driver.find_element_by_id("orderCarTimeTv").is_Displayed()
        #except:
            #print(u"---跨市跟团不可半日游！---")
        #用车天数选择1天
            #useday=self.driver.find_element_by_id("com.senbaba.senbacust:id/dayNumTv")
            #useday.click()
            #daypicker=self.driver.swipe(700, 1760, 700, 1660, 200)
            #time.sleep(1.5)
            #ensure.click()
            #再次提交订单
        #nextbtn=self.driver.find_element_by_id("com.senbaba.senbacust:id/nextBtn")
        #nextbtn.click()
        print(u"---价格获取成功---")
        #返回去选择含路费
        backbtn=self.driver.find_element_by_id("com.senbaba.senbacust:id/back")
        backbtn.click()
        lf=self.driver.find_element_by_id("com.senbaba.senbacust:id/hanlufeiCb")
        lf.click()
        #点击下一步
        nextbtn=self.driver.find_element_by_id("com.senbaba.senbacust:id/nextBtn")
        nextbtn.click()
        #点击下一步
        nextbtn.click()
        time.sleep(0.5)
        #高级选项
        highOptionT=self.driver.find_element_by_id("com.senbaba.senbacust:id/highOptionT")
        highOptionT.click()
        #业务属性
        t=self.driver.find_element_by_name(u"送关").click()
        #车辆新旧程度选择
        ct=self.driver.find_element_by_name(u"全部").click()
        try:
            #小米
            #yearpicker=self.driver.swipe(500, 1010, 500, 1180, 200)
            #魅族
            yearpicker=self.driver.swipe(950, 1500, 930, 1600, 200)
        except:
            return
        time.sleep(0.5)
        ensure=self.driver.find_element_by_id("com.senbaba.senbacust:id/ensureTv").click()
        #点击确定
        print(u"---高级属性设置成功---")
        nextbtn=self.driver.find_element_by_id("com.senbaba.senbacust:id/nextBtn")
        nextbtn.click()
        #备注
        remark=self.driver.find_element_by_id("com.senbaba.senbacust:id/descEd")
        remark.send_keys("test script")
        #提交订单
        nextbtn.click()
        #优惠码使用
        coupon=self.driver.find_element_by_id("com.senbaba.senbacust:id/settlement_down_edit")
        couponuse=self.driver.find_element_by_id("com.senbaba.senbacust:id/add_coupons_bt")
        coupon.send_keys("111111")
        couponuse.click()
        time.sleep(0.5)
        try:
            swipe=self.driver.swipe(400, 1000, 400, 600, 300)
        except:
            print(u"---报错啦--")
        nextbtn.click()
        print(u"---订单提交成功---")
        #判断当前有未支付订单
        try:
            #if self.driver.find_element_by_id("com.senbaba.senbacust:id/titleTv").text == u"您还有订单未支付":
            #print(u"---当前有未支付订单---")
            ensure=self.driver.find_element_by_id("com.senbaba.senbacust:id/ensureTv")
            ensure.click()
            print(u"---当前有未支付订单---")
            #支付宝支付
            paybtn=self.driver.find_element_by_id("com.senbaba.senbacust:id/payBtn")
            paybtn.click()
            time.sleep(1.5)
            self.driver.back()
            # if self.driver.find_element_by_id():
            #     self.driver.back()
            # else:
            #     self.driver.back()
            #微信支付
            wxpay=self.driver.find_element_by_id("com.senbaba.senbacust:id/wxCb")
            wxpay.click()
            paybtn=self.driver.find_element_by_id("com.senbaba.senbacust:id/payBtn")
            paybtn.click()
            time.sleep(1.5)
        except:
            print(u"---当前无未支付订单---")
            #支付宝支付
            paybtn=self.driver.find_element_by_id("com.senbaba.senbacust:id/payBtn")
            paybtn.click()
            time.sleep(2.5)
            self.driver.back()
            #微信支付
            wxpay=self.driver.find_element_by_id("com.senbaba.senbacust:id/wxCb")
            wxpay.click()
            paybtn=self.driver.find_element_by_id("com.senbaba.senbacust:id/payBtn")
            paybtn.click()
            time.sleep(2.5)
        #取消支付跳转至首页
        backbtn=self.driver.back()
        backbtn=self.driver.back()
        ensure=self.driver.find_element_by_id("com.senbaba.senbacust:id/ensureTv")
        ensure.click()
        if search=="bcRB":
            print(u"---跟团类型下单成功未支付---")
        elif search=="sgRB":
            print(u"---过境类型下单成功未支付---")
        else:
            print(u"---接送类型下单成功未支付---")