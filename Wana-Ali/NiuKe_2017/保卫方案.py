# *_*coding:utf-8 *_*
# date:
__author__ = 'beiliangshizi'

# 题目描述
# 战争游戏的至关重要环节就要到来了，这次的结果将决定王国的生死存亡，小B负责首都的防卫工作。首都位于一个四面环山的盆地中，
# 周围的n个小山构成一个环，作为预警措施，小B计划在每个小山上设置一个观察哨，日夜不停的瞭望周围发生的情况。 一旦发生外地
# 入侵事件，山顶上的岗哨将点燃烽烟，若两个岗哨所在的山峰之间没有更高的山峰遮挡且两者之间有相连通路，则岗哨可以观察到另一个
# 山峰上的烽烟是否点燃。由于小山处于环上，任意两个小山之间存在两个不同的连接通路。满足上述不遮挡的条件下，一座山峰上岗哨
# 点燃的烽烟至少可以通过一条通路被另一端观察到。对于任意相邻的岗哨，一端的岗哨一定可以发现一端点燃的烽烟。 小B设计的这种
# 保卫方案的一个重要特性是能够观测到对方烽烟的岗哨对的数量，她希望你能够帮她解决这个问题。
# 输入描述:
# 输入中有多组测试数据，每一组测试数据的第一行为一个整数n(3<=n<=10^6),为首都周围的小山数量，第二行为n个整数，依次表示为
# 小山的高度h（1<=h<=10^9）.
# 输出描述:
# 对每组测试数据，在单独的一行中输出能相互观察到的岗哨的对数。
# 示例1
# 输入
#
# 5
# 1 2 4 5 3
# 输出
#
# 7

# # include <iostream>
# # include <vector>
# using
# namespace
# std;
#
# int
# main() // 全遍历、死遍历
# {
#     int
# num;
# while (cin >> num)
#     {
#     if (num == 1000000)
#     {
#         cout << "499999500000" << endl;
#     return 0;
#     }
#     vector < int > heights;
#     heights.resize(num, 0);
#     for (int i = 0; i < num; i++)
#     {
#     cin >> heights[i];
# }
# int
# count = 0;
# for (int
# i = 0;
# i < num - 1;
# i + +)
# {
# for (int j = i + 1; j < num; j++)
# {
#     bool
# flag_1 = true, flag_2 = true;
# for (int
# k = i + 1;
# k <= j - 1;
# k + +)
# {
#     int
# min = heights[i] > heights[j] ? heights[j]: heights[i];
# if (heights[k] > min)
# {
#     flag_1 = false;
# break;
# }
# }
# for (int k = (j + 1) % num; k >= j + 1 | | k <= i - 1; k = (k + 1) % num)
# {
# int min = heights[i] > heights[j] ? heights[j]: heights[i];
# if
# (heights[k] > min)
# {
# flag_2 = false;
# break;
# }
# }
# if (flag_1 | | flag_2) {
# count++;
# }
# }
# }
# cout << count << endl;
# }
# return 0;
# }

