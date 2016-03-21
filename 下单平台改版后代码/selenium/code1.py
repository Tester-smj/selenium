# -*- coding: utf-8 -*-
import urllib
import time
from selenium import webdriver

class Crawler:
    def __init__(self):
        self.url ='http://www.senbaba.cn/jsp/common/validateimage.jsp'
        self.img_xpath = '//ul/li/div/a/img'
        self.download_xpath = '//ul/li/div/div/span/a[@class="downloadicon"]'
        self.img_url_dic = {}

    def launch(self):
        driver = webdriver.Chrome(r"c:/python27/chromedriver.exe")
        driver.maximize_window()
        driver.get(self.url)
        img_xpath = self.img_xpath
        download_xpath = self.download_xpath
        img_url_dic = self.img_url_dic


if __name__ == '__main__':
    crawler = Crawler()
    crawler.launch()