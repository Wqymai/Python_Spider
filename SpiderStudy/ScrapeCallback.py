# -*- coding: utf-8 -*-

import csv
import re
import urlparse
import lxml.html
from SpiderTest import link_crawler



class ScrapeCallback:
    print '来ScrapeCallback啦!'
    def __init__(self):
        self.writer = csv.writer(open('countries.csv', 'w'))
        self.fields = ('area', 'population', 'iso', 'country', 'capital', 'continent', 'tld', 'currency_code', 'currency_name', 'phone', 'postal_code_format', 'postal_code_regex', 'languages', 'neighbours')
        self.writer.writerow(self.fields)

    def __call__(self, url, html):
        print '回调中:',url
        if re.search('/view/', url):
            tree = lxml.html.fromstring(html)
            row = []
            for field in self.fields:
                row.append(tree.cssselect('table > tr#places_{}__row > td.w2p_fw'.format(field))[0].text_content())
            self.writer.writerow(row)
        else:
            print '回调 不匹配'

if __name__ == '__main__':
    link_crawler('http://example.webscraping.com/', '/(index|view)', scrape_callback=ScrapeCallback())