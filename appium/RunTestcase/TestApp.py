#coding=utf-8
import HTMLTestRunner
import sys
import unittest
from CommenMethod import Method
from Testcase import Login
from Testcase import Logout
from Testcase import Enterprises

class SenbabaApp(unittest.TestCase):
    def setUp(self):
        Login.login(self)

    def test_axiadan(self):
        u"""用户下单"""
        Method.method(self)

    def test_logout(self):
        u"""退出"""
        Logout.logout(self)

    def test_enterprises(self):
        """企业加入"""
        Enterprises.enterprises(self)

if __name__ == "__main__":
    #防止编码格式报错
    reload(sys)
    sys.setdefaultencoding('utf8')
    suite = unittest.TestSuite()
    suite.addTest(SenbabaApp("test_axiadan"))
    suite.addTest(SenbabaApp("test_logout"))
    #suite.addTest(SenbabaApp("test_gentuan"))
    #suite.addTest(SenbabaApp("test_guojing"))
    #suite.addTest(SenbabaApp("test_enterprise"))
    #suite.addTest(SenbabaApp("test_loginout"))
    filename='F:\\test_case\\erro_png\\APPtestresult.html'
    fp=file(filename,'wb')
    runner =HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u'下单平台app测试报告',
        description=u'用例执行情况：')
    runner.run(suite)


