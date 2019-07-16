# *_*coding:utf-8 *_*
# date:
__author__ = 'beiliangshizi'


# 题目描述
# 牛牛和 15 个朋友来玩打土豪分田地的游戏，牛牛决定让你来分田地，地主的田地可以看成是一个矩形，每个位置有一个价值。
# 分割田地的方法是横竖各切三刀，分成 16 份，作为领导干部，牛牛总是会选择其中总价值最小的一份田地， 作为牛牛最好的朋友，
# 你希望牛牛取得的田地的价值和尽可能大，你知道这个值最大可以是多少吗？
# 输入描述:
# 每个输入包含 1 个测试用例。每个测试用例的第一行包含两个整数 n 和 m（1 <= n, m <= 75），表示田地的大小，
# 接下来的 n 行，每行包含 m 个 0-9 之间的数字，表示每块位置的价值。
# 输出描述:
# 输出一行表示牛牛所能取得的最大的价值。
# 示例1
# 输入
#
# 4 4
# 3332
# 3233
# 3332
# 2323
# 输出
#
# 2

##########   C++

# # include <iostream>
# # include <vector>
# # include <string>
# # include <algorithm>
# # include <climits>
# # include <cstring>
# # include <cstdio>
# # include <fstream>
# # include <ctime>
# # include <map>
# # include <unordered_set>
# # include <unordered_map>
# # include <deque>
# # include <set>
# # include <functional>
# using
# std::cin;
# using
# std::cout;
#
# int
# n, m, array[75][75], x[3], y[3];
#
# bool
# check(int
# s){
# for (x[0] = 0; x[0] < m - 3; ++x[0]){
# if (array[n - 1][x[0]] < 4 * s)
# continue;
# for (x[1] = x[0] + 1; x[1] < m - 2; ++x[1]){
# if (array[n - 1][x[1]] - array[n - 1][x[0]] < 4 * s)
# continue;
# for (x[2] = x[1] + 1; x[2] < m - 1; ++x[2]){
# if (array[n - 1][x[2]] - array[n - 1][x[1]] < 4 * s | | array[n - 1][m - 1] - array[n - 1][x[2]] < 4 * s)
# continue;
# for (y[0] = 0; y[0] < n - 3; ++y[0]){
# if (array[y[0]][x[0]] < s | | array[y[0]][x[1]] - array[y[0]][x[0]] < s | |
# array[y[0]][x[2]] - array[y[0]][x[1]] < s | | array[y[0]][m - 1] - array[y[0]][x[2]] < s)
# continue;
# for (y[1] = y[0] + 1; y[1] < n - 2; ++y[1]){
# if (array[y[1]][x[0]] - array[y[0]][x[0]] < s | |
# array[y[1]][x[1]] - array[y[1]][x[0]] - array[y[0]][x[1]] + array[y[0]][x[0]] < s | |
# array[y[1]][x[2]] - array[y[1]][x[1]] - array[y[0]][x[2]] + array[y[0]][x[1]] < s | |
# array[y[1]][m - 1] - array[y[1]][x[2]] - array[y[0]][m - 1] + array[y[0]][x[2]] < s)
# continue;
# for (y[2] = y[1] + 1; y[2] < n - 1; ++y[2]){
# if (array[y[2]][x[0]] - array[y[1]][x[0]] < s | |
# array[y[2]][x[1]] - array[y[2]][x[0]] - array[y[1]][x[1]] + array[y[1]][x[0]] < s | |
# array[y[2]][x[2]] - array[y[2]][x[1]] - array[y[1]][x[2]] + array[y[1]][x[1]] < s | |
# array[y[2]][m - 1] - array[y[2]][x[2]] - array[y[1]][m - 1] + array[y[1]][x[2]] < s)
# continue;
# else if (array[n - 1][x[0]] - array[y[2]][x[0]] < s | |
#                 array[n - 1][x[1]] - array[n - 1][x[0]] - array[y[2]][x[1]] + array[y[2]][x[0]] < s | |
#                 array[n - 1][x[2]] - array[n - 1][x[1]] - array[y[2]][x[2]] + array[y[2]][x[1]] < s | |
#                 array[n - 1][m - 1] - array[n - 1][x[2]] - array[y[2]][m - 1] + array[y[2]][x[2]] < s)break;
# return true;
# }
# }
# }
# }
# }
# }
# return false;
# }
#
# int
# main()
# {
# cin >> n >> m;
# for (int i = 0; i < n; ++i)
# for (int j = 0; j < m; ++j){
# char c;
# cin >> c;
# array[i][j] = c - '0';
# if (i > 0)array[i][j] += array[i - 1][j];
# if (j > 0)array[i][j] += array[i][j - 1];
# if (i > 0 & & j > 0)array[i][j] -= array[i - 1][j - 1];
# }
# int
# b = 0, e = 75 * 75 * 9;
# while (b < e - 1){
# int mid = (b + e) / 2;
# if (check(mid))b = mid;
# else e = mid;
# }
# cout << b << '\n';
# }