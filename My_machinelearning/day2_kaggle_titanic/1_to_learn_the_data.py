#coding:utf-8
#date : 2017-06-19

__author__ = 'beiliangshizi'

import pandas as pd #数据分析
import numpy as np #科学计算
from pandas import Series,DataFrame
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
font_set = FontProperties(fname=r"/usr/local/lib/python2.7/dist-packages/matplotlib-2.0.2-py2.7-linux-x86_64.egg/matplotlib/mpl-data/fonts/ttf/um.ttf", size=10)
# plt.rcParams['font.sans-serif'] = ['um']
# plt.rcParams['axes.unicode_minus'] = False

data_train = pd.read_csv("train.csv")

#------------------------------------------------------------------------------------------
# print data_train.info()

# train.csv 's informations,we can see that some values are null..

# RangeIndex: 891 entries, 0 to 890
# Data columns (total 12 columns):
# PassengerId    891 non-null int64
# Survived       891 non-null int64
# Pclass         891 non-null int64
# Name           891 non-null object
# Sex            891 non-null object
# Age            714 non-null float64
# SibSp          891 non-null int64
# Parch          891 non-null int64
# Ticket         891 non-null object
# Fare           891 non-null float64
# Cabin          204 non-null object
# Embarked       889 non-null object

# PassengerId => 乘客ID
# Pclass => 乘客等级(1/2/3等舱位)
# Name => 乘客姓名
# Sex => 性别
# Age => 年龄
# SibSp => 堂兄弟/妹个数
# Parch => 父母与小孩个数
# Ticket => 船票信息
# Fare => 票价
# Cabin => 客舱
# Embarked => 登船港口

#-------------------------------------------------------------------------------------------
# print  data_train.describe()

#train.csv 's informations,描述性统计,

#        PassengerId    Survived      Pclass         Age       SibSp  \
# count   891.000000  891.000000  891.000000  714.000000  891.000000
# mean    446.000000    0.383838    2.308642   29.699118    0.523008
# std     257.353842    0.486592    0.836071   14.526497    1.102743
# min       1.000000    0.000000    1.000000    0.420000    0.000000
# 25%     223.500000    0.000000    2.000000   20.125000    0.000000
# 50%     446.000000    0.000000    3.000000   28.000000    0.000000
# 75%     668.500000    1.000000    3.000000   38.000000    1.000000
# max     891.000000    1.000000    3.000000   80.000000    8.000000
    #             Parch        Fare
    # count  891.000000  891.000000
    # mean     0.381594   32.204208
    # std      0.806057   49.693429
    # min      0.000000    0.000000
    # 25%      0.000000    7.910400
    # 50%      0.000000   14.454200
    # 75%      0.000000   31.000000
    # max      6.000000  512.329200


fig = plt.figure()
fig.set(alpha=0.2)  # 设定图表颜色alpha参数

plt.subplot2grid((2,3),(0,0))             # 在一张大图里分列几个小图
data_train.Survived.value_counts().plot(kind='bar')# 柱状图
plt.title(u"获救情况 (1为获救)",fontproperties=font_set) # 标题
plt.ylabel(u"人数",fontproperties=font_set)

plt.subplot2grid((2,3),(0,1))
data_train.Pclass.value_counts().plot(kind="bar")
plt.ylabel(u"人数",fontproperties=font_set)
plt.title(u"乘客等级分布",fontproperties=font_set)

plt.subplot2grid((2,3),(0,2))
plt.scatter(data_train.Survived, data_train.Age)
plt.ylabel(u"年龄",fontproperties=font_set)                         # 设定纵坐标名称
plt.grid(b=True, which='major', axis='y')
plt.title(u"按年龄看获救分布 (1为获救)",fontproperties=font_set)


plt.subplot2grid((2,3),(1,0), colspan=2)
data_train.Age[data_train.Pclass == 1].plot(kind='kde')
data_train.Age[data_train.Pclass == 2].plot(kind='kde')
data_train.Age[data_train.Pclass == 3].plot(kind='kde')
plt.xlabel(u"年龄",fontproperties=font_set)# plots an axis lable
plt.ylabel(u"密度",fontproperties=font_set)
plt.title(u"各等级的乘客年龄分布",fontproperties=font_set)
plt.legend((u'top', u'2nd',u'3rd'),loc='best') # sets our legend for our graph.


plt.subplot2grid((2,3),(1,2))
data_train.Embarked.value_counts().plot(kind='bar')
plt.title(u"各登船口岸上船人数",fontproperties=font_set)
plt.ylabel(u"人数",fontproperties=font_set)
plt.show()



