#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import mysql.connector
# from bs4 import BeautifulSoup
#
# soup = BeautifulSoup(open('iplist.txt'), "lxml")
#
# print soup.prettify()

file_object = open('iplist.txt')
all_the_text = file_object.read()
ips = re.findall(r'(\d+.\d+.\d+.\d+):(\d+)',all_the_text)
conn = mysql.connector.connect(user='root', database='Spider')
cursor = conn.cursor()
for ip in ips:
    print ip[0],ip[1]
    cursor.execute('insert into Proxy (ip,port,iptype,status) value (%s, %s, %s, %s)',[ip[0], ip[1], 'http', 0])
    conn.commit()
cursor.close()