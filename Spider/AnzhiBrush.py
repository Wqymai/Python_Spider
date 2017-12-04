import json
import random
import datetime
import requests
import time
from fake_useragent import UserAgent
import os


uas = []
ua = UserAgent()
COUNT = 0


def saveLog(str):
    if isinstance(str, dict):
        obj = json.dumps(str)
    else:
        obj = str
    with open('/Users/wuqiyan/Documents/shell/anzhi-normal-'+time.strftime('%Y-%m-%d',time.localtime(time.time()))+'.txt', 'a') as f:
        f.write(obj+'\n')

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


def downloadAnzhi(proxies):
    try:
        saveLog(proxies)
        global COUNT
        time.sleep(random.randrange(3, 20, 1))
        headers = {'User-Agent': getRandomUA()}
        session = requests.session()
        anzhiIndex = 'http://www.anzhi.com/ajaxdl_app.php?s=2884633'
        r = session.get(anzhiIndex, headers=headers, proxies=proxies, timeout=3)
        if str(r.text) == '1':
            try:
                appPath = 'http://wap.apk.anzhi.com/data1/apk/201711/17/5474a200b656ad5da9bb247e4e6a216d_72467600.apk'
                saveLog('start download:'+appPath)
                response = session.get(appPath, headers=headers, proxies=proxies, timeout=3)
                if response.status_code == 200:
                    timespan = int(round(time.time() * 1000))
                    savepath = '/Users/wuqiyan/Documents/shell/apk/' + str(timespan) + '.apk'
                    with open(savepath, 'wb') as f:
                        f.write(response.content)
                    COUNT += 1
                    saveLog('download over '+str(COUNT))
                    os.remove(savepath)

            except Exception, e:
                repr(e)
        else:
            saveLog("except ...")
    except Exception, e:
        repr(e)

year = datetime.datetime.now().year
month = datetime.datetime.now().month
day = datetime.datetime.now().day
end_datetime = datetime.datetime(year, month, day, 21, 30, 0)
ipFile = open('/Users/wuqiyan/Documents/shell/xiciIP.txt', 'r')
listIp = []
for line in ipFile.readlines():
    listIp.append(line)
ipFile.close()
for _ in listIp:
    saveLog(str(len(listIp)))
    if datetime.datetime.now() < end_datetime:
        saveLog('time is ok ...')
        proxies = {}
        line = random.choice(listIp)
        list = line.split('\t')
        listIp.remove(line)
        proxies[list[2].replace('\n', '')] = list[2].replace('\n', '') + '://' + list[0] + ':' + list[1]
        downloadAnzhi(proxies)
    else:
        saveLog('time out...')
        break