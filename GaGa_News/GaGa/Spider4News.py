#coding:utf-8
#编程实现：爬取新浪新闻网站上2017年“新闻排行”的新闻，去重存储到数据库中，并可视化到网页
#使用urllib2和beautifulsoup库

import urllib2
from bs4 import BeautifulSoup
import MySQLdb
import MySQLdb.cursors
import re

def crawl(url):
    page = urllib2.urlopen(url)
    content = page.read()
    soup = BeautifulSoup(content)
    for tag in soup.find_all('td',class_='ConsTi'):
        news = tag.a.get_text()
        # print news
        conn = MySQLdb.connect(host='localhost',user='root',passwd='5211314',db='test_News',port=3306,charset='utf8')
        cur = conn.cursor()
        cur.execute('insert into test(content) values(%s)',(news))
        print "good success"
        conn.commit()
        cur.close()
        conn.close()


if __name__=='__main__':
    print '新浪新闻2017年新闻排行榜上榜新闻'
    #crawl('http://news.sina.com.cn/hotnews/#1')
    urltemp = 'http://news.sina.com.cn/hotnews/20170101.shtml'
    for i in range(1,4):
        for j in range(1,32):
            if j>=10:
                print str(i)
                print str(j)
                urltemp = urltemp[:37]+str(i)+str(j)+'.shtml'
            else:
                urltemp = urltemp[:37]+str(i)+'0'+str(j)+'.shtml'
            crawl(urltemp)
                #print urltemp




