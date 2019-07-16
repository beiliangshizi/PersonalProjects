#coding:utf-8
author = 'beiliangshizi'
#date:2017-05-23
#note:this module is used by python3.5

from os import path
import jieba

import sys


import codecs

stopwords = {}
splist = ["salary", "scale", "规模", "degree","学历要求：", "nature","公司","性质", "company",
             "jobname", "exprience","学历","工作","经验：", "location", "askandduty"]
for i in splist:
    stopwords.setdefault(i,0)

def importStopword(filename = ''):
    global stopwords
    f = codecs.open(filename,'r',encoding='gbk')
    line = f.readline().rstrip()

    while line:
        stopwords.setdefault(line,0)
        stopwords[line] = 1
        line = f.readline().rstrip()

    f.close()

def processChinese(text):
    seg_generator = jieba.cut(text)
    seg_list = [i for i in seg_generator if i not in stopwords]
    seg_list = [i for i in seg_list if i != u' ']
    seg_list = r' '.join(seg_list)
    return seg_list

if __name__ == "__main__":
    importStopword(filename='./stopwords.txt')
    d = path.dirname(__file__)
    # text = open(path.join(d,'./fenci_test.txt'),encoding='utf-8').read()
    text = open(path.join(d,'./json_test.txt'),encoding='utf-8').read()
    fc = processChinese(text)
    print("*********************************************************")
    with open(sys.path[0] + '/output.txt','r+') as output:
        for i in fc:
            output.write(i)
        output.close()































