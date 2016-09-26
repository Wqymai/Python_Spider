#!/usr/bin/env python
# -*- coding: utf-8 -*-

import  requests
import re
import json

def saveTxt(content):
    file_name = "/Users/wuqiyan/Downloads/PyCharm/ZhiHu/cookies.txt"
    f = open(file_name, "w+")
    f.write(content.encode('utf-8'))
    f.close()


url='https://www.zhihu.com/login/email'
proxies = {
    'https':'https://36.234.170.73:8080',
}
# headers={'Host':'www.zhihu.com','Connection':'keep-alive','Accept':'*/*','Origin':'https://www.zhihu.com','X-Requested-With':'XMLHttpRequest','X-Xsrftoken':'ba86ed1e1c541ab8d7fa43e4d14fd848','User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36','Content-Type':'application/x-www-form-urlencoded; charset=UTF-8','Referer':'https://www.zhihu.com/question/28385432','Accept-Encoding':'gzip, deflate, br','Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6','Cookie':' d_c0="AICAD2hZwgmPTtpxdNNGWz66AB0SQO_LPyU=|1460441377"; _za=49253c39-81bc-4dad-99f9-24fe67e58d94; _zap=bd72b431-0501-477f-8d4d-89cbe315abce; _xsrf=ba86ed1e1c541ab8d7fa43e4d14fd848; q_c1=72d9c332d3e34bedb6b742e5724565d9|1471770533000|1471770533000; l_n_c=1; login="YzdhMjlhOGUzMjExNGYzZWE3YTdkZWU1Y2QwODFiMTE=|1471852882|8174118435e33cbfe2c3971c470d9e98b2d0421c"; l_cap_id="OThjZDc1OGE0YmQwNDQzNDljYjk1NzI3MzcyMTRlZmE=|1471855483|545f681105d5f539b7ffc7702de52d2605eec687"; cap_id="NmYzNzI4YmVlMzU2NGYxYTk4NWNlOTcyZjliZGUxODE=|1471855626|64fb15a8ce2dce1e4e036bfc8adb9f06040c142c"; __utmt=1; __utma=51854390.471154460.1471758859.1471852907.1471855626.9; __utmb=51854390.2.10.1471855626; __utmc=51854390; __utmz=51854390.1471855626.9.6.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/question/28385432; __utmv=51854390.000--|2=registration_date=20150522=1^3=entry_date=20160821=1; n_c=1'}
headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 '}
data={'password':'921126wqydezh','remember_me':'true','email':'2367482229@qq.com','_xsrf':'ba86ed1e1c541ab8d7fa43e4d14fd848'}
s = requests.session()
r=s.post(url,data=data,headers=headers)

x= json.loads(r.text)
print x['msg']

request_cookie=''

for cookie in r.cookies:
     c= re.findall(r'<Cookie\s(.*?)\sfor\s.zhihu.com/>',str(cookie))
     request_cookie+=c[0]+';'

other='d_c0="AICAD2hZwgmPTtpxdNNGWz66AB0SQO_LPyU=|1460441377";_za=49253c39-81bc-4dad-99f9-24fe67e58d94;_zap=bd72b431-0501-477f-8d4d-89cbe315abce;_xsrf=ba86ed1e1c541ab8d7fa43e4d14fd848;__utma=51854390.585792142.1472435505.1472550444.1472623680.5;__utmc=51854390;__utmz=51854390.1472550444.4.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic;__utmv=51854390.100--|2=registration_date=20150522=1^3=entry_date=20150522=1'
total_cookies= request_cookie+other
#把cookies保存到本地
saveTxt(total_cookies)
print total_cookies
headers2={'Host':'www.zhihu.com','Connection':'keep-alive','Accept':'*/*','Origin':'https://www.zhihu.com','X-Requested-With':'XMLHttpRequest','X-Xsrftoken':'ba86ed1e1c541ab8d7fa43e4d14fd848','User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36','Content-Type':'application/x-www-form-urlencoded; charset=UTF-8','Referer':'https://www.zhihu.com/question/28385432','Accept-Encoding':'gzip, deflate, br','Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6','Cookie':total_cookies}
params={'params':'{"offset":20,"start":"19"}','method':'next'}
g=s.post('https://www.zhihu.com/node/TopStory2FeedList',headers=headers,data=params)
print g
# for t in json.loads(g.text)['msg']:
#     print t




