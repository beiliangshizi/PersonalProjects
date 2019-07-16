# *_*coding:utf-8 *_*
# date:
__author__ = 'beiliangshizi'

# iris数据集的中文名是安德森鸢尾花卉数据集，英文全称是Anderson’s Iris data set。
# iris包含150个样本，对应数据集的每行数据。每行数据包含每个样本的四个特征和样本的类别信息，
# 所以iris数据集是一个150行5列的二维表。
# 通俗地说，iris数据集是用来给花做分类的数据集，每个样本包含了花萼长度、花萼宽度、花瓣长度、花瓣宽度四个特征（前4列），
# 我们需要建立一个分类器，分类器可以通过样本的四个特征来判断样本属于山鸢尾、变色鸢尾还是维吉尼亚鸢尾（这三个名词都是花的品种）。
# iris的每个样本都包含了品种信息，即目标属性（第5列，也叫target或label）。


from sklearn import datasets
iris = datasets.load_iris()
#表征数据量的大小,此处150行4列
print iris.data.shape
#要显示的特征样本数量,这里是从头到第20行
print iris.data[:20]
#target对应了样本的类别（目标属性），150行1列
print iris.target.shape
#显示所有样本的目标属性
print iris.target

