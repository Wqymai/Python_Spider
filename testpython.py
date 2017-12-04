import datetime
import time

year = datetime.datetime.now().year
month = datetime.datetime.now().month
day = datetime.datetime.now().day


def saveLog(str):
    with open(time.strftime('%Y-%m-%d',time.localtime(time.time()))+'.txt','a') as f:
        f.write(str+'\n')

saveLog('fail...')
