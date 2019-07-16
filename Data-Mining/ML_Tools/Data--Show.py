# *_*coding:utf-8 *_*
# date:
__author__ = 'beiliangshizi'



from numpy import genfromtxt, zeros
# read the first 4 columns

localfn='iris.csv'


data = genfromtxt(localfn,delimiter=',',usecols=(0,1,2,3))
# read the fifth column
target = genfromtxt(localfn,delimiter=',',usecols=(4),dtype=str)

#figure for 2D data
from pylab import plot, show
plot(data[target=='setosa',0],data[target=='setosa',2],'bo')
plot(data[target=='versicolor',0],data[target=='versicolor',2],'r+')
plot(data[target=='virginica',0],data[target=='virginica',2],'g*')
show()


#figure for all 4D（4个维度） data, 同色一类，圈是花萼，加号花瓣
setosa_sepal_x=ssx=data[target=='setosa',0]
setosa_sepal_y=ssy=data[target=='setosa',1]
setosa_petal_x=spx=data[target=='setosa',2]
setosa_petal_y=spy=data[target=='setosa',3]

versicolor_sepal_x=vsx=data[target=='versicolor',0]
versicolor_sepal_y=vsy=data[target=='versicolor',1]
versicolor_petal_x=vpx=data[target=='versicolor',2]
versicolor_petal_y=vpy=data[target=='versicolor',3]

virginica_sepal_x=vgsx=data[target=='virginica',0]
virginica_sepal_y=vgsy=data[target=='virginica',1]
virginica_petal_x=vgpx=data[target=='virginica',2]
virginica_petal_y=vgpy=data[target=='virginica',3]

plot(ssx,ssy,'bo',spx,spy,'b+')
plot(vsx,vsy,'ro',vpx,vpy,'r+')
plot(vgsx,vgsy,'go',vgpx,vgpy,'g+')
show()


#figure for 1D（花萼的长度），三类长度及平均值的直方图
#pylab详细用法参考如下
#http://hyry.dip.jp/tech/book/page/scipy/matplotlib_fast_plot.html
from pylab import figure, subplot, hist, xlim, show
xmin = min(data[:,0])
xmax = max(data[:,0])
figure() #可省略，默认会生成一个figure
subplot(411) # distribution of the setosa class (1st, on the top)
hist(data[target=='setosa',0],color='b',alpha=.7)
xlim(xmin,xmax)
#subplot（行,列,plot号）；(4,1,2)合并为412,都小于10可合成
subplot(412) # distribution of the versicolor class (2nd)
hist(data[target=='versicolor',0],color='r',alpha=.7)
xlim(xmin,xmax)
subplot(413) # distribution of the virginica class (3rd)
hist(data[target=='virginica',0],color='g',alpha=.7)
xlim(xmin,xmax)
subplot(414) # global histogram (4th, on the bottom)
hist(data[:,0],color='y',alpha=.7)
xlim(xmin,xmax)
show()