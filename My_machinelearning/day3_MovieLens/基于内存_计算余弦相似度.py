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

#使用sklearn的pairwise_distances函数来计算余弦相似性。注意，输出范围从0到1，因为打分都是正的。
from sklearn.metrics.pairwise import pairwise_distances
user_similarity = pairwise_distances(train_data_matrix, metric='cosine')
item_similarity = pairwise_distances(train_data_matrix.T, metric='cosine')

#下一步是做出预测。你已经创建了相似性矩阵：user_similarity和item_similarity，因此，你可以通过为基于用户的CF应用下面的公式做出预测：
# 你可以将用户k和a之间的相似性看成权重，它乘以相似用户a (校正的平均评分用户)的评分。你需要规范化该值，使打分位于1到5之间，
# 最后，对你尝试预测的用户的平均评分求和。这里的想法是，某些用户可能会倾向于对所有的电影，总是给予高或低评分。这些用户提供的评分的
# 相对差比绝对评分值更重要。举个例子：假设，用户k对他最喜欢的电影打4星，而对所有其他的好电影打3星。现在假设另一个用户t对他/她喜欢的
# 电影打5星，而对他/她感到无聊的电影打3星。那么这两个用户可能品味非常相似，但对打分系统区别对待。当为基于产品的CF进行预测时，你无须纠正
# 用户的平均打分，因为查询用户本事就是用来做预测的。

def predict(ratings, similarity, type='user'):
    if type == 'user':
        mean_user_rating = ratings.mean(axis=1)
        # You use np.newaxis so that mean_user_rating has same format as ratings
        ratings_diff = (ratings - mean_user_rating[:, np.newaxis])
        pred = mean_user_rating[:, np.newaxis] + similarity.dot(ratings_diff) / np.array(
            [np.abs(similarity).sum(axis=1)]).T
    elif type == 'item':
        pred = ratings.dot(similarity) / np.array([np.abs(similarity).sum(axis=1)])
    return pred

item_prediction = predict(train_data_matrix, item_similarity, type='item')
user_prediction = predict(train_data_matrix, user_similarity, type='user')

#最受欢迎的用来度量预测评分的准确性的指标是均方根误差 (RMSE)。可以使用sklearn的mean_square_error (MSE)函数，其中，RMSE仅仅是MSE的平方根。
# 只是想要考虑测试数据集中的预测评分，因此，使用prediction[ground_truth.nonzero()]筛选出预测矩阵中的所有其他元素。
from sklearn.metrics import mean_squared_error
from math import sqrt
def rmse(prediction, ground_truth):
    prediction = prediction[ground_truth.nonzero()].flatten()
    ground_truth = ground_truth[ground_truth.nonzero()].flatten()
    return sqrt(mean_squared_error(prediction, ground_truth))

print ('User-based CF RMSE: ' + str(rmse(user_prediction, test_data_matrix)))
print ('Item-based CF RMSE: ' + str(rmse(item_prediction, test_data_matrix)))