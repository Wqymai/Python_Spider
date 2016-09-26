#!/usr/bin/env python
# -*- coding: utf-8 -*-
import mysql.connector
conn = mysql.connector.connect(user='root', database='test')
cursor = conn.cursor()
cursor.execute('select * from student')
values = cursor.fetchall()
for row in values:
    id = row[0]
    name = row[1]
    print id, name