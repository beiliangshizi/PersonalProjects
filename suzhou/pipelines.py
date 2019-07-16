# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs
import sys



reload(sys)
sys.setdefaultencoding('utf-8')

class SuzhouPipeline(object):
    def __init__(self):
        self.file = codecs.open('items.json','wb',encoding='utf-8')
    def process_item(self, item, spider):
        #做些输出测试
        # print 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
        # for i in item:
        #     print item[i]
        # print 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx','\n\n\n\n\n'
        # item['jobname'] = json.dumps(str(item['jobname']),ensure_ascii=False)
        # item['company'] = json.dumps(str(item['company']),ensure_ascii=False)
        # item['location'] = json.dumps(str(item['location']),ensure_ascii=False)
        # item['salary'] = json.dumps(str(item['salary']),ensure_ascii=False)
        # item['degree'] = json.dumps(str(item['degree']),ensure_ascii=False)
        # item['exprience'] = json.dumps(str(item['exprience']),ensure_ascii=False)
        # item['nature'] = json.dumps(str(item['nature']),ensure_ascii=False)
        # item['scale'] = json.dumps(str(item['scale']),ensure_ascii=False)
        # item['askandduty'] = json.dumps(str(item['askandduty']),ensure_ascii=False)
        #line = jobname+company+location+salary+degree+exprience+nature+scale+askandduty
        # "岗位:"+"公司:"+"位置:"+"薪水:"+"学历:"+"工作经验:"+"公司性质:"+"公司规模:"+"要求和职责:"+
        line = json.dumps(dict(item),ensure_ascii=False) + '\n'
        self.file.write(line)
        return item

    def spider_closed(self,spider):
        self.file.close()






















