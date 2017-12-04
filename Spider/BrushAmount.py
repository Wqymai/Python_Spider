import random

import datetime
import requests
import time
from fake_useragent import UserAgent
from lxml import etree


uas = []
ua = UserAgent()
COUNT = 0


def getHuaweiAppPath():
    return 'http://appdl.hicloud.com/dl/appdl/application/apk/40/40d479b1b6994f4192fbb9a322f4d002/com.wqy.poems.1711171637.apk?sign=portal@portal' + str(
        int(round(time.time() * 1000))) + '&source=portalsite'


def getAnzhiAppPath():
    return 'http://wap.apk.anzhi.com/data1/apk/201711/17/5474a200b656ad5da9bb247e4e6a216d_72467600.apk'


def getBaiduAppPath():
    return 'http://p.gdown.baidu.com/26bff8c70ec8a9fe03d799bd1b3788b91be1d0edb284ea28c50da6739a013287cf0a3617cb2b436a43900b579d7b9dbaf5be4c7817d99d43923c04a9b5808bc7cafb7dd1a6510490e4860d239d4f957f403c681792c8e60c7da338fc228f1363ca534b939376ae7e18b13416460110de889ff1cd6a406d49d588fd6b829a9fa5b9742033e72b07c84dd4e14dc8d7931042d6fee541bc56856fda5349854081396ce510fc615baf1080ff9b24adcea6815d7f8a3b475abc012b6e92190324e676a27806a304dbb9b788f8cc2934aa7159b8420f96f1a4d67c'



# user_agent = [
#     "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
#     "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
#     "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
#     "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
#     "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
#     "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
#     "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
#     "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
#     "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
#     "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
#     "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
#     "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
#     "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
#     "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
#     "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
#     "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
#     "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
#     "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
#     "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
#     "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
#     "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
#     "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
#     "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
#     "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
#     "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
#     "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
#     "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
#     "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
#     "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
#     "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
#     "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
#     "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
#     "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
#     'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
# ]


def downloadBaidu(proxies):
    try:
        print 'start index:', proxies
        baiduIndex = 'http://shouji.baidu.com/s?wd=%E5%A5%BD%E8%AF%97&data_type=app&f=header_all%40input%40btn_search'
        tempUa = getRandomUA()
        print 'get ua:'+tempUa
        headers = {'User-Agent': tempUa}
        session = requests.session()
        r = session.get(baiduIndex,headers=headers,proxies=proxies)
        if r.status_code == 200:
            try:
                timespan = int(round(time.time() * 1000))
                html = etree.HTML(r.text)
                apkUrl = html.xpath('//a[@data_package="com.wqy.poems"]/@data_url')[0]
                logUrl = 'http://shouji.baidu.com/mobres/log?beacon=1&type=install&tj=software_22721345_3250694_%E5%A5%BD%E8%AF%97&f=search_app_%E5%A5%BD%E8%AF%97%40list_1%401%40header_all_input_btn_search&_t='+str(timespan)
                sleeptime = random.randrange(3,20,1)
                print 'sleep time',sleeptime
                time.sleep(sleeptime)
                if session.get(logUrl,headers=headers,proxies=proxies).status_code == 200:
                    try:
                        response = session.get(apkUrl, headers=headers, proxies=proxies)
                        with open('apk/' + str(timespan) + '.apk', 'wb') as code:
                            code.write(response.content)
                        print 'download over'
                    except:
                        print "download error"
                else:
                    print "request logurl error...1"
            except:
                print "request logurl error...0"
        else:
            print "request apkurl error...1"
    except:
        print "request indexurl error...0"




def downloadAnzhi(proxies):
    try:
        print proxies
        global COUNT
        time.sleep(random.randrange(3, 20, 1))
        anzhiFirst = 'http://www.anzhi.com/search.php?keyword=%E5%A5%BD%E8%AF%97'
        tempUa = getRandomUA()
        headers = {'User-Agent': tempUa}
        session = requests.session()
        f = session.get(anzhiFirst, headers=headers, proxies=proxies)
        if f.status_code == 200:
            time.sleep(random.randrange(3, 10, 1))
            anzhiIndex = 'http://www.anzhi.com/ajaxdl_app.php?s=2884633'
            r = session.get(anzhiIndex, headers=headers, proxies=proxies)
            print r.text
            if str(r.text) == '1':
                try:
                    appPath = getAnzhiAppPath()
                    print 'start download:', appPath, " ", proxies
                    response = session.get(appPath, headers=headers, proxies=proxies)
                    if response.status_code == 200:
                        timespan = int(round(time.time() * 1000))
                        with open('apk/' + str(timespan) + '.apk', 'wb') as code:
                            code.write(response.content)
                        COUNT += 1
                        print 'download over '+str(COUNT)

                except:
                    print "except ..."
            else:
                print "except ..."
        else:
            print "except ..."
    except:
        print "except ..."

def brushHuaWei(proxies):
    print proxies
    global COUNT
    tempUa = getRandomUA()
    try:
        headers = {'User-Agent': tempUa}
        time.sleep(random.randrange(3, 25, 1))
        indexUrl ='http://app.hicloud.com/search/%25E5%25A5%25BD%25E8%25AF%2597'
        r = requests.session()
        response = r.get(indexUrl, headers=headers, proxies=proxies, timeout=3)
        if response.status_code == 200:
           time.sleep(random.randrange(2, 10, 1))
           html = etree.HTML(response.text)
           appbtn = html.xpath('//div[@class="app-btn"]/a/@onclick')
           for url in appbtn:
               if 'com.wqy.poems.1711171637' in url:
                   appUrl = str(url.split(',')[5]).replace('\'', '')
                   print appUrl
                   try:
                       print 'start download...'
                       timespan = int(round(time.time() * 1000))
                       out = r.get(appUrl, headers=headers, proxies=proxies, timeout=3)
                       if out.status_code == 200:
                            with open('apk/'+str(timespan)+'.apk', 'wb') as f:
                               f.write(out.content)
                            COUNT += 1
                            uas.append(tempUa)
                            print 'downloading over ' + str(COUNT)
                       else:
                           print 'app url return error...'

                   except:
                       print 'request app url error...'
        else:
            print 'index url return error...'
    except:
        print 'request index url error...'



def getRandomUA():
    exist = True
    count = 0
    while exist:
        useragent = ua.random
        if count > 8:
            print 'ua count > 8,over'
            exist = False
        else:
            if useragent in uas:
                print '...in...no return,continue'
            else:
                print '...not in...return,over'
                exist = False
        count += 1
    return useragent


year = datetime.datetime.now().year
month = datetime.datetime.now().month
day = datetime.datetime.now().day
end_datetime = datetime.datetime(year, month, day, 21, 30, 0)
ipFile = open('xiciIP.txt', 'r')
listIp = []
for line in ipFile.readlines():
    listIp.append(line)
ipFile.close()
for _ in listIp:
    print len(listIp)
    if datetime.datetime.now() < end_datetime:
        print 'time is ok ...'
        proxies = {}
        line = random.choice(listIp)
        list = line.split('\t')
        listIp.remove(line)
        proxies[list[2].replace('\n', '')] = list[2].replace('\n', '') + '://' + list[0] + ':' + list[1]
        brushHuaWei(proxies)
    else:
        print 'time out...'
        break












