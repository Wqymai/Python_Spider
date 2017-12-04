import datetime
from selenium import webdriver
import time
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.proxy import ProxyType
from fake_useragent import UserAgent


uas = []
count = 0
ua = UserAgent()
def getRandomUA():
    return ua.random

listIp = []
ipFile = open('xiciIP.txt', 'r')
for line in ipFile.readlines():
    listIp.append(line)
ipFile.close()


year = datetime.datetime.now().year
month = datetime.datetime.now().month
day = datetime.datetime.now().day
end_datetime = datetime.datetime(year, month, day, 21, 30, 0)
for line in listIp:

    if datetime.datetime.now() > end_datetime:
        break

    print 'time is ok...'
    proxies = {}
    list = line.split('\t')
    PROXY = list[0] + ':' + list[1]

    listIp.remove(line)

    print PROXY
    try:
        desired_capabilities = DesiredCapabilities.PHANTOMJS
        desired_capabilities["phantomjs.page.settings.userAgent"] = getRandomUA()
        desired_capabilities["phantomjs.page.settings.loadImages"] = False
        proxy = webdriver.Proxy()
        proxy.proxy_type = ProxyType.MANUAL
        proxy.http_proxy = PROXY
        proxy.add_to_capabilities(desired_capabilities)
        driver = webdriver.PhantomJS(desired_capabilities=desired_capabilities)

        driver.implicitly_wait(5)

        driver.set_page_load_timeout(10)

        driver.set_script_timeout(10)

        driver.get('http://www.anzhi.com/pkg/686d_com.wqy.poems.html')

        # data = driver.page_source

        time.sleep(30)

        driver.find_element_by_css_selector(".detail_down a").click()

        count += 1
        print 'download count : '+str(count)

        time.sleep(30)

        driver.quit()
    except:
        driver.quit()
        print 'except...'





