import random
import os
import datetime
import requests
import time
from fake_useragent import UserAgent
from lxml import etree
import json


uas = []
ua = UserAgent()
COUNT = 0

def saveLog(str):
    if isinstance(str, dict):
        obj = json.dumps(str)
    else:
        obj = str
    with open('/Users/wuqiyan/Documents/shell/log/huawei-' + time.strftime('%Y-%m-%d', time.localtime(
            time.time())) + '.txt', 'a') as f:
        f.write(obj + '\n')

def getRandomUA():
    exist = True
    count = 0
    while exist:
        useragent = ua.random
        if count > 8:
            saveLog('ua count > 8,over')
            exist = False
        else:
            if useragent in uas:

                saveLog('...in...no return,continue')
            else:
                saveLog('...not in...return,over')
                exist = False
        count += 1
    return useragent


def brushHuaWei(proxies):
    saveLog(proxies)
    global COUNT
    tempUa = getRandomUA()
    try:
        headers = {'User-Agent': tempUa}
        time.sleep(random.randrange(3, 25, 1))
        indexUrl = 'http://app.hicloud.com/app/C100132421'
        r = requests.session()
        response = r.get(indexUrl, headers=headers,proxies=proxies, timeout=10)
        if response.status_code == 200:
           time.sleep(random.randrange(2, 10, 1))
           html = etree.HTML(response.text)
           appbtn = html.xpath('//a[@class="mkapp-btn mab-download"]/@onclick')
           for url in appbtn:
               if 'com.wqy.poems' in url:
                   appUrl = str(url.split(',')[5]).replace('\'', '')
                   saveLog('app download url:'+appUrl.strip())
                   try:
                       saveLog('start download...')
                       out = r.get(appUrl.strip(), headers=headers,proxies=proxies, timeout=10)
                       timespan = int(round(time.time() * 1000))
                       savepath = '/Users/wuqiyan/Documents/shell/apk/'+str(timespan)+'.apk'
                       if out.status_code == 200:
                            with open(savepath, 'wb') as f:
                               f.write(out.content)
                            COUNT += 1
                            uas.append(tempUa)
                            saveLog('downloading over ' + str(COUNT))
                            os.remove(savepath)
                       else:
                           saveLog('app url return error...')
                   except Exception, e:
                       saveLog(repr(e))
        else:
            saveLog('index url return error...')
    except Exception, e:
        saveLog(repr(e))



year = datetime.datetime.now().year
month = datetime.datetime.now().month
day = datetime.datetime.now().day
end_datetime = datetime.datetime(year, month, day, 21, 30, 0)
filePath = '/Users/wuqiyan/Documents/shell/xiciIP.txt'
with open(filePath,'r') as f:
    for line in f:
        saveLog('current IP is >>> '+line)
        if datetime.datetime.now() < end_datetime:
            saveLog('time is ok ...')
            proxies = {}
            list = line.split('\t')
            listIp.remove(line)
            proxies[list[2].replace('\n', '')] = list[2].replace('\n', '') + '://' + list[0] + ':' + list[1]
            brushHuaWei(proxies)
        else:
            saveLog('time out...')
            break
# ipFile = open('/Users/wuqiyan/Documents/shell/xiciIP.txt', 'r')
# listIp = []
# for line in ipFile.readlines():
#     listIp.append(line)
# ipFile.close()
# for _ in listIp:
#     saveLog(str(len(listIp)))
#     if datetime.datetime.now() < end_datetime:
#         saveLog('time is ok ...')
#         proxies = {}
#         line = random.choice(listIp)
#         list = line.split('\t')
#         listIp.remove(line)
#         proxies[list[2].replace('\n', '')] = list[2].replace('\n', '') + '://' + list[0] + ':' + list[1]
#         brushHuaWei(proxies)
#     else:
#         saveLog('time out...')
#         break