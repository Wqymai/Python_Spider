from lxml import etree
import requests
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
savefile = open('/Users/wuqiyan/Documents/shell/xiciIP.txt', 'w')
for page in range(1, 20):
        try:
                url = 'http://www.xicidaili.com/nn/' + str(page)
                print url
                response = requests.get(url, headers=headers)
                html = etree.HTML(response.text)
                trs = html.xpath("//table[@id='ip_list']/tr")
                for i in range(0,len(trs)):
                        if i == 0:
                                continue
                        ip = trs[i].xpath('./td[2]/text()')[0]
                        port = trs[i].xpath('./td[3]/text()')[0]
                        type = trs[i].xpath('./td[6]/text()')[0]
                        line = ip+'\t'+port+'\t'+type.lower()+'\n'
                        savefile.write(line)
        except:
                print 'except...'

savefile.close()












