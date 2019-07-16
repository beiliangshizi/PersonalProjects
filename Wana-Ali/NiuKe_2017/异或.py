# *_*coding:utf-8 *_*
# date:
__author__ = 'beiliangshizi'

# 题目描述
# 给定整数m以及n各数字A1,A2,..An，将数列A中所有元素两两异或，共能得到n(n-1)/2个结果，请求出这些结果中大于m的有多少个。
# 输入描述:
# 第一行包含两个整数n,m.
#
# 第二行给出n个整数A1，A2，...，An。
#
# 数据范围
#
# 对于30%的数据，1 <= n, m <= 1000
#
# 对于100%的数据，1 <= n, m, Ai <= 10^5
# 输出描述:
# 输出仅包括一行，即所求的答案
# 示例1
# 输入
#
# 3 10
# 6 5 10
# 输出
#
# 2

# # include <cstdio>
# # include <cstring>
#
# const
# int
# N = 100010;
#
# int
# a[N];
#
# struct
# node
# {
#     int
# count;
# int
# next[2];
# }p[N * 17], root;
#
# int
# cnt = 0;
# void
# insert(int * a, int
# len) {
#     int
# now = 0;
# for (int
# i = 0;
# i < len;
# ++i) {
# if (p[now].next[a[i]] == -1)
# {
#     cnt + +;
# p[cnt].next[0] = p[cnt].next[1] = -1;
# p[cnt].count = 0;
# p[now].next[a[i]] = cnt;
# }
# now = p[now].next[a[i]];
# p[now].count + +;
# }
# }
#
# typedef
# long
# long
# LL;
# int
# query(int * a, int * b, int
# len) {
#     int
# now = 0;
# int
# ret = 0;
# for (int
# i = 0;
# now != -1 & & i < len;
# ++i) {
# if (b[i] == 0)
# {
# if (p[now].next[1 ^ a[i]] != -1)
# ret += p[p[now].next[1 ^ a[i]]].count;
# now = p[now].next[a[i]];
# }
# else {
#     now = p[now].next[1 ^ a[i]];
# }
# }
# return ret;
# }
#
#
# int
# main()
# {
# int
# n, m;
# while (scanf("%d%d", & n, & m) == 2) {
# cnt = 0;
# p[0].next[0] = p[0].next[1] = -1;
# p[0].count = 0;
# for (int i = 0; i < n; ++i) {
# scanf("%d", & a[i]);
# int tmp[18];
# for (int j = 0; j < 18; ++j)
# tmp[j] = (a[i] >> (17 - j)) & 1;
# insert(tmp, 18);
# // for (int i = 0; i < 30; ++i) printf("%d ", p[i].count);
# // puts("----");
# }
# int kk[18];
# for (int j = 0; j < 18; ++j)
# kk[j] = (m >> (17 - j)) & 1;
# LL ret = 0;
# for (int i = 0; i < n; ++i) {
# int tmp[18];
# for (int j = 0; j < 18; ++j)
# tmp[j] = (a[i] >> (17 - j)) & 1;
# ret += query(tmp, kk, 18);
# // printf("%d\n", ret);
# }
# printf("%lld\n", ret / 2);
# }
# return 0;
# }
