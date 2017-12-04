import requests
from lxml import etree

url = 'http://www.xicidaili.com/nn/'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
response = requests.get(url, headers=headers)
trs =  etree.HTML(response.text).xpath('//tr[@class="odd"]')
for tr in trs:
    print tr.xpath('./td[2]/text()')


