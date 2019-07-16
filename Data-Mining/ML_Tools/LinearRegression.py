# *_*coding:utf-8 *_*
# date:
__author__ = 'beiliangshizi'


from numpy import genfromtxt
from matplotlib.pyplot import plot,show

localfn='iris.csv'
data = genfromtxt(localfn,delimiter=',',usecols=(0,1,2,3))
# read the fifth column
target = genfromtxt(localfn,delimiter=',',usecols=(4),dtype=str)

#回归是一个用于预测变量之间函数关系调查的方法。
#假设有两个变量：一个被认为是因，一个被认为是果。
#回归模型描述两者关系；从一个变量推断另一个变量；
#当这种关系是一条线时，称为线性回归。


##############
#sklear.linear_model模块中的LinearRegression模型。
#它通过计算每个数据点到拟合线的垂直差的平方和，
#找到平方和最小的最佳拟合线。类似sklearn模型；
#
##############

#下面举例随机产生了40个点样本，但大致函数趋势是
#在第一象限线性增长，用线性回归来找出拟合线并评估
#Step1-随机产生第一象限40个点
from numpy.random import rand
x = rand(40,1) # explanatory variable
y = x*x*x+rand(40,1)/5 # depentend variable

#Step2-线性回归
from sklearn.linear_model import LinearRegression
linreg = LinearRegression()
linreg.fit(x,y)

#Step3-随机产生x变量，用线性回归模型推断y变量（推断出来是一条线）
from numpy import linspace, matrix
#产生0到1之间40个样本值
randx = linspace(0,1,40)
#用随机产生的40个x轴样本，用线性回归预测其y轴样本，并输出比较
#推断y时先将x当做矩阵转置为y再推断
plot(x,y,'o',randx,linreg.predict(matrix(randx).T),'--r')
show()

#Step4-通过测量MSE指标看拟合线与真实数据的距离平方。0最好
from sklearn.metrics import mean_squared_error
print mean_squared_error(linreg.predict(x),y)

#########################
#针对本例实际花萼的长宽数据做线性回归
#########################
#获取x和y（需要reshape来转换数组(50,)到一维矩阵(50,1)，才能做linreg.fit!
ssx_blue=data[target=='setosa',0].reshape((50,1)) #获取setosa的sepal花萼length
ssy_blue=data[target=='setosa',1].reshape((50,1)) #获取setosa的sepal花萼width

#用x和y获得线性回归模型
linreg = LinearRegression()
linreg.fit(ssx_blue,ssy_blue)

#随机产生x变量，用线性回归模型推断y变量（推断出来是一条线）
#根据经验蓝色品种setosa的花萼sepal的长宽尺寸一般为X:[4.0-6.0]y:[2.5-4.5]
randx = linspace(4.0,6.0,50)
plot(ssx_blue,ssy_blue,'o',randx,linreg.predict(matrix(randx).T),'--r')
show()

#通过测量MSE指标看拟合线与真实数据的距离平方。0最好
print mean_squared_error(linreg.predict(ssx_blue),ssy_blue)
