# import urllib2
# response = urllib2.urlopen('http://www.baidu.com/')
# html = response.read()
# print html

# -*- coding: utf-8 -*-
import urllib2
import urllib
# req = urllib2.Request('http://www.ebay.com')
# response = urllib2.urlopen(req)
# the_page = response.read()
# print the_page

def save_result(result):
    f = open('result.txt', 'w')
    for res in result:
        f.write(res+'\n')
    f.close()

url='http://www.ebay.com/sch/i.html'
values = {'_odkw' : 'arabic-tv-iptv-box',
          '_osacat' : '0',
          '_from' : 'R40',
          '_trksid': 'p2045573.m570.l1313.TR0.TRC0.H0.TRS0',
          '_nkw' : 'arabic-tv-iptv-box',
          '_sacat' : '0'
          }
data = urllib.urlencode(values)
req = urllib2.Request(url, data)
response = urllib2.urlopen(req)

result = response.read()
save_result(result)
print result