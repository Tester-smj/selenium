# -*- coding: utf-8 -*-
import urllib
import urllib2
import cookielib
import pytesseract
from pytesser import *
from selenium import webdriver

# 二值化
threshold = 140
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
#由于都是数字
#对于识别成字母的 采用该表进行修正
rep={'O':'0',
    'I':'1','L':'1',
    'Z':'2',
    'S':'8'
    };
def verifyImg(picpath):
    #打开图片
    #name=='2.jpg'
    im = Image.open(picpath)
    #转化到灰度图
    imgry = im.convert('L')
    #保存图像
    #imgry.save('g'+name)
    #二值化，采用阈值分割法，threshold为分割点
    out = imgry.point(table,'1')
    #out.save('b'+name)
    #识别
    text =pytesseract.image_to_string(out)
    #识别对吗
    text = text.strip()
    text = text.upper();
    for r in rep:
        text = text.replace(r,rep[r])
    #out.save(text+'.jpg')
    print text
    return text
#注意这里的图片要和此文件在同一个目录，要不就传绝对路径也行
#getverify1('2.jpg')
def login(coo):
    loginUrl = 'http://www.senbaba.cn/joinuspage'
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(loginUrl)
    driver.find_element_by_id("enterpriseName").send_keys(u"测试公司")
    driver.find_element_by_id("enterpriseAddress").send_keys(u"测试地址")
    driver.find_element_by_id("enterprisePhone").send_keys("07558888888")
    driver.find_element_by_id("enterpriseContacts").send_keys(u"测试")
    driver.find_element_by_id("verificationCode").send_keys(randomCode)
    driver.find_element_by_id("sub").click()
    data = {'enterpriseName':'*****', 'enterpriseAddress':'*****', 'enterprisePhone':'*******','enterpriseContacts':'*****','verificationCode':'******'}
    #encode the postData
    postData = urllib.urlencode(data)
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'
    header = {'User-Agent':user_agent,'Referer':'http://www.senbaba.cn/joinuspage'}
    #generate a Request with url,postData headers and cookie
    request = urllib2.Request(loginUrl, postData, headers = header)
    #post data
    content = opener.open(request)
    #get html file
    #mainUrl = 'http://www.senbaba.cn/joinuspage'
    #mainContent = opener.open(mainUrl).read()
    #print mainContent
def getImg(picurl):
    '''
    request for random_code picture and cookie
    '''
    pic = opener.open(picurl).read()
    with open('./2.jpg','wb') as emptyPic:emptyPic.write(pic)
if __name__ == '__main__':
    cookie = cookielib.CookieJar()
    handler = urllib2.HTTPCookieProcessor(cookie)
    opener = urllib2.build_opener(handler)
    picurl = 'http://www.senbaba.cn/jsp/common/validateimage.jsp'
    randomCode = verifyImg("2.jpg")
    login(randomCode)
    getImg(picurl)
    #randomCode = verifyImg("2.jpg")
    #login(randomCode)