import urllib
import  urllib2


proxy="http://120.197.57.244:8000"
# Build ProxyHandler object by given proxy
proxy_support=urllib2.ProxyHandler({'http':proxy})
# Build opener with ProxyHandler object
opener = urllib2.build_opener(proxy_support)
# Install opener to request
urllib2.install_opener(opener)
# Open url
response = urllib2.urlopen('http://www.baidu.com',timeout = 8000)
print  response.read()
