# -*- coding: utf-8 -*-
import random

d=random.uniform(0,10)
a=str(d)
def enterprises(self):
    button2=self.driver.find_element_by_id("mineRd").click()
    join=self.driver.find_element_by_id("com.senbaba.senbacust:id/vipT").click()
    name=self.driver.find_element_by_id("com.senbaba.senbacust:id/qyNameEd").send_keys(u"测试"+a)
    add=self.driver.find_element_by_id("com.senbaba.senbacust:id/qyAddEd").send_keys(u"123")
    contact=self.driver.find_element_by_id("com.senbaba.senbacust:id/linkNameEd").send_keys(u"测试")
    phonenumb=self.driver.find_element_by_id("com.senbaba.senbacust:id/linkPhoneEd").send_keys("07556111915")
    postbtn=self.driver.find_element_by_id("com.senbaba.senbacust:id/postBtn").click()
    for i in range(0,3):
        if i<3:
            self.driver.back()
            i+=1;
            print(i)
        else:
            return

