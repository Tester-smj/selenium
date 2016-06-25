# coding: utf-8

import urllib2
import re

def get_html(url):
    req = urllib2.urlopen(url)
    content = req.read()
    return content.decode('utf-8').encode('utf-8')

#2.
def search_div(html):
    rp1 = re.compile(r'(.*?)', re.S | re.I)
    m = re.search(rp1, html)
    n = m.group(1)
    print n
    list1 = []
    rp2 = re.compile(r'(.*?)')
    for i in re.finditer(rp2, n):
     list1.append(i.group(1))
    return list1

#3.
def save_result(result):

    f = open('result.txt', 'w')
    for res in result:
        f.write(res+'\n')
    f.close()

    url = 'http://www.soho.com/'
    html = get_html(url)
    data = search_div(html)
    save_result(data)