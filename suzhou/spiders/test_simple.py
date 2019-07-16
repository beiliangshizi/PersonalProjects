# #coding:utf-8
# # start_url:http://jobs.51job.com/suzhou/jisuanjiruanjian/
# # 功能：爬取前程无忧苏州地区计算机软件招聘信息，后期进行数据分析和可视化
# import threading
# import traceback
# import scrapy.spiders.crawl
#
#
# import lxml
# from lxml import etree
# from multiprocessing import Pool, Queue
# import json
# import sys
#
# import bs4
# from bs4 import BeautifulSoup
# import requests
# import time
# import re
# import os
# from scrapy.selector import Selector
# from scrapy.spiders import spiders, Rule
# import scrapy
# from SUZHOU.items import SuzhouItem
#
# __author__ = 'beilianshizi'
#
# reload(sys)
# sys.setdefaultencoding('utf-8')
#
# class suzhouspider(object):
#     def __init__(self):
#         self.page_link = set()  # 保存下一页页面url
#         self.content_link = set()  # 保存页面内所有可获得的url
#         self.jobs = Queue.Queue(1)  #建立一个队列，用来存储和分配任务
#         self.data = {}   #将结果保存和输出用
#     def run(self):   #运行并获得下一个网址
#         self.jobs.put("http://jobs.51job.com/suzhou/jisuanjiruanjian/p1")
#         for loopid in range(2):
#             t_update = threading.Thread(target=self.work,
#                                         args=(loopid,))
#             t_update.setDaemon(False)
#             t_update.start()
#         self.create()
#     def work(self,response):
#         try:
#             print "ppppppppppppppppppp-------------work-------------pppppppppppppppppppppppp"
#             if response:
#                 self.parse(response)
#             item = SuzhouItem()
#             for con in response.xpath('//div[@class="detlist gbox"]/div[@class="e"]'):
#
#                 jobname = con.xpath('p[1]/span[1]/a[1]/text()').extract()[0]
#                 item['jobname'] = ''.join(jobname).replace('\n', '').replace(' ', '').replace('\t', '')
#                 company = con.xpath('p[1]/a[@class="name"]/text()').extract()[0]
#                 item['company'] = ''.join(company).replace('\n', '').replace(' ', '').replace('\t', '')
#                 location = con.xpath('p[1]/span[@class="location name"]/text()').extract()[0]
#                 item['location'] = ''.join(location).replace('\n', '').replace(' ', '').replace('\t', '')
#                 # now,TypeError: <Selector xpath= data='> is not JSON serializable
#                 salary = con.xpath('p[1]/span[@class="location"]/text()').extract()[0]
#                 item['salary'] = ''.join(salary).replace('\n', '').replace(' ', '').replace('\t', '')
#                 degree = con.xpath('p[2]/text()').extract()[0]
#                 item['degree'] = ''.join(degree).replace('\n', '').replace(' ', '').replace('\t', '')
#                 exprience = con.xpath('p[2]/text()').extract()[1]
#                 item['exprience'] = ''.join(exprience).replace('\n', '').replace(' ', '').replace('\t', '')
#                 nature = con.xpath('p[2]/text()').extract()[2]
#                 item['nature'] = ''.join(nature).replace('\n', '').replace(' ', '').replace('\t', '')
#                 scale = con.xpath('p[2]/text()').extract()[3]
#                 item['scale'] = ''.join(scale).replace('\n', '').replace(' ', '').replace('\t', '')
#                 # .replace('\n', '').replace(' ', '')
#                 askandduty = con.xpath('p[3]/text()').extract()[0]
#                 item['askandduty'] = ''.join(askandduty).replace('\n', '').replace(' ', '').replace('\t', '')
#                 items.append(item)
#         except:
#             if "location" in traceback.format_exc():
#                 pass
#             else:
#                 print 'something wrong here'
#                 error_msg = traceback.format_exc()
#                 print error_msg
#     def create(self):
#         pass
#     def show(self):
#         for i in range(len(self.data)):
#             print self.data[i]
#
#
#
#
#     def parse(self, response):
#         # global is_start_page
#         #
#         # url = ""
#         # # 从开始页面开始解析数据，开始页面start_urls
#         # if is_start_page:
#         #     url = self.start_urls[0]
#         #     is_start_page = False
#         # else:
#         #     href = response.xpath('//div[@id="cppageno"]/ul/li[@class="bk"]/a/@href')
#         #     url = response.urljoin(href.extract())
#         #
#         # yield scrapy.Request(url, callback=self.parse_content)
#             # 爬取一个页面内的所有url链接
#
#         # for link in self.rules['page'].extract_links(response):
#         #
#         #     if link.url not in self.content_link:
#         #         self.page_link.add(link.url)
#         #
#         #         yield scrapy.Request(link.url, callback=self.parse_item)
#
#                 # 自动获取下一页的url
#
#         next_pages = response.xpath('//div[@id="cppageno"]/ul/li[8]/a/@href').extract()[0]
#
#         if next_pages not in self.page_link:
#             next_page =  next_pages
#
#             self.page_link.add(next_page)
#             print "---------------here parse run000000000000000000"
#
#             yield scrapy.Request(next_pages, callback=self.parse_item)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
