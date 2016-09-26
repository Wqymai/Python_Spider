#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import re
class CheckProxy:
  def __init__(self):
      # http://1212.ip138.com/ic.asp  gb2312
      # http://icanhazip.com
      self.ip_check_url = "http://www.baidu.com"

  def check_proxy(self,protocol, ip, port):
    try:
        proxy = protocol+'://'+ip+':'+port
        proxy_support = urllib2.ProxyHandler({protocol: proxy})
        opener = urllib2.build_opener(proxy_support)
        urllib2.install_opener(opener)
        response = urllib2.urlopen(self.ip_check_url, timeout=10000)
        if response.getcode()==200:
            return True
        # result = re.findall(r'百度一下，你就知道',response.read())
        # if len(result) > 0:
        #     return True
        # else:
        #     return False
    except Exception, detail:
        print 'ERROR:', detail
        return False
        # return False
    # finally:
    #     if response:
    #      response.close()
