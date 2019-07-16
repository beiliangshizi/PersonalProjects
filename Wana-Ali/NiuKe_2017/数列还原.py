# *_*coding:utf-8 *_*
# date:
__author__ = 'beiliangshizi'

# 题目描述
# 牛牛的作业薄上有一个长度为 n 的排列 A，这个排列包含了从1到n的n个数，但是因为一些原因，其中有一些位置（不超过 10 个）
# 看不清了，但是牛牛记得这个数列顺序对的数量是 k，顺序对是指满足 i < j 且 A[i] < A[j] 的对数，请帮助牛牛计算出，
# 符合这个要求的合法排列的数目。
# 输入描述:
# 每个输入包含一个测试用例。每个测试用例的第一行包含两个整数 n 和 k（1 <= n <= 100, 0 <= k <= 1000000000），
# 接下来的 1 行，包含 n 个数字表示排列 A，其中等于0的项表示看不清的位置（不超过 10 个）。
# 输出描述:
# 输出一行表示合法的排列数目。
# 示例1
# 输入
#
# 5 5
# 4 0 0 2 0
# 输出
#
# 2

def sequence(n, k, A):
    def right_seq(remain, zero_loc, diff_list, A):
        if remain < 0 or (remain > 0 and len(zero_loc) <= 0):
            # print "not right",remain,A
            return 0
        if remain == 0 and len(zero_loc) == 0:
            # print "====right====",A
            return 1
        result = 0
        for i in range(len(diff_list)):
            A[zero_loc[0]] = diff_list[i]
            # 计算新增的合法排列数
            new_add = 0
            for j in range(len(A)):
                if A[j] != 0 and (
                    (j < zero_loc[0] and A[j] < A[zero_loc[0]]) or (j > zero_loc[0] and A[j] > A[zero_loc[0]])):
                    new_add += 1
            # print "A, newadd",A,new_add
            result += right_seq(remain - new_add, zero_loc[1:], diff_list[:i] + diff_list[i + 1:], A)
            A[zero_loc[0]] = 0
        return result

    # 缺失的数据
    n_list = [i for i in range(0, n + 1)]
    diff_list = list(set(n_list) ^ set(A))
    # print "diff_list",diff_list

    # 缺失数据的位置
    zero_loc = []
    for i in range(n):
        if A[i] == 0:
            zero_loc.append(i)
    # print "zero_loc",zero_loc
    origin_pair_num = 0
    for i in range(n - 1):
        if A[i] != 0:
            for j in range(i + 1, n):
                if A[j] > A[i]:
                    origin_pair_num += 1
    # print "origin_pair_num",origin_pair_num

    return right_seq(k - origin_pair_num, zero_loc, diff_list, A)


if __name__ == '__main__':
    firstline = raw_input()
    secondline = raw_input()
    n, k = [int(i) for i in firstline.strip().split(' ')]
    A = [int(i) for i in secondline.strip().split(' ')]
    print sequence(n, k, A)