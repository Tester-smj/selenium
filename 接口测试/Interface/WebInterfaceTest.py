# -*- coding: utf-8 -*-
import unittest
import requests
import re
import json

class TestCode(unittest.TestCase):
    def setUp(self):
        # 把所需要的一些初始准备数据全都在setUp写好
        #正式环境
        # self.url = "http://www.senbaba.cn/login"
        # 测试环境
        self.url="http://120.24.68.124:8080/sbborders/login"
        self.data ={"uname":"15112408147","pwd":"123456"}
        r=requests.get(self.url,self.data)
        print(type(self.data))
        # new=json.dumps(change, ensure_ascii=False)
        print(r.text)
        # print(r.cookies)
        # print(r.headers)
        global b,q
        b=re.findall("{(.+?)}",str(r.headers))
        # d=simplejson.dumps(b)
        q="".join(b)
        # msg=r.headers.get("Transfer-Encoding")
        # self.assertEqual(msg,'chunked')
    def test_prices(self):
        #正式环境
        self.url="http://www.senbaba.cn/getprice"
        #测试环境
        #self.url="http://120.24.68.124:8080/sbborders/getprice"
        self.data={"car_struct_name":"商务","capacity":"5","etBeginTime":"2016-07-16 15:55:00","etFinishTime":"2016-07-16 15:55:09","vehicleCount":"1","tdays":"0","fromCity":"深圳市","departurePlace":"深圳北站","toCity":"深圳市","destinationPlace":"深圳皇岗口岸","tagValue":"","tripValue":"","cost":"140","contractName":"test","contractPhone":"18707148477","remark":"script","contr_select_bus_info":"0","couponName":"","departureCoords":"{'area':',广州市,越秀区,','coords':[23.155001,113.264057],'name':'广州火车站'}","destinationCoords":"{'area':'广东省,深圳市,福田区,福田南路,','coords':[22.615102,114.035529],'name':'深圳皇岗口岸'}","pathway":"[]","content":"[{'key':'driver_info','name':'司机业务属性','values':[]},{'key':'bus_info','name':'车辆新旧程度','values':{'name':'全部','value':'0'}}]","jobType":"0","confirm":"0","days":"0","tripNo":"","withTolls":"0","addItion":"0","count":"","couponCode":""}
        q=requests.get(self.url,self.data)
        # change=q.json()
        # new=json.dumps(change,ensure_ascii=False)
        print(q.text)
    def test_addorder(self):
        u"""多辆车不议价包销下单"""
        self.url="http://www.senbaba.cn/addorder"
        # self.url="http://120.24.68.124:8080/sbborders/addorder"
        self.data={"car_struct_name":"商务","capacity":"5","etBeginTime":"2017-07-20 15:55:00","etFinishTime":"2017-07-20 15:55:09","vehicleCount":"3","tdays":"0","fromCity":"深圳市","departurePlace":"深圳北站","toCity":"深圳市","destinationPlace":"深圳皇岗口岸","tagValue":"","tripValue":"","cost":"0.01","contractName":"test","contractPhone":"18707148477","remark":"script","contr_select_bus_info":"0","couponName":"","departureCoords":"{'area':',广州市,越秀区,','coords':[23.155001,113.264057],'name':'广州火车站'}","destinationCoords":"{'area':'广东省,深圳市,福田区,福田南路,','coords':[22.615102,114.035529],'name':'深圳皇岗口岸'}","pathway":"[]","content":"[{'key':'driver_info','name':'司机业务属性','values':[]},{'key':'bus_info','name':'车辆新旧程度','values':{'name':'全部','value':'0'}}]","jobType":"0","confirm":"0","days":"0","tripNo":"","withTolls":"0","addItion":"0","count":"3","couponCode":""}
        headers = {'content-type': 'application/json','User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko','Accept':'application/x-ms-application, image/jpeg, application/xaml+xml, image/gif, image/pjpeg, application/x-ms-xbap, */*','Accept-Language':'zh-CN'}
        #月结cookies
        # cookies={'Date': 'Fri, 15 Jul 2016 08:58:20 GMT', 'Set-Cookie': 'JSESSIONID=5E95474D195B256175944EBF887D7610; Path=/sbborders/; HttpOnly, sidd=5E95474D195B256175944EBF887D7610; Expires=Mon, 25-Jul-2016 08:58:20 GMT', 'Content-Length': '665', 'Content-Type': 'application/json;charset=utf-8', 'Server': 'Apache-Coyote/1.1'}
        #现付cookies
        # cookies={'Transfer-Encoding': 'chunked', 'Set-Cookie': 'JSESSIONID=49F988B82FBF364D90BAD46B2FAB0CCC; Path=/sbborders/; HttpOnly, sidd=49F988B82FBF364D90BAD46B2FAB0CCC; Expires=Mon, 25-Jul-2016 10:23:07 GMT', 'Content-Type': 'application/json;charset=utf-8', 'Date': 'Fri, 15 Jul 2016 10:23:07 GMT', 'Server': 'Apache-Coyote/1.1'}
        #正则提取
        cookies={q}
        print(cookies)
        z=requests.get(self.url,self.data,headers=headers,cookies=cookies)
        # change=z.json()
        # new=json.dumps(change, ensure_ascii=False)
        print(z.text)
    def test_addorder1(self):
        u"""单辆车不议价包销下单"""
        self.url="http://www.senbaba.cn/addorder"
        # self.url="http://120.24.68.124:8080/sbborders/addorder"
        self.data={"car_struct_name":"商务","capacity":"5","etBeginTime":"2017-07-20 15:55:00","etFinishTime":"2017-07-20 15:55:09","vehicleCount":"1","tdays":"0","fromCity":"深圳市","departurePlace":"深圳北站","toCity":"深圳市","destinationPlace":"深圳皇岗口岸","tagValue":"","tripValue":"","cost":"0.01","contractName":"test","contractPhone":"18707148477","remark":"script","contr_select_bus_info":"0","couponName":"","departureCoords":"{'area':',广州市,越秀区,','coords':[23.155001,113.264057],'name':'广州火车站'}","destinationCoords":"{'area':'广东省,深圳市,福田区,福田南路,','coords':[22.615102,114.035529],'name':'深圳皇岗口岸'}","pathway":"[]","content":"[{'key':'driver_info','name':'司机业务属性','values':[]},{'key':'bus_info','name':'车辆新旧程度','values':{'name':'全部','value':'0'}}]","jobType":"0","confirm":"0","days":"0","tripNo":"","withTolls":"0","addItion":"0","count":"1","couponCode":""}
        headers = {'content-type': 'application/json','User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko','Accept':'application/x-ms-application, image/jpeg, application/xaml+xml, image/gif, image/pjpeg, application/x-ms-xbap, */*','Accept-Language':'zh-CN'}
        #现付cookies
        # cookies={'Date': 'Fri, 15 Jul 2016 08:58:20 GMT', 'Set-Cookie': 'JSESSIONID=49F988B82FBF364D90BAD46B2FAB0CCC; Path=/sbborders/; HttpOnly, sidd=49F988B82FBF364D90BAD46B2FAB0CCC; Expires=Mon, 25-Jul-2016 08:58:20 GMT', 'Content-Length': '665', 'Content-Type': 'application/json;charset=utf-8', 'Server': 'Apache-Coyote/1.1'}
        #月结cookies
        cookies={'Transfer-Encoding': 'chunked', 'Set-Cookie': 'JSESSIONID=; Path=/sbborders/; HttpOnly, sidd=5E95474D195B256175944EBF887D7610; Expires=Mon, 25-Jul-2016 10:23:07 GMT', 'Content-Type': 'application/json;charset=utf-8', 'Date': 'Fri, 15 Jul 2016 10:23:07 GMT', 'Server': 'Apache-Coyote/1.1'}
        #正则提取
        # cookies={b}
        z=requests.get(self.url,self.data,headers=headers,cookies=cookies)
        # change=z.json()
        # new=json.dumps(change, ensure_ascii=False)
        print(z.text)
    def test_addorder2(self):
        u"""单辆车议价下单"""
        self.url="http://www.senbaba.cn/addorder"
        # self.url="http://120.24.68.124:8080/sbborders/addorder"
        self.data={"car_struct_name":"商务","capacity":"5","etBeginTime":"2017-07-20 15:55:00","etFinishTime":"2017-07-20 15:55:09","vehicleCount":"1","tdays":"0","fromCity":"深圳市","departurePlace":"深圳北站","toCity":"深圳市","destinationPlace":"深圳皇岗口岸","tagValue":"","tripValue":"","cost":"0.01","contractName":"test","contractPhone":"18707148477","remark":"script","contr_select_bus_info":"0","couponName":"","departureCoords":"{'area':',广州市,越秀区,','coords':[23.155001,113.264057],'name':'广州火车站'}","destinationCoords":"{'area':'广东省,深圳市,福田区,福田南路,','coords':[22.615102,114.035529],'name':'深圳皇岗口岸'}","pathway":"[]","content":"[{'key':'driver_info','name':'司机业务属性','values':[]},{'key':'bus_info','name':'车辆新旧程度','values':{'name':'全部','value':'0'}}]","jobType":"0","confirm":"1","days":"0","tripNo":"","withTolls":"0","addItion":"0","count":"1","couponCode":""}
        headers = {'content-type': 'application/json','User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko','Accept':'application/x-ms-application, image/jpeg, application/xaml+xml, image/gif, image/pjpeg, application/x-ms-xbap, */*','Accept-Language':'zh-CN'}
        #现付cookies
        # cookies={'Date': 'Fri, 15 Jul 2016 08:58:20 GMT', 'Set-Cookie': 'JSESSIONID=49F988B82FBF364D90BAD46B2FAB0CCC; Path=/sbborders/; HttpOnly, sidd=49F988B82FBF364D90BAD46B2FAB0CCC; Expires=Mon, 25-Jul-2016 08:58:20 GMT', 'Content-Length': '665', 'Content-Type': 'application/json;charset=utf-8', 'Server': 'Apache-Coyote/1.1'}
        #月结cookies
        cookies={'Transfer-Encoding': 'chunked', 'Set-Cookie': 'JSESSIONID=5E95474D195B256175944EBF887D7610; Path=/sbborders/; HttpOnly, sidd=5E95474D195B256175944EBF887D7610; Expires=Mon, 25-Jul-2016 10:23:07 GMT', 'Content-Type': 'application/json;charset=utf-8', 'Date': 'Fri, 15 Jul 2016 10:23:07 GMT', 'Server': 'Apache-Coyote/1.1'}
        #正则提取
        # cookies={b}
        z=requests.get(self.url,self.data,headers=headers,cookies=cookies)
        # change=z.json()
        # new=json.dumps(change, ensure_ascii=False)
        print(z.text)
    def test_addorder3(self):
        u"""多辆车议价下单"""
        self.url="http://www.senbaba.cn/addorder"
        # self.url="http://120.24.68.124:8080/sbborders/addorder"
        self.data={"car_struct_name":"商务","capacity":"5","etBeginTime":"2017-07-20 15:55:00","etFinishTime":"2017-07-20 15:55:09","vehicleCount":"3","tdays":"0","fromCity":"深圳市","departurePlace":"深圳北站1","toCity":"深圳市","destinationPlace":"深圳皇岗口岸2","tagValue":"","tripValue":"","cost":"0.01","contractName":"test","contractPhone":"18707148477","remark":"script","contr_select_bus_info":"0","couponName":"","departureCoords":"{'area':',广州市,越秀区,','coords':[23.155001,113.264057],'name':'广州火车站'}","destinationCoords":"{'area':'广东省,深圳市,福田区,福田南路,','coords':[22.615102,114.035529],'name':'深圳皇岗口岸'}","pathway":"[]","content":"[{'key':'driver_info','name':'司机业务属性','values':[]},{'key':'bus_info','name':'车辆新旧程度','values':{'name':'全部','value':'0'}}]","jobType":"0","confirm":"1","days":"0","tripNo":"","withTolls":"1","addItion":"0","count":"3","couponCode":""}
        headers = {'content-type': 'application/json','User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko','Accept':'application/x-ms-application, image/jpeg, application/xaml+xml, image/gif, image/pjpeg, application/x-ms-xbap, */*','Accept-Language':'zh-CN'}
        #月结cookies
        cookies={'Date': 'Fri, 15 Jul 2016 08:58:20 GMT', 'Set-Cookie': 'JSESSIONID=5E95474D195B256175944EBF887D7610; Path=/sbborders/; HttpOnly, sidd=5E95474D195B256175944EBF887D7610; Expires=Mon, 25-Jul-2016 08:58:20 GMT', 'Content-Length': '665', 'Content-Type': 'application/json;charset=utf-8', 'Server': 'Apache-Coyote/1.1'}
        #现付cookies
        # cookies={'Transfer-Encoding': 'chunked', 'Set-Cookie': 'JSESSIONID=49F988B82FBF364D90BAD46B2FAB0CCC; Path=/sbborders/; HttpOnly, sidd=49F988B82FBF364D90BAD46B2FAB0CCC; Expires=Mon, 25-Jul-2016 10:23:07 GMT', 'Content-Type': 'application/json;charset=utf-8', 'Date': 'Fri, 15 Jul 2016 10:23:07 GMT', 'Server': 'Apache-Coyote/1.1'}
        #正则提取
        # cookies={b}
        z=requests.get(self.url,self.data,headers=headers,cookies=cookies)
        # change=z.json()
        # new=json.dumps(change, ensure_ascii=False)
        print(z.text)
    def test_addorder4(self):
        u"""单辆车指派车队下单"""
        self.url="http://www.senbaba.cn/addorder"
        # self.url="http://120.24.68.124:8080/sbborders/addorder"
        self.data={"car_struct_name":"商务","capacity":"5","etBeginTime":"2016-07-21 15:55:00","etFinishTime":"2016-07-21 15:55:09","vehicleCount":"1","tdays":"0","fromCity":"深圳市","departurePlace":"深圳北站","toCity":"深圳市","destinationPlace":"深圳皇岗口岸","tagValue":"","tripValue":"","cost":"0.01","contractName":"test","contractPhone":"18707148477","remark":"script","contr_select_bus_info":"0","couponName":"","departureCoords":"{'area':',广州市,越秀区,','coords':[23.155001,113.264057],'name':'广州火车站'}","destinationCoords":"{'area':'广东省,深圳市,福田区,福田南路,','coords':[22.615102,114.035529],'name':'深圳皇岗口岸'}","pathway":"[]","content":"[{'key':'driver_info','name':'司机业务属性','values':[]},{'key':'bus_info','name':'车辆新旧程度','values':{'name':'全部','value':'0'}}]","jobType":"0","confirm":"0","days":"0","tripNo":"","withTolls":"0","addItion":"0","count":"1","couponCode":"","FleetName":"森巴巴测试","fleetCode":"FC14509262022723"}
        headers = {'content-type': 'application/json','User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko','Accept':'application/x-ms-application, image/jpeg, application/xaml+xml, image/gif, image/pjpeg, application/x-ms-xbap, */*','Accept-Language':'zh-CN'}
        #现付cookies
        # cookies={'Date': 'Fri, 15 Jul 2016 08:58:20 GMT', 'Set-Cookie': 'JSESSIONID=49F988B82FBF364D90BAD46B2FAB0CCC; Path=/sbborders/; HttpOnly, sidd=49F988B82FBF364D90BAD46B2FAB0CCC; Expires=Mon, 25-Jul-2016 08:58:20 GMT', 'Content-Length': '665', 'Content-Type': 'application/json;charset=utf-8', 'Server': 'Apache-Coyote/1.1'}
        #月结cookies
        cookies={'Transfer-Encoding': 'chunked', 'Set-Cookie': 'JSESSIONID=5E95474D195B256175944EBF887D7610; Path=/sbborders/; HttpOnly, sidd=5E95474D195B256175944EBF887D7610; Expires=Mon, 25-Jul-2016 10:23:07 GMT', 'Content-Type': 'application/json;charset=utf-8', 'Date': 'Fri, 15 Jul 2016 10:23:07 GMT', 'Server': 'Apache-Coyote/1.1'}
        #正则提取
        # cookies={b}
        z=requests.get(self.url,self.data,headers=headers,cookies=cookies)
        # change=z.json()
        # new=json.dumps(change, ensure_ascii=False)
        print(z.text)
    def test_addorder5(self):
        u"""多辆车指派车队下单"""
        self.url="http://www.senbaba.cn/addorder"
        # self.url="http://120.24.68.124:8080/sbborders/addorder"
        self.data={"car_struct_name":"商务","capacity":"5","etBeginTime":"2016-07-21 15:55:00","etFinishTime":"2016-07-21 15:55:09","vehicleCount":"3","tdays":"0","fromCity":"深圳市","departurePlace":"深圳北站","toCity":"深圳市","destinationPlace":"深圳皇岗口岸","tagValue":"","tripValue":"","cost":"0.01","contractName":"test","contractPhone":"18707148477","remark":"script","contr_select_bus_info":"0","couponName":"","departureCoords":"{'area':',广州市,越秀区,','coords':[23.155001,113.264057],'name':'广州火车站'}","destinationCoords":"{'area':'广东省,深圳市,福田区,福田南路,','coords':[22.615102,114.035529],'name':'深圳皇岗口岸'}","pathway":"[]","content":"[{'key':'driver_info','name':'司机业务属性','values':[]},{'key':'bus_info','name':'车辆新旧程度','values':{'name':'全部','value':'0'}}]","jobType":"0","confirm":"0","days":"0","tripNo":"","withTolls":"0","addItion":"0","count":"3","couponCode":"","FleetName":"森巴巴测试","fleetCode":"FC14509262022723"}
        headers = {'content-type': 'application/json','User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko','Accept':'application/x-ms-application, image/jpeg, application/xaml+xml, image/gif, image/pjpeg, application/x-ms-xbap, */*','Accept-Language':'zh-CN'}
        #现付cookies
        # cookies={'Date': 'Fri, 15 Jul 2016 08:58:20 GMT', 'Set-Cookie': 'JSESSIONID=49F988B82FBF364D90BAD46B2FAB0CCC; Path=/sbborders/; HttpOnly, sidd=49F988B82FBF364D90BAD46B2FAB0CCC; Expires=Mon, 25-Jul-2016 08:58:20 GMT', 'Content-Length': '665', 'Content-Type': 'application/json;charset=utf-8', 'Server': 'Apache-Coyote/1.1'}
        #月结cookies
        cookies={'Transfer-Encoding': 'chunked', 'Set-Cookie': 'JSESSIONID=5E95474D195B256175944EBF887D7610; Path=/sbborders/; HttpOnly, sidd=5E95474D195B256175944EBF887D7610; Expires=Mon, 25-Jul-2016 10:23:07 GMT', 'Content-Type': 'application/json;charset=utf-8', 'Date': 'Fri, 15 Jul 2016 10:23:07 GMT', 'Server': 'Apache-Coyote/1.1'}
        #正则提取
        # cookies={b}
        z=requests.get(self.url,self.data,headers=headers,cookies=cookies)
        # change=z.json()
        # new=json.dumps(change, ensure_ascii=False)
        print(z.text)
    def test_addorder6(self):
        u"""多辆车不包销下单"""
        # self.url="http://www.senbaba.cn/addorder"
        self.url="http://120.24.68.124:8080/sbborders/addorder"
        self.data={"car_struct_name":"商务","capacity":"5","etBeginTime":"2016-07-21 15:55:00","etFinishTime":"2016-07-21 15:55:09","vehicleCount":"3","tdays":"0","fromCity":"深圳市","departurePlace":"深圳北站1","toCity":"深圳市","destinationPlace":"深圳皇岗口岸2","tagValue":"","tripValue":"","cost":"0.01","contractName":"test","contractPhone":"18707148477","remark":"script","contr_select_bus_info":"0","couponName":"","departureCoords":"{'area':',广州市,越秀区,','coords':[23.155001,113.264057],'name':'广州火车站'}","destinationCoords":"{'area':'广东省,深圳市,福田区,福田南路,','coords':[22.615102,114.035529],'name':'深圳皇岗口岸'}","pathway":"[]","content":"[{'key':'driver_info','name':'司机业务属性','values':[]},{'key':'bus_info','name':'车辆新旧程度','values':{'name':'全部','value':'0'}}]","jobType":"0","confirm":"0","days":"0","tripNo":"","withTolls":"0","addItion":"0","count":"3","couponCode":""}
        headers = {'content-type': 'application/json','User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko','Accept':'application/x-ms-application, image/jpeg, application/xaml+xml, image/gif, image/pjpeg, application/x-ms-xbap, */*','Accept-Language':'zh-CN'}
        #月结cookies
        cookies={'Date': 'Fri, 15 Jul 2016 08:58:20 GMT', 'Set-Cookie': 'JSESSIONID=5C17B73B6588A7FA88812AC5076EEB6F; Path=/sbborders/; HttpOnly, sidd=5C17B73B6588A7FA88812AC5076EEB6F; Expires=Mon, 25-Jul-2016 08:58:20 GMT', 'Content-Length': '665', 'Content-Type': 'application/json;charset=utf-8', 'Server': 'Apache-Coyote/1.1'}
        #现付cookies
        # cookies={'Transfer-Encoding': 'chunked', 'Set-Cookie': 'JSESSIONID=49F988B82FBF364D90BAD46B2FAB0CCC; Path=/sbborders/; HttpOnly, sidd=49F988B82FBF364D90BAD46B2FAB0CCC; Expires=Mon, 25-Jul-2016 10:23:07 GMT', 'Content-Type': 'application/json;charset=utf-8', 'Date': 'Fri, 15 Jul 2016 10:23:07 GMT', 'Server': 'Apache-Coyote/1.1'}
        #正则提取
        # cookies={b}
        z=requests.get(self.url,self.data,headers=headers,cookies=cookies)
        # change=z.json()
        # new=json.dumps(change, ensure_ascii=False)
        msg=(z.text).get("status")
        self.assertEqual(msg,'chunked')
        print(z.text)
    # def test_cancleorder(self):
    #     self.url="http://120.24.68.124:8080/sbborders/cancleorder"
    #     self.data={"reasons":"[{'cancelReason':'天气原因导致行程改变或取消','cancelType':6}]","orderNo":"OP14682247771653"}
    #     asd=requests.post(self.url,self.data)
    #     # new=json.dumps(change, ensure_ascii=False)
    #     print(asd.text)
if __name__ == '__main__':
    unittest.main()
