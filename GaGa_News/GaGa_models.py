#coding=utf-8
import MySQLdb
from GaGa_app import db



class News(db.Model):
    news_content = db.Column(db.String(32),primary_key=False) #here is not clear,类型是string还是text？

    def __init__(self,news_content):
        self.news_content = news_content
    def __repr__(self):
        return '<News'