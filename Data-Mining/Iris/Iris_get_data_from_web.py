# *_*coding:utf-8 *_*
# date:
__author__ = 'beiliangshizi'


import urllib2
url = 'http://aima.cs.berkeley.edu/data/iris.csv'
u = urllib2.urlopen(url)
#以下为本地样本存储路径，请根据实际情况设定！
localfn='iris.csv'
localf = open(localfn, 'w')
localf.write(u.read())
localf.close()