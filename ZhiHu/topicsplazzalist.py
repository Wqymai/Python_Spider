#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
import urllib2
import urllib
from bs4 import BeautifulSoup
import  random
import  time
import mysql.connector

url='https://www.zhihu.com/node/TopicsPlazzaListV2'
list=[]
offset=0
user_agent = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
    "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
]
conn = mysql.connector.connect(user='root', database='Spider')
cursor = conn.cursor()
proxies = {
    'https': 'https://113.128.132.44:8123',
}
proxies1 = {
    'https': 'https://223.67.136.218:80',
}
proxies2 = {
    'https': 'https://117.83.39.76:8080',
}
#========获取话题分类==============================
# headers={'User-Agent':user_agent[index]}
# txt=requests.get('https://www.zhihu.com/topics',proxies=proxies1,headers=headers)
# soup = BeautifulSoup(txt.text, "lxml")
# response = soup.select("ul.zm-topic-cat-main > li")
# for r in response:
#     topic_id= r['data-id']
#     topic_category=r.select('a')[0].string
#     cursor.execute('insert into CATEGORY (categoryid,categoryname) value (%s, %s)', [unicode(topic_id), unicode(topic_category)])
#     conn.commit()
# cursor.close()
#========获取话题分类==============================

cursor.execute('select * from CATEGORY')
for query in cursor:
    list.append(query)
conn.close()

for l in list:
    autoid=l[0]
    cid   =l[1]
    cname =l[2]
    print 'id==', autoid, 'cid==', cid, 'cname==', cname
    while offset < 800:
       index = random.randrange(0, 35, 1)
       timespan = random.randrange(5, 20, 1)
       time.sleep(timespan)
       if cid <> 253:
         s_user_agent= user_agent[index]
         params='{"topic_id":%s,"offset":%s,"hash_id":"d2b42b8373130739a91394e96c4d9c46"}'%[cid,offset]
         headers={'Connection':'keep-alive','Accept':'*/*','Origin':'https://www.zhihu.com','X-Requested-With':'XMLHttpRequest','X-Xsrftoken':'ba86ed1e1c541ab8d7fa43e4d14fd848','User-Agent':s_user_agent,'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8','Referer':'https://www.zhihu.com/','Accept-Encoding':'gzip, deflate, br','Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6','Cookie':'_za=1d4f1623-91b1-41a6-b118-373eb932f390; _zap=96976460-3573-4878-aa05-a331467f870b; cap_id="NDNkMjBiNmQ3NjRlNGQxNmI0NjRjMmNlZDZiMjNmODE=|1471942866|2a9c9ec457aa1c67a57b493e0f40f381be2cc184"; d_c0="AEBAqBi8bQqPTusp0Xt0CkahsDN7B_9jF78=|1471942866"; l_cap_id="YzI2ODViNmNiMjI2NDU4NmIyMzQxMmZlYmVlNzI0MDU=|1471942866|b5aebcfaf3d2acf94a98423564320f3fbafc2ad2"; l_n_c=1; n_c=1; q_c1=7ee80390f41b4b7c95b74b5e5e003511|1471942866000|1471942866000','Host':'www.zhihu.com'}
         data={'params':params,'method':'next'}
         s = requests.session()
         r=s.post(url=url,data=data,headers=headers,proxies=proxies1)
         print r.text
         s = json.loads(r.text)
         content= s['msg']
         if len(content)>0:
            for c in content:
                 soup = BeautifulSoup(c,'html5lib')
                 tname=  soup.strong.string
                 summary= soup.p.string
                 turl =soup.a['href']
                 print tname,'--',turl,'--',summary,'--',offset
                 # print type(unicode(tname)), '--', type(turl), '--', type(summary), '--',type(offset)
                 cursor.execute('insert into TOPIC (tname,url,summary,status,offset,category) value (%s, %s, %s, %s, %s)', [unicode(tname), unicode(turl), unicode(summary), '0',str(offset),str(cname)])
                 conn.commit()
            offset = offset + 20
            print offset
         else:
             break

cursor.close()

