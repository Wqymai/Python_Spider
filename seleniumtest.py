import json
import time
from fake_useragent import UserAgent
import datetime
from selenium import webdriver

count = 0
uas = []
ua = UserAgent()
def getRandomUA():
    return ua.random

def saveLog(str):
    if isinstance(str, dict):
        obj = json.dumps(str)
    else:
        obj = str
    with open('/Users/wuqiyan/Documents/shell/log/anzhi-selenium-'+time.strftime('%Y-%m-%d',time.localtime(time.time()))+'.txt', 'a') as f:
        f.write(obj+'\n')

# listIp =[]
# ipFile = open('/Users/wuqiyan/Documents/shell/xiciIP.txt', 'r')
filePath = '/Users/wuqiyan/Documents/shell/xiciIP.txt'
# for line in ipFile.readlines():
#     listIp.append(line)
# ipFile.close()

year = datetime.datetime.now().year
month = datetime.datetime.now().month
day = datetime.datetime.now().day
end_datetime = datetime.datetime(year, month, day, 21, 30, 0)
with open(filePath, 'r') as f:
    for line in f:
        saveLog('current IP is >>> '+line)
        if datetime.datetime.now() > end_datetime:
            saveLog('time is out ... over')
            break
        saveLog('time is ok ...')
        proxies = {}
        list = line.split('\t')
        try:
            chrome_options = webdriver.ChromeOptions()
            # proxy = '--proxy-server='+list[2].replace('\n', '') + '://' + list[0] + ':' + list[1]
            # saveLog proxy
            prefs = {"profile.managed_default_content_settings.images": 2}
            chrome_options.add_experimental_option("prefs", prefs)
            # chrome_options.add_argument(proxy)
            PROXY = list[0] + ':' + list[1]
            saveLog(PROXY)
            desired_capabilities = chrome_options.to_capabilities()
            desired_capabilities['proxy'] = {
                "httpProxy": PROXY,
                "ftpProxy": PROXY,
                "sslProxy": PROXY,
                "noProxy": None,
                "proxyType": "MANUAL",
                "class": "org.openqa.selenium.Proxy",
                "autodetect": False
            }
            chrome_options.add_argument('user-agent="'+getRandomUA()+'"')
            browser = webdriver.Chrome(desired_capabilities=desired_capabilities,executable_path="/Users/wuqiyan/Downloads/PyCharm/seleniumdriver/chromedriver",chrome_options=chrome_options)

            browser.get("http://www.anzhi.com/pkg/686d_com.wqy.poems.html")

            browser.implicitly_wait(5)

            browser.set_page_load_timeout(7)

            browser.set_script_timeout(7)

            browser.find_element_by_css_selector(".detail_down a").click()
            count += 1
            saveLog('download count : '+str(count))
            time.sleep(30)
            saveLog('end time:'+ str(datetime.datetime.now()))
            browser.quit()
        except Exception, e:
            saveLog(repr(e))
            browser.quit()


