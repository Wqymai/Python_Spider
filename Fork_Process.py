#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import os

print 'Process (%s) start ...' % os.getpid()
pid = os.fork()
print 'pid=(%s)' % pid
if pid == 0:
    print '我是子线程 (%s) ,我的父线程是 (%s). ' % (os.getpid(),os.getppid())
else:
    print '我(%s) 创建了一个子线程(%s).' % (os.getpid(),pid)

