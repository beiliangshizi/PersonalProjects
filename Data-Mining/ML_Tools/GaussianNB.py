# *_*coding:utf-8 *_*
# date:
from numpy import genfromtxt, zeros

__author__ = 'beiliangshizi'


localfn='iris.csv'
data = genfromtxt(localfn,delimiter=',',usecols=(0,1,2,3))
# read the fifth column
target = genfromtxt(localfn,delimiter=',',usecols=(4),dtype=str)

#仿造target阵列(1维)弄出全0的t阵列
t = zeros(len(target))
#type(t) #show type of t (numpy.ndarray)
#print t #show contains of t
#将target阵列中特定元素的位置设置为1(真简洁)
t[target == 'setosa'] = 1
t[target == 'versicolor'] = 2
t[target == 'virginica'] = 3
#print t


# 朴素贝叶斯分类器是常用的一种，分为（高斯模型/非多项式模式/非伯努利模式）



#用全部data集来做训练
from sklearn.naive_bayes import GaussianNB
classifier = cf = GaussianNB()
cf.fit(data,t) # training on the iris dataset
print cf.predict(data[0]) #训练完分类1条数据
#output:[ 1.]
print t[0]
#output:1.0

#从原始数据data中划分为训练集和验证集，t也做同样划分
from sklearn import cross_validation
train,test,t_train,t_test = cross_validation.train_test_split(data,t,test_size=0.4, random_state=0)

print train.shape
#output:(90, 4)
print test.shape
#output:(60, 4)
print t_train.shape
#output:(90,)
print t_test.shape
#output:(60,)

#用60%数据训练后，再用40%数据验证，得到93.3%
cf.fit(train,t_train) # train
print cf.score(test,t_test) # test
#output:0.93333333333333335
cf.score(train,t_train) #用训练集训练后同样用它测试居然不是100%分类！
#output:0.97777777777777775

#用全部数据训练后，同样用它测试，结果低于刚才97%
cf.fit(data,t)
#output:GaussianNB()
cf.score(data,t)
#output:0.95999999999999996


#用100%数据训练后，再用40%数据验证，得到94.99%
cf.fit(data,t)
#output:GaussianNB()
cf.score(test,t_test)
#output:0.94999999999999996