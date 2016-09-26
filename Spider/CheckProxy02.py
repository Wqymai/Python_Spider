import requests


class CheckProxy02:
       def check_proxy(self,protocol, ip, port):
           try:
             requests.adapters.DEFAULT_RETRIES = 5
             s = requests.session()
             s.keep_alive = False
             proxies = {
               protocol: protocol+"://"+ip+":"+port
             }
             r=s.get("https://tumutanzi.com/", proxies=proxies,verify=True)
             if r.status_code==200:
                 return True
           except Exception,detail:
               print 'ERROR:', detail
               return False