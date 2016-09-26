#!/usr/bin/env python
# -*- coding: utf-8 -*-
import shutil
import os
import re
import urlparse
import zlib
from datetime import datetime, timedelta
from link_crawler import link_crawler
try:
    import cPickle as pickle
except ImportError:
    import pickle


class DiskCache:
    def __init__(self, cache_dir='cache', expires=timedelta(days=30), compress=True):
        self.cache_dir = cache_dir
        self.expires = expires
        self.compress = compress


    def url_to_path(self, url):
        components = urlparse.urlsplit(url)
        path = components.path
        if not path:
            path = '/index.html'
        elif path.endswith('/'):
            path += 'index.html'
        filename = components.netloc+path+components.query
        filename = re.sub('[^/0-9a-zA-Z\-.,;_ ]', '_', filename)
        # restrict maximum number of characters
        filename = '/'.join(segment[:255] for segment in filename.split('/'))
        return os.path.join(self.cache_dir, filename)


    def has_expired(self, timestamp):
        return datetime.utcnow() > timestamp+self.expires

    def clear(self):
        if os.path.exists(self.cache_dir):
            shutil.rmtree(self.cache_dir)


    def __getitem__(self, url):
        path = self.url_to_path(url)
        if os.path.exists(path):
            with open(path, 'rb') as fp:
                data = fp.read()
                if self.compress:
                    data = zlib.decompress(data)
                result, timestamp = pickle.loads(data)
                if self.has_expired(timestamp):
                    raise KeyError(url + ' has expired')
                return result
        else:
            raise KeyError(url + ' does not exist')

    def __setitem__(self, url, result):
        path = self.url_to_path(url)
        folder = os.path.dirname(path)
        if not os.path.exists(folder):
            os.makedirs(folder)
        data = pickle.dumps((result, datetime.utcnow()))
        if self.compress:
            data = zlib.compress(data)
        with open(path, 'wb') as fp:
            fp.write(data)

    def __delitem__(self, url):
        path = self.__key__path(url)
        try:
            os.remove(path)
            os.removedirs(os.path.dirname(path))
        except OSError:
            pass

if __name__ == '__main__':
        link_crawler('http://example.webscraping.com/', '/(index|view)',max_depth=1, cache=DiskCache())
