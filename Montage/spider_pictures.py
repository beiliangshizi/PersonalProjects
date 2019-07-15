#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import re
import sys
import json
import time
import socket
import threading
import urllib
import urllib.error
import urllib.request
from queue import Queue
from threading import Lock


timeout = 5 # 设置超时
socket.setdefaulttimeout(timeout)

def MultiPrint(content):    #解决多线程中输出错乱的问题
    sys.stdout.write('{}\n'.format(content))

mutex = Lock()      # 线程锁

def add_mutex(func):

    def decor(*args, **kwargs):
        time.sleep(0.1)
        mutex.acquire()
        func(*args, **kwargs)
        mutex.release()

    return decor


class Crawler:

    __time_sleep = 0.1      # 睡眠时长
    __amount = 0
    __start_amount = 0
    __counter = 0

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}

    def __init__(self, t = 0.1):
        self.time_sleep = t         # t 下载图片时间间隔
        self.taskQueue = Queue()     #图片下载任务队列

    @add_mutex
    def incre(self):
        self.__counter += 1

    # 获取后缀名
    def get_suffix(self, name):
        m = re.search(r'\.[^\.]*$', name)
        if m.group(0) and len(m.group(0)) <= 5:
            return m.group(0)
        else:
            return '.jpeg'

    # 获取referrer，用于生成referrer
    def get_referrer(self, url):
        par = urllib.parse.urlparse(url)
        if par.scheme:
            return par.scheme + '://' + par.netloc
        else:
            return par.netloc

    # 保存图片
    def save_image(self, downloadurl, word):
        # 判断名字是否重复，获取图片长度
        self.__counter = len(os.listdir('./' + word)) + 1

        try:
            time.sleep(self.time_sleep)
            suffix = self.get_suffix(downloadurl)
            refer = self.get_referrer(downloadurl)
            opener = urllib.request.build_opener()
            opener.addheaders = [
                ('User-agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0'),
                ('Referer', refer)
            ]
            urllib.request.install_opener(opener)       # 指定UA和referrer，减少403
            urllib.request.urlretrieve(downloadurl, './' + word + '/' + str(self.__counter) + str(suffix))  #保存图片
        except Exception as err:
            time.sleep(1)
            MultiPrint("产生未知错误，放弃保存")
        else:
            MultiPrint("+1, 当前完成 {0} /{1}张图片下载 ".format(str(self.__counter), self.__amount))
            self.incre()

    # 获取图片下载地址
    def get_images_url(self, word):
        search = urllib.parse.quote(word)
        pn = self.__start_amount                # pn int 图片数
        while pn < self.__amount:

            url = 'http://image.baidu.com/search/avatarjson?tn=resultjsonavatarnew&ie=utf-8&word=' + search +\
                  '&cg=girl&pn=' + str(pn) + '&rn=60&itg=0&z=0&fr=&width=&height=&lm=-1&ic=0&s=0&st=-1&gsm=1e0000001e'
            try:
                time.sleep(self.time_sleep)
                req = urllib.request.Request(url=url, headers=self.headers)                 # 设置header防ban
                page = urllib.request.urlopen(req)
                rsp = page.read().decode('unicode_escape')
            except UnicodeDecodeError as e:
                MultiPrint('-----UnicodeDecodeErrorurl:', url)
            except urllib.error.URLError as e:
                MultiPrint("-----urlErrorurl:", url)
            except socket.timeout as e:
                MultiPrint("-----socket timout:", url)
            else:
                rsp_data = json.loads(rsp)                          # 解析json
                for image_info in rsp_data['imgs']:
                    image_download_url = image_info['objURL']
                    self.taskQueue.put(image_download_url)
                pn += 60
                MultiPrint("已获取{0}/{1}个图片下载地址".format(pn, self.__amount))
            finally:
                page.close()

    def download(self, word):
        if not os.path.exists("./" + word):
            os.mkdir("./" + word)
        while True:
            try:
                url = self.taskQueue.get_nowait()       # 不阻塞的读取队列数据
                i = self.taskQueue.qsize()
            except:
                break
            else:
                self.save_image(url, word)


    def start(self, word= '美女', spider_page_num= 1, start_page= 1):
        """
        爬虫入口
        :param word: 抓取的关键词
        :param spider_page_num: 需要抓取数据页数 总抓取图片数量为 页数x60
        :param start_page:起始页数
        :return:
        """

        def current_time():
            return time.time()

        start_time = current_time()  # 程序启动时间点

        self.__start_amount = (start_page - 1) * 60
        self.__amount = spider_page_num * 60 + self.__start_amount
        self.get_images_url(word)
        threads = [threading.Thread(target= self.download, args=(word,)) for i in range(5)]
        for _ in threads:
            _.start()
            _.join()

        MultiPrint("耗时: %s" % (current_time() - start_time))



if __name__ == '__main__':

    crawler = Crawler(0.05)  # 抓取延迟为 0.05
    # crawler.start('二次元 美女', 10, 2)  # 抓取关键词为 “二次元 美女”，总数为 1 页（即总共 1*60=60 张），开始页码为 2
    crawler.start('特朗普', 100, 1)


