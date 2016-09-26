#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import re
import itertools
import urlparse
import robotparser
from Throttle import  Throttle
import Queue



def download(url, headers, proxy=None, num_retries=2, data=None):
    print 'Downloading:', url
    request = urllib2.Request(url, data, headers)
    opener = urllib2.build_opener()
    if proxy:
        proxy_params = {urlparse.urlparse(url).scheme: proxy}
        opener.add_handler(urllib2.ProxyHandler(proxy_params))
    try:
        response = opener.open(request)
        html = response.read()
        code = response.code
    except urllib2.URLError as e:
        print 'Download error:', e.reason
        html = ''
        if hasattr(e, 'code'):
            code = e.code
            if num_retries > 0 and 500 <= code < 600:
                return download(url, headers, proxy, num_retries - 1, data)
        else:
            code = None
    return html

def crawl_sitmap(url):
    sitemap = download(url)
    links = re.findall('<loc>(.*?)</loc>',sitemap)
    for link in links:
        html = download(link)

# max_errors = 5
# num_errors = 0
#
# for page in itertools.count(1):
#     url = 'http://example.webscraping.com/view/-%d' % page
#     html = download(url)
#     if html is None:
#         num_errors += 1
#         if num_errors == max_errors:
#           break
#     else:
#         num_errors = 0




def link_crawler(seed_url, link_regex=None, delay=0, max_depth=-1,max_urls=-1, headers=None, user_agent='wswp', proxy=None, num_retries=1,scrape_callback=None):

    crawl_queue = Queue.deque([seed_url])
    print 'crawl_queue==为:', crawl_queue
    seen = {seed_url: 0}
    print 'seen为:', seen
    num_urls = 0
    rp = get_robots(seed_url)
    throttle = Throttle(delay)
    headers = headers or {}

    if user_agent:
        headers['User-agent'] = user_agent

    while crawl_queue:
        url = crawl_queue.pop()
        print 'url为:', url
        if rp.can_fetch(user_agent, url):
            throttle.wait(url)
            html = download(url, headers=headers, proxy=proxy, num_retries=num_retries)
            links = []
            if scrape_callback:
                links.extend(scrape_callback(url, html) or [])

            depth = seen[url]
            print 'depth为:', depth
            if depth != max_depth:
                if link_regex:
                    links.extend(link for link in get_links(html) if re.match(link_regex, link))
                print 'links为:',links
                for link in links:
                    print 'link为:',link
                    link = normalize(seed_url, link)
                    if link not in seen:
                        seen[link] = depth + 1
                        print 'seen为:',seen
                        if same_domain(seed_url, link):
                            crawl_queue.append(link)

            num_urls += 1
            if num_urls == max_urls:
                break
        else:
            print 'Blocked by robots.txt:', url
        print 'crawl_queue为:', crawl_queue


def get_links(html):
    webpage_regex = re.compile('<a[^>]+href=["\'](.*?)["\']',re.IGNORECASE)
    return webpage_regex.findall(html)


def get_robots(url):
    rp = robotparser.RobotFileParser()
    rp.set_url(urlparse.urljoin(url, '/robots.txt'))
    rp.read()
    return rp


def normalize(seed_url, link):
    link, _ = urlparse.urldefrag(link) # remove hash to avoid duplicates
    return urlparse.urljoin(seed_url, link)

def same_domain(url1, url2):
    return urlparse.urlparse(url1).netloc == urlparse.urlparse(url2).netloc


# link_crawler('http://example.webscraping.com','/(index|view)')

if __name__ == '__main__':
     # link_crawler('http://example.webscraping.com', '/(index|view)', delay=0, num_retries=1, user_agent='BadCrawler')
     link_crawler('http://example.webscraping.com', '/(index|view)', delay=0, num_retries=1, max_depth=1, user_agent='GoodCrawler')