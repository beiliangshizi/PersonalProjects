# *_*coding:utf-8 *_*
# date:
# __author__ = 'beiliangshizi'


from numpy import genfromtxt
import sklearn
from matplotlib.pyplot import plot,show



localfn='iris.csv'
data = genfromtxt(localfn,delimiter=',',usecols=(0,1,2,3))
# read the fifth column
target = genfromtxt(localfn,delimiter=',',usecols=(4),dtype=str)



from sklearn.decomposition import PCA
#降维到更少feature（主成分）不仅仅是为了可视化
#虽然3D也可以看，但不直观，最直观的是2D平面图，而4D或更高维人眼无法观察
#所以将data中原始4个feature降维到2维来观察。
#特别注意：它等于自动的将feature做了算法组合，以期望分离不同种类。
pca = PCA(n_components=2)

pcad = pca.fit_transform(data)

plot(pcad[target=='setosa',0],pcad[target=='setosa',1],'bo')
plot(pcad[target=='versicolor',0],pcad[target=='versicolor',1],'ro')
plot(pcad[target=='virginica',0],pcad[target=='virginica',1],'go')
show()

#查看主成分PC
print pca.explained_variance_ratio_
#output: [ 0.92461621  0.05301557]
pc1, pc2 = pca.explained_variance_ratio_ #保存2个PC

print 1-sum(pca.explained_variance_ratio_)
#output:0.0223682249752
print 1.0-pc1-pc2 #等价于上述输出

#逆变换还原数据
data_inv = pca.inverse_transform(pcad)
#比较还原后数据和原始数据的相似度
print abs(sum(sum(data - data_inv)))
#output:6.66133814775e-15

#循环尝试：PC数量从1维到4维（原始数据也是4维）
#看PCA覆盖信息量；4个肯定100%，3个也很高了；
for i in range(1,5):
    pca = PCA(n_components=i)
    pca.fit(data)
    print sum(pca.explained_variance_ratio_) * 100,'%'

#output:92.4616207174 %
#output:97.7631775025 %
#output:99.481691455 %
#output:100.0 %