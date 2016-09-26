#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import re
import urllib2
import mysql.connector

url='http://www.66ip.cn/nmtq.php?getnum=200&isp=0&anonymoustype=3&start=&ports=&export=&ipaddress=&area=1&proxytype=1&api=66ip'
requests.adapters.DEFAULT_RETRIES = 5
response=requests.get(url)
ips = re.findall(r'(\d+.\d+.\d+.\d+):(\d+)',response.text)
conn = mysql.connector.connect(user='root', database='Spider')
cursor = conn.cursor()
for ip in ips:
    print ip[0],ip[1]
    cursor.execute('insert into Proxy (ip,port,iptype,status) value (%s, %s, %s, %s)',[ip[0], ip[1], 'https', 0])
    conn.commit()
cursor.close()

