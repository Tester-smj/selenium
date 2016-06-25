# -*- coding: utf-8 -*-
import HTMLTestRunner
import sys
import unittest
import test11
from Testcase import Guojing, Register, Enterprises,Jiesong,Login,Jargon,Gentuan,Loginout,Myorder,FixedPrice

class Senbaba(unittest.TestCase):
    def setUp(self):
        Login.login(self)

    def test_jiesong(self):
        u"""接送类型下单"""
        Jiesong.jiesong(self)

    def test_gentuan(self):
        u"""跟团类型下单"""
        Gentuan.gentuan(self)

    def test_guojing(self):
        u"""过境类型下单"""
        Guojing.guojing(self)

    def test_enterprise(self):
        u"""企业加入"""
        Enterprises.enterprises(self)

    def test_loginout(self):
        u"""用户退出"""
        Loginout.loginout(self)

    def test_myoder(self):
        u"""我的订单"""
        Myorder.myorder(self)

    def test_regist(self):
        u"""用户注册"""
        Register.regist(self)

    def test_jargon(self):
        u"""黑话下单"""
        Jargon.jargon(self)

    def test_fixedpice(self):
        u"""固定路线价格"""
        FixedPrice.fixedprice(self)

    def tearDown(self):
        self.browser.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    reload(sys)
    sys.setdefaultencoding('utf8')
    #构造测试集
    suite = unittest.TestSuite()
    suite.addTest(Senbaba("test_jiesong"))
    suite.addTest(Senbaba("test_gentuan"))
    suite.addTest(Senbaba("test_guojing"))
    suite.addTest(Senbaba("test_enterprise"))
    suite.addTest(Senbaba("test_loginout"))
    suite.addTest(Senbaba("test_myoder"))
    suite.addTest(Senbaba("test_regist"))
    filename='F:\\test_case\\erro_png\\webresult.html'
    fp=file(filename,'wb')
    #执行测试
    runner =HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u'下单平台web测试报告',
        description=u'用例执行情况：')
    runner.run(suite)