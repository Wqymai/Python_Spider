#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup

soup = BeautifulSoup(open('source.html'), "lxml")
print soup.prettify()

response = soup.select("div.article")
count = 0
for con in response:
    author = con.select(".author > a > h2") #作者
    if len(author) <= 0:
        author = con.select(".author > span > h2")
    content = con.select(".content") #内容
    hx = con.select(".stats > span.stats-vote > i")  #好笑
    com = con.select(".stats > span.stats-comments > a > i") #评论
    if len(com) > 0:
       print author[0].string, content[0].string, hx[0].string, com[0].string
    else:
        print author[0].string, content[0].string, hx[0].string

    count = count+1
print count