# -*- coding: utf-8 -*-
from selenium.webdriver.support.ui import WebDriverWait
import method
import runtestcase

def timewait(self):
    values=['fromDate','capaSel','fromCity','fromAi','page1Next']
    browser=self.browser
    element=WebDriverWait(browser,10).until(lambda x:x.find_element_by_id(values))
    is_disappeared=WebDriverWait(browser,30,1,(ElementNotVisibleException)).until_not(lambda x:x.find_element_by_id(values).is_displayed())