#!/usr/bin/env python
# -*- coding: gb2312 -*-
from CheckProxy import CheckProxy
import  time
from CheckProxy02 import CheckProxy02
import mysql.connector
protocol="https"
# list=[]
# proxy=CheckProxy02()
# conn = mysql.connector.connect(user='root', database='Spider')
# cursor = conn.cursor()
# cursor.execute('select * from Proxy where id >= 787')
# for query in cursor:
#     list.append(query)
# conn.close()
#
# print  len(list)
# for l in list:
#     id=l[0]
#     ip=l[1]
#     port=l[2]
#     print 'id==', id, 'ip==', ip, 'port==', port
#     conn = mysql.connector.connect(user='root', database='Spider')
#     cursor = conn.cursor()
#     res=proxy.check_proxy(protocol,ip,port)
#     print res
#     if res == True:
#       print 'success'
#       cursor.execute('update Proxy set status=%s where id=%s',['1',id])
#       conn.commit()
#     else:
#       cursor.execute('update Proxy set status=%s where id=%s', ['0', id])
#       conn.commit()
# conn.close()


#
# 842
proxy02=CheckProxy02()
print proxy02.check_proxy('https','218.5.238.206','80')