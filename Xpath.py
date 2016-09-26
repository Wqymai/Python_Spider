#!/usr/bin/env python
# -*- coding: utf-8 -*-
from lxml import etree


text='''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item<span id="myspanid" class="myspanclass"></span></a>
     </ul>
 </div>
 '''
html=etree.HTML(text)
result=etree.tostring(html)
print type(html)
print  result

print "=====获取所用的 li 标签====="
result=html.xpath('//li')
print  result
print  len(result)
print type(result)
print type(result[0])

print "====获取 <li> 标签的所有 class======"
result=html.xpath('//li/@class')
print result

print "====获取 <li> 标签下 href 为 link1.html 的 <a> 标签======="
result=html.xpath('//li/a[@href="link1.html"]')
print  result

print "====获取 <li> 标签下的所有 <span> 标签====="
result=html.xpath('//li//span')
print  result
