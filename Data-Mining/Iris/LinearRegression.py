# *_*coding:utf-8 *_*
# date:
__author__ = 'beiliangshizi'


from pylab import plot,show

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
