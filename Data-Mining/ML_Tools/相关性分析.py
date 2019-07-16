# *_*coding:utf-8 *_*
# date:
__author__ = 'beiliangshizi'

from numpy import genfromtxt

localfn='iris.csv'
data = genfromtxt(localfn,delimiter=',',usecols=(0,1,2,3))
# read the fifth column
target = genfromtxt(localfn,delimiter=',',usecols=(4),dtype=str)

#通过研究feature之间的相关性来理解变量之间是否相关，相关强弱。
#相关性分析帮助定位被依赖的重要变量。最好的相关方法可能是皮尔逊积矩相关系数。
#它是由两个变量的协方差除以它们的标准差的乘积计算而来。
#我们将鸢尾花数据集的4个变量两两组合计算出其相关性系数。
#特别说明：feature是可以组合与变换的，所以不一定是未处理的初始feature两两做相关性判断，
#          而可能是人为`判断有相关性的，尝试组合或变换feature再不断测试相关性。

#当值一起增长时相关性为正。当一个值减少而另一个值增加时相关性为负。
#1代表完美的正相关，0代表不相关，-1代表完美的负相关。

#本例红色被关联为最高的正相关，可以看出最强相关是：
#“花瓣宽度”petal width和“花瓣长度”petal length这两个变量。

from numpy import corrcoef

corr = corrcoef(data.T) # .T gives the transpose
print corr
#output:[[ 1.         -0.10936925  0.87175416  0.81795363]
#output: [-0.10936925  1.         -0.4205161  -0.35654409]
#output: [ 0.87175416 -0.4205161   1.          0.9627571 ]
#output: [ 0.81795363 -0.35654409  0.9627571   1.        ]]

from pylab import pcolor, colorbar, xticks, yticks , show
from numpy import arange
pcolor(corr) #添加相关性矩阵，4个属性所以是4x4
colorbar() #添加彩色注释条
#添加X,Y轴注释，默认一个属性是1，坐标是1,2,3,4，对应四个属性name如下。
xticks(arange(1,5),['sepal length',  'sepal width', 'petal length', 'petal width'],rotation=-20)
yticks(arange(1,5),['sepal length',  'sepal width', 'petal length', 'petal width'],rotation=-45)
show()