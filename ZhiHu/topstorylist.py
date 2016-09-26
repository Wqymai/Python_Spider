#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
import urllib2
import urllib

url='https://www.zhihu.com/node/TopStory2FeedList'
# Connection: keep-alive
# Accept: */*
# Origin: https://www.zhihu.com
# X-Requested-With: XMLHttpRequest
# X-Xsrftoken: ba86ed1e1c541ab8d7fa43e4d14fd848
# User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36
# Content-Type: application/x-www-form-urlencoded; charset=UTF-8
# Referer: https://www.zhihu.com/
# Accept-Encoding: gzip, deflate, br
# # Accept-Language: zh-CN,zh;q=0.8,en;q=0.6
# Cookie:  d_c0="AICAD2hZwgmPTtpxdNNGWz66AB0SQO_LPyU=|1460441377"; _za=49253c39-81bc-4dad-99f9-24fe67e58d94; _zap=bd72b431-0501-477f-8d4d-89cbe315abce; _xsrf=ba86ed1e1c541ab8d7fa43e4d14fd848; q_c1=72d9c332d3e34bedb6b742e5724565d9|1471770533000|1471770533000; l_n_c=1; l_cap_id="OThjZDc1OGE0YmQwNDQzNDljYjk1NzI3MzcyMTRlZmE=|1471855483|545f681105d5f539b7ffc7702de52d2605eec687"; cap_id="NmYzNzI4YmVlMzU2NGYxYTk4NWNlOTcyZjliZGUxODE=|1471855626|64fb15a8ce2dce1e4e036bfc8adb9f06040c142c"; __utmt=1; login="YWRkZjQ0Nzk0NGRkNDllMzkzODA1NzNlYjgzN2NiZWQ=|1471855645|e4037826de17539a69f5dc7cef00a9dccd3f9ebe"; __utma=51854390.471154460.1471758859.1471852907.1471855626.9; __utmb=51854390.7.9.1471855760400; __utmc=51854390; __utmz=51854390.1471855626.9.6.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/question/28385432; __utmv=51854390.100--|2=registration_date=20150522=1^3=entry_date=20150522=1; a_t="2.0ABBCimhiHggXAAAAlEniVwAQQopoYh4IAICAD2hZwgkXAAAAYQJVTR5J4lcADNSgJ1sjH9ebKilUWic5rpbzKNmGqySt0Sw6h3uxXE8DLZCD70n5VA=="; z_c0=Mi4wQUJCQ2ltaGlIZ2dBZ0lBUGFGbkNDUmNBQUFCaEFsVk5Ia25pVndBTTFLQW5XeU1mMTVzcUtWUmFKem11bHZNbzJR|1471855764|d2b3f76e43610c1be2ee4d2cee00f6a6c1051394
# Host: www.zhihu.com

headers={'Connection':'keep-alive','Accept':'*/*','Origin':'https://www.zhihu.com','X-Requested-With':'XMLHttpRequest','X-Xsrftoken':'ba86ed1e1c541ab8d7fa43e4d14fd848','User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36','Content-Type':'application/x-www-form-urlencoded; charset=UTF-8','Referer':'https://www.zhihu.com/','Accept-Encoding':'gzip, deflate, br','Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6','Cookie':' d_c0="AICAD2hZwgmPTtpxdNNGWz66AB0SQO_LPyU=|1460441377"; _za=49253c39-81bc-4dad-99f9-24fe67e58d94; _zap=bd72b431-0501-477f-8d4d-89cbe315abce; _xsrf=ba86ed1e1c541ab8d7fa43e4d14fd848; l_n_c=1; q_c1=99b53cc93b5b4811b4c46527f9367907|1471942754000|1471942754000; cap_id="MTI5YjJjOWZmODY1NGY0MjgyNmMxNjA4NjY3ZjkwZDU=|1471942754|fbf6cb3ab6cede0d77e1659a9fde8b3dedf81973"; l_cap_id="OWE0ZGI2MmVkYTU5NDQwNTlkOWQzMWJjNjYwNTIzMmE=|1471942754|94132cce7cb751e4dad012a1d41fa2e56769a56b"; login="NDYwMjBjMTUwOTFkNGI5NGFlMzQyOWZiNDM1YzAyZDY=|1471942767|59129d899ee005651e185dc4b425763dcd01c954"; __utma=51854390.1758560404.1471933262.1471940903.1471947448.4; __utmb=51854390.4.10.1471947448; __utmc=51854390; __utmz=51854390.1471933262.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmv=51854390.100--|2=registration_date=20150522=1^3=entry_date=20150522=1; a_t="2.0ABBCimhiHggXAAAArLbjVwAQQopoYh4IAICAD2hZwgkXAAAAYQJVTW-d41cAJHJqfHMGMjlwNfnK1T6MF2hDDVuGR-5r1riaRGas0fSHcbYxzt116A=="; z_c0=Mi4wQUJCQ2ltaGlIZ2dBZ0lBUGFGbkNDUmNBQUFCaEFsVk5iNTNqVndBa2NtcDhjd1l5T1hBMS1jclZQb3dYYUVNTld3|1471949228|08a19c35330c78bf77407d1fd31a351a5a9c7e5b','Host':'www.zhihu.com'}
data={'params':'{"offset":10,"start":"-1"}','method':'next'}
proxies = {
    'https':'https://1.161.153.3:8080',

}
s = requests.session()
r=s.post(url=url,data=data,headers=headers,proxies=proxies,verify=True)

s = json.loads(r.text)
print s['msg'][0]

# request = urllib2.Request(url,urllib.urlencode(data),headers)
# proxy =  'http://124.193.9.6:3128'
# proxy_support = urllib2.ProxyHandler({'http': proxy})
# opener = urllib2.build_opener(proxy_support)
# urllib2.install_opener(opener)
# response = urllib2.urlopen(request)
# print  response.read()

# request = urllib2.Request(url,urllib.urlencode(data),headers)
#
# request.set_proxy('124.193.9.6:3128','http')
# conn = urllib2.urlopen(request)
# print conn.read()

# s = json.loads(r.text)
# print s['msg'][0]