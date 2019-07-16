# *_*coding:utf-8 *_*
# date:
__author__ = 'beiliangshizi'

from numpy import genfromtxt, zeros
import sklearn
from matplotlib.pyplot import plot,show



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


#k-means算法简介：算法接受输入量k ，并将n个数据对象分为k个聚类；获得的聚类满足:同一聚类中的对象相似度较高;不同聚类中对象相似度低；
#                聚类相似度是利用各聚类中对象的均值所获得一个“中心对象”（引力中心）来进行计算。
#k-means 算法基本步骤：
#（1） 从 n个数据对象任意选择k个对象作为初始聚类中心（最终期望聚为k类）；
#（2） 根据每个聚类对象的均值（中心对象），计算每个对象与这些中心对象的距离；按最小距离重新对相应对象进行划分；
#（3） 重新计算每个（有变化）聚类的均值（中心对象）；
#（4） 计算标准测度函数，当满足一定条件，如函数收敛时，则算法终止；如果条件不满足则回到步骤（2）。
############################

from pylab import figure, subplot, hist, xlim, show
from sklearn.cluster import KMeans
kms = KMeans(n_clusters=3) # initialization 先验知道3种植物，所以设定引力中心为聚合成3类。
#kmeans = KMeans(k=3, init='random') # both parameters are wrong
kms.fit(data) # actual execution
c = kms.predict(data)

from sklearn.metrics import completeness_score, homogeneity_score
print completeness_score(t,c)
#output:0.764986151449
print homogeneity_score(t,c)
#output:0.751485402199

#特别注意！t中只要是3类值就行，不一定非要1,2,3
#当大部分数据点属于一个给定的类并且属于同一个群集，那么完整性得分就趋向于1。
#当所有群集都几乎只包含某个单一类的数据点时同质性得分就趋向于1.
figure()
subplot(211) # top figure with the real classes
plot(data[t==1,0],data[t==1,2],'bo')
plot(data[t==2,0],data[t==2,2],'ro')
plot(data[t==3,0],data[t==3,2],'go')
subplot(212) # bottom figure with classes assigned automatically
plot(data[c==1,0],data[c==1,2],'bo',alpha=.5)
plot(data[c==2,0],data[c==2,2],'go',alpha=.5)
plot(data[c==0,0],data[c==0,2],'mo',alpha=.5)
show()

#观察此图我们可以看到，底部左侧的群集可以被k-means完全识别，
#然而顶部的两个群集有部分识别错误。按照kmean的中心对象是引力中心的聚类方法
#出现识别错误是必然的；样本的偶然性可能导致识别错误

#如下是将4个feature维度组合为2个点放入一个平面，也可以看到聚类为3种后，
#边界变得清晰了。
import matplotlib.pyplot as plt
plt.figure()
plt.subplot(211) # top figure with the real classes
plt.plot(data[t==1,0],data[t==1,1],'bo',data[t==1,2],data[t==1,3],'b+')
plt.plot(data[t==2,0],data[t==2,1],'ro',data[t==2,2],data[t==2,3],'r+')
plt.plot(data[t==3,0],data[t==3,1],'go',data[t==3,2],data[t==3,3],'g+')
plt.subplot(212) # bottom figure with classes assigned automatically
plt.plot(data[c==0,0],data[c==0,1],'bo',data[c==0,2],data[c==0,3],'b+',alpha=.7)
plt.plot(data[c==1,0],data[c==1,1],'ro',data[c==1,2],data[c==1,3],'r+',alpha=.7)
plt.plot(data[c==2,0],data[c==2,1],'go',data[c==2,2],data[c==2,3],'g+',alpha=.7)
p=plt
fig=plt.gcf()
fig.show() # p.show()也可，但二者只能执行一次。
