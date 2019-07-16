# *_*coding:utf-8 *_*
# date:
__author__ = 'beiliangshizi'


#NetworkX提供了4种常见网络的建模方法，分别是：规则图，ER随机图，WS小世界网络和BA无标度网络。


#------------------------------------------------------------------------------------------#
# 则图差不多是最没有复杂性的一类图，random_graphs.random_regular_graph(d, n)方法可以生成一个含有n个节点，
# 每个节点有d个邻居节点的规则图。

import networkx as nx
import matplotlib.pyplot as plt

# regular graphy
# generate a regular graph which has 20 nodes & each node has 3 neghbour nodes.
RG = nx.random_graphs.random_regular_graph(3, 20)
# the spectral layout
pos = nx.spectral_layout(RG)
# draw the regular graphy
nx.draw(RG, pos, with_labels = False, node_size = 30)
plt.show()



#------------------------------------------------------------------------------------------#

# ER随机图是早期研究得比较多的一类“复杂”网络，模型的基本思想是以概率p连接N个节点中的每一对节点。用
# random_graphs.erdos_renyi_graph(n,p)方法生成一个含有n个节点、以概率p连接的ER随机图：

import networkx as nx
import matplotlib.pyplot as plt

# erdos renyi graph
# generate a graph which has n=20 nodes, probablity p = 0.2.
ER = nx.random_graphs.erdos_renyi_graph(20, 0.2)
# the shell layout
pos = nx.shell_layout(ER)
nx.draw(ER, pos, with_labels = False, node_size = 30)
plt.show()

#------------------------------------------------------------------------------------------#
# 　用random_graphs.watts_strogatz_graph(n, k, p)方法生成一个含有n个节点、每个节点有k个邻居、
# 以概率p随机化重连边的WS小世界网络。

import networkx as nx
import matplotlib.pyplot as plt

# WS network

# generate a WS network which has 20 nodes,
# each node has 4 neighbour nodes,
# random reconnection probability was 0.3.
WS = nx.random_graphs.watts_strogatz_graph(20, 4, 0.3)
# circular layout
pos = nx.circular_layout(WS)
nx.draw(WS, pos, with_labels = False, node_size = 30)
plt.show()

#------------------------------------------------------------------------------------------#
# 　　用random_graphs.barabasi_albert_graph(n, m)方法生成一个含有n个节点、每次加入m条边的BA无标度网络。

import networkx as nx
import matplotlib.pyplot as plt

# BA scale-free degree network
# generalize BA network which has 20 nodes, m = 1
BA = nx.random_graphs.barabasi_albert_graph(20, 1)
# spring layout
pos = nx.spring_layout(BA)
nx.draw(BA, pos, with_labels = False, node_size = 30)
plt.show()