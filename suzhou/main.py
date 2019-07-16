#coding:utf-8
import sys
from scrapy import cmdline


reload(sys)
sys.setdefaultencoding('utf-8')


if __name__ == '__main__':
    cmdline.execute("scrapy crawl suzhou".split())