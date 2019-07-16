#coding:utf-8
# start_url:http://jobs.51job.com/suzhou/jisuanjiruanjian/
# 功能：爬取前程无忧苏州地区计算机软件招聘信息，后期进行数据分析和可视化
import traceback

from datetime import datetime
import scrapy.spiders
import scrapy.spiders.crawl
from scrapy.linkextractors import LinkExtractor

import lxml
from lxml import etree
from multiprocessing import Pool
import json
import sys

import bs4
from bs4 import BeautifulSoup
import requests
import time
import re
import os
from scrapy.selector import Selector
from scrapy.spiders import spiders, Rule
import scrapy
from SUZHOU.items import SuzhouItem

__author__ = 'beilianshizi'

reload(sys)
sys.setdefaultencoding('utf-8')

# is_start_page = True

number = 0


class suzhouspider(scrapy.Spider):
    name = 'suzhou'
    allowed_domains = ["51job.com"]
    start_urls = ["http://jobs.51job.com/suzhou/jisuanjiruanjian/p1"]
    page_link = set()  # 保存下一页页面url
    # content_link = set()  # 保存页面内所有可获得的url
    times = {'c':0}

    def parse(self,response):
        item = SuzhouItem()
        for con in response.xpath('//div[@class="detlist gbox"]/div[@class="e"]'):
            item['jobname'] = con.xpath('p[1]/span[1]/a[1]/text()').extract()[0].strip()
            item['company']  = con.xpath('p[1]/a[@class="name"]/text()').extract()[0].strip()
            item['location'] = con.xpath('p[1]/span[@class="location name"]/text()').extract()[0].strip()
            # now,TypeError: <Selector xpath= data='> is not JSON serializable
            item['salary'] = con.xpath('p[1]/span[@class="location"]/text()').extract()
            item['degree'] = con.xpath('p[2]/text()').extract()[0].strip()
            item['exprience'] = con.xpath('p[2]/text()').extract()[1].strip()
            item['nature'] = con.xpath('p[2]/text()').extract()[2].strip()
            item['scale'] = con.xpath('p[2]/text()').extract()[3].strip()
            item['askandduty'] = con.xpath('p[3]/text()').extract()[0].strip()
            yield item
        next_pages = response.xpath('//div[@id="cppageno"]/ul/li[8]/a/@href').extract()[0]
        if next_pages and next_pages not in self.page_link:
            next_page = next_pages
            self.page_link.add(next_page)
            print '%s,next page ****************************'%(datetime.now())
            self.times['c'] = self.times['c'] +1
            print '\n',self.times['c']
            yield scrapy.Request(next_page, callback=self.parse)



    #处理item[location]无法使用jumps方法实现序列化问题,,,,弃了，方法太瓜皮了，改成字符串的join方法直接修改
# class LocationEncoder(json.JSONEncoder):
#     def default(self, obj):
#         if isinstance(obj, lxml.etree._ElementUnicodeResult):
#             return obj.name
#         return json.JSONEncoder.default(self, obj)














        # data = response.body
       # soup = BeautifulSoup(data,'html.parser', from_encoding='utf-8')
       # # contents = soup.find_all('div',class_ = 'e')
       # # test01 = soup.find("div",class_='e')
       # # print "*************************",test01
       # test02 = soup.find_all(attrs={'class':True,'id':False})
       # num = 0
       # for x in test02:
       #     if not hasattr(x,''):
       #          print "*************************",x,'\n\n\n\n\n'
       #          print hasattr(x,'三大件啦')
       #          num = num+1
       # print '00000000000000000000000000000000000000000--------',num
       #
       # # for i in soup.find_all("div",class_='detlist gbox'):
       # #      print i,"--------------------------------------------------------------------","\n"
       #
       #
       # # for con in contents:
       # try:
       #       for con in soup.find_all("div",class_="e"):
       #             item = SuzhouItem()
       #             jobnameNode = con.find('p',class_='info').find('a')
       #
       #             item['jobname'] = jobnameNode.get_text()
       #             companyNode = con.find('title',class_='name')
       #             item['company'] = companyNode.get_text()
       #             locationNode = con.find('span',class_='location name')
       #             item['location'] = locationNode.get_text()
       #             salaryNode = con.find('span',class_='location')
       #             item['salary'] = salaryNode.get_text()
       #             degreeNode = con.find('p',class_='order')
       #             item['degree'] = degreeNode.get_text()
       #             exprienceNode = con.find('p',class_='order')
       #             item['exprience'] = exprienceNode.get_text()
       #             natureNode = con.find('p',class_='order')
       #             item['nature'] = natureNode.get_text()
       #             scaleNode = con.find('p',class_='order')
       #             item['scale']= salaryNode.get_text()
       #             askanddutyNode = con.find('p',class_='text')
       #             item['askandduty'] = askanddutyNode.get_text()
       #             yield item
       # except:
       #      print 'something wrong here'
       #      error_msg = traceback.format_exc()
       #      print error_msg


































