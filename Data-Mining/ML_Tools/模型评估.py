# *_*coding:utf-8 *_*
# date:
__author__ = 'beiliangshizi'

from numpy import genfromtxt, zeros


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
from sklearn import cross_validation
train,test,t_train,t_test = cross_validation.train_test_split(data,t,test_size=0.4, random_state=0)
#用全部data集来做训练
from sklearn.naive_bayes import GaussianNB
classifier = cf = GaussianNB()
cf.fit(data,t) # training on the iris dataset






#用混淆矩阵估计分类器表现
from sklearn.metrics import confusion_matrix
print confusion_matrix(cf.predict(test),t_test)
#output:[[16  0  0]
#output: [ 0 23  4]
#output: [ 0  0 17]]

#混淆矩阵简单说明
#        预测情况
#        -----------
#        类1 类2 类3
#实 |类1 43  5   2
#际 |类2 2   45  3
#情 |类3 0   1   49
#况 |
#
#说明：正确的猜测都在表格的对角线
#解读：实际情况是3个类每个都50个样本；
#      类3有1个错误的猜测为类2；
#      类2有2个错误的猜测为类1,3个错误的识别为类3
#      类1有5个错误的猜测为类2,2个错误的识别为类3

#分类器性能的完整报告
#Precision：正确预测的比例
#Recall（或者叫真阳性率）：正确识别的比例
#F1-Score：precision和recall的调和平均数

from sklearn.metrics import classification_report
print classification_report(classifier.predict(test), t_test, target_names=['setosa', 'versicolor', 'virginica'])
#output:            precision    recall  f1-score   support
#output:    setosa       1.00      1.00      1.00        16
#output:versicolor       1.00      0.85      0.92        27
#output: virginica       0.81      1.00      0.89        17
#output:avg / total      0.95      0.93      0.93        60

##############################################################
#补充调和平均数知识点
#调和平均数：Hn=n/(1/a1+1/a2+...+1/an)
#几何平均数：Gn=(a1a2...an)^(1/n)
#算术平均数：An=(a1+a2+...+an)/n
#平方平均数：Qn=√ [(a1^2+a2^2+...+an^2)/n]
#这四种平均数满足 Hn ≤ Gn ≤ An ≤ Qn
#
#调和平均数典型举例：
#问：有4名学生分别在一个小时内解题3、4、6、8道，求平均解题速度多少（1小时能解几道）？
#答：就是求调和平均数，即1/[(1/3+1/4+1/6+1/8)/4]=4/(1/3+1/4+1/6+1/8)=4.57
###########################################################


#以上仅仅只是给出用于支撑测试分类的数据量。
#分割数据、减少用于训练的样本数以及评估结果等操作
#都依赖于配对的训练集和测试集的随机选择


#如果要切实评估一个分类器并与其它的分类器作比较的话，
#我们需要使用一个更加精确的评估模型，例如Cross Validation。
#该模型背后的思想很简单：多次将数据分为不同的训练集和测试集，
#最终分类器评估选取多次预测的平均值。
#sklearn为我们提供了运行模型的方法：

from sklearn.cross_validation import cross_val_score
# cross validation with 6 iterations
scores = cross_val_score(classifier, data, t, cv=6)
print scores
#output:[ 0.92592593  1.          0.91666667  0.91666667  0.95833333  1.        ]
#并非迭代越多次越好。当前CV=6，迭代6次

#输出是每次模型迭代产生的精确度的数组。我们可以很容易计算出平均精确度：
from numpy import mean, genfromtxt

print mean(scores)
#output:0.96

#循环不断增加迭代cv次数，并输出mean值
#迭代CV必须>=2,否则报错'ValueError: k-fold cross validation requires at least one train / test split by setting n_folds=2 or more, got n_folds=1.'
#迭代CV必须小于最小的一个样本数目（对t=50;t_train=27;t_test=16），详见后面ndarray归类打印！
#1.穷举data的所有迭代cv可能的交叉验证平均值并打印
for i in range(2, 51):
  scores = cross_val_score(classifier, data, t, cv=i)
  print mean(scores)#每句for语句在交互式界面必须跟一行空行（没任何字符包括空格）才能表示输入结束！


#2.穷举test的所有迭代cv可能的交叉验证平均值并打印
for i in range(2, 17): print mean(cross_val_score(classifier, test, t_test, cv=i))


#3.穷举train的所有迭代cv可能的交叉验证平均值并打印
for i in range(2, 28): print mean(cross_val_score(classifier, train, t_train, cv=i))


#
#
#对一维numpy.ndarray数字值归类并打印
ndarray={}
for item in t: ndarray[item] = ndarray.get(item, 0) + 1
    #下面必须有一行空行（没任何空格！），让交互式python确认for语句完成输入

print(ndarray)
#output:{1.0: 50, 2.0: 50, 3.0: 50}

#对一维numpy.ndarray数字值归类并打印
ndarray={}
for item in t_train: ndarray[item] = ndarray.get(item, 0) + 1
    #下面必须有一行空行，让交互式python确认for语句完成输入

print(ndarray)
#output:{1.0: 34, 2.0: 27, 3.0: 29}

#对一维numpy.ndarray数字值归类并打印
ndarray={}
for item in t_test: ndarray[item] = ndarray.get(item, 0) + 1
    #下面必须有一行空行，让交互式python确认for语句完成输入

print(ndarray)
#output:{1.0: 16, 2.0: 23, 3.0: 21}