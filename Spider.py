#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import urllib
import urllib2
import re
import mysql.connector

url = "http://www.qiushibaike.com/hot/page/1/"
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
headers = {'User-Agent' : user_agent}
isFirst=True
try:
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)
    text = response.read()
    numbers = re.findall(r'<span class="dots">[\w\W]*?<span class="page-numbers">\n(\d+)\n</span>', text)
    print '总页数:',numbers[0]
    for number in range(1,int(numbers[0])+1):
           print '当前页数:',number
           newurl = "http://www.qiushibaike.com/hot/page/"+str(number)+"/"
           print '当前请求的地址:',newurl
           req = urllib2.Request(newurl, headers=headers)
           resp = urllib2.urlopen(req)
           newtext = resp.read()
           contents = re.findall(r'<h2>(.*?)</h2>[\w\W].*\n</div>\n\n\n<div class="content">\n\n(.*?)\n\n</div>[\w\W]*?<div class="stats">\n<span class="stats-vote"><i class="number">(\d+?)</i> 好笑</span>[\w\W]*?<span class="stats-comments">[\w\W]*?>(\d*?)<[\w\W]*?</span>',newtext)
           conn = mysql.connector.connect(user='root', database='Spider')
           cursor = conn.cursor()
           for content in contents:
               # print '=作者=',content[0],'=内容=',content[1],'=好笑=',content[2],'=评论=',content[3]
               cursor.execute('insert into QSBK (author,content,hx,comments) value (%s, %s,%s,%s)',
                              [content[0], content[1], content[2], content[3]])
               conn.commit()

    cursor.close()
except Exception as e:
    print e
