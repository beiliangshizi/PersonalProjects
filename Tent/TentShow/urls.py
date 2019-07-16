#coding:utf-8
#author: beilianghsizi
#file: urls.py
#time: 2018/3/2 9:36
#desc: "  "

from django.conf.urls import *
import views


urlpatterns = [
    url(r'^$', views.showtents,name='showtents')
]