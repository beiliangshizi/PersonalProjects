import numpy as np
import pandas as pd

header = ['user_id', 'item_id', 'rating', 'timestamp']
df = pd.read_csv('./ml-100k/u.data', sep='\t', names=header)
n_users = df.user_id.unique().shape[0]
n_items = df.item_id.unique().shape[0]
print ('Number of users = ' + str(n_users) + ' | Number of movies = ' + str(n_items))


# 使用scikit-learn库将数据集分割成测试和训练。Cross_validation.train_test_split根据测试样本的比例（test_size），
# 本例中是0.25，来将数据混洗并分割成两个数据集。
from sklearn import cross_validation as cv
train_data, test_data = cv.train_test_split(df, test_size=0.25)

# Create two user-item matrices, one for training and another for testing
#创建用户-产品矩阵。由于你既有测试数据，又有训练数据，那么你需要创建两个矩阵。
train_data_matrix = np.zeros((n_users, n_items))
for line in train_data.itertuples():
    train_data_matrix[line[1] - 1, line[2] - 1] = line[3]

test_data_matrix = np.zeros((n_users, n_items))
for line in test_data.itertuples():
    test_data_matrix[line[1] - 1, line[2] - 1] = line[3]

#-----------------------------------------------------------------------------------------------------------#

# 基于模型的协同过滤是基于矩阵分解（MF），它已获得更大的曝光，它主要是作为潜变量分解和降维的一个无监督学习方法。
# 矩阵分解广泛用于推荐系统，其中，它比基于内存的CF可以更好地处理与扩展性和稀疏性. MF的目标是从已知的评分中学习用户的
# 潜在喜好和产品的潜在属性（学习描述评分特征的特征），随后通过用户和产品的潜在特征的点积预测未知的评分。
# 当你有一个非常稀疏的多维矩阵时，通过进行矩阵分解可以调整用户-产品矩阵为低等级的结构，然后你可以通过两个低秩矩阵
# （其中，每行包含该本征矢量，即特征向量）的乘积来代表该矩阵。你通过将低秩矩阵相乘，在原始矩阵填补缺少项，以调整这个矩阵，
# 从而尽可能的近似原始矩阵。

# 计算MovieLens数据集的稀疏度
sparsity=round(1.0-len(df)/float(n_users*n_items),3)
print ('The sparsity level of MovieLens100K is ' +  str(sparsity*100) + '%')

# CF模型仅使用数据（user_id, movie_id, rating）来学习潜在特征。如果只有少数可用的数据，那么基于模型的CF模式将预测不良，
# 因为这将更难以学习潜在特征。

# 同时使用评分和内容特性的模型称为混合推荐系统，其中，协同过滤和基于内容的模型相结合。混合推荐系统通常比协同过滤或
# 基于内容的模型自身表现出更高的精度：它们有能力更好的解决冷启动问题，因为如果你没有一个用户或者一个产品的评分，
# 那么你可以使用该用户或产品的元数据进行预测。

# 一个众所周知的矩阵分解方法是奇异值分解(SVD)。通过使用奇异值分解，协同过滤可以被近似一个矩阵X所制定。
# 一般的方程可以表示为：X=USV^T
# 给定m x n矩阵X：
# U是一个(m x r)正交矩阵
# S是一个对角线上为非负实数的(r x r)对角矩阵
# V^T是一个(r x n)正交矩阵
# S的对角线上的元素被称为X的奇异值。
# 矩阵X可以被分解成U，S和V。U矩阵表示对应于隐藏特性空间中的用户的特性矩阵，而V矩阵表示对应于隐藏特性空间中的产品的特性矩阵。
import scipy.sparse as sp
from scipy.sparse.linalg import svds
from day3_MovieLens.基于内存_计算余弦相似度 import rmse

# get SVD components from train matrix. Choose k.
u, s, vt = svds(train_data_matrix, k=20)
s_diag_matrix = np.diag(s)
X_pred = np.dot(np.dot(u, s_diag_matrix), vt)

print ('User-based CF MSE: ' + str(rmse(X_pred, test_data_matrix)))

#SVD可能会非常缓慢，并且计算成本比较高。更近期的工作通过应用交替最小二乘或随机梯度下降最小化平方误差，并使用正则项以防止过度拟合。


















