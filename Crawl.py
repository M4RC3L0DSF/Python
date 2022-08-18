#!/usr/bin/python3

import urllib.request
import re

data = {}
data = ['fromUrl']=''
user_agent='Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'

url='Target'
postdata = urllib.parse.urlencode(data)
postdata = postdata.encode('utf-8')
header = ('User-Agent' : user_agent)
res = urllib.request.urlopen(url)
strResult = (res.read().decode('ISO-8859-1'))
 
p - re.compile(r'<a href="(.*?)".*?>(.*?)</a>')

for m in p.finditer(strResult):
    print(m.group(1))