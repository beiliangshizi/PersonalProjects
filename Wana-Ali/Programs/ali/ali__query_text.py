# *_*coding:utf-8 *_*
# date:
__author__ = 'beiliangshizi'

# 题目描述：给定一个query和一个text，均由小写字母组成。要求在text中找出以同样的顺序连续出现在query中的最长连续
# 字母序列的长度。例如，query为“acbac”，text为“acaccbabb”，那么text中的“cba”为最长的连续出现在query中的
# 字母序列，因此，返回结果应该为其长度3。请注意程序效率。
#
# 思路：用一个矩阵来记录两个字符串中所有位置的两个字符之间的匹配情况，若是匹配则为1，否则为0。
# 然后求出对角线最长的1序列，其对应的位置就是最长匹配子串的位置.
#
# 当字符匹配的时候，不是简单的给相应元素赋上1，而是赋上其左上角元素的值加1。
# 我们用两个标记变量来标记矩阵中值最大的元素的位置，在矩阵生成的过程中来判断当前生成的元素的值是不是最大的，
# 据此来改变标记变量的值，那么到矩阵完成的时候，最长匹配子串的位置和长度就已经出来了。
#
# 实例如下：
#
#      a    c    b    a    c
#
# a   1    0    0    1    0
#
# c   0    2    0    0    2
#
# a   1    0    0    1    0
#
# c   0    2    0    0    2
#
# c   0    1    0    0    1
#
# b   0    0    2    0    0
#
# a   1    0    0    3    0
#
# b   0    0    1    0    0
#
# b   0    0    1    0    0


def largest_common(query, text, is_first_same):
    if (len(query) == 0 or len(text) == 0):
        return 0
    else:
        a = query[0]
        b = text[0]
        if is_first_same:
            if (a == b):
                first_same_l = largest_common(query[1:], text[1:], True) + 1
            else:
                first_same_l = 0
            first_diff_l = max(largest_common(query[1:], text[0:], False), largest_common(query[0:], text[1:], False))
        else:
            if (a == b):
                first_same_l = largest_common(query[1:], text[1:], True)
            else:
                first_same_l = 0
            first_diff_l = max(largest_common(query[1:], text[0:], False), largest_common(query[0:], text[1:], False))
        if first_same_l > first_diff_l:
            return first_same_l
        else:
            return first_diff_l


if __name__ == '__main__':
    a = "acbac"
    b = "accbaccbabb"
    print largest_common(a, b, True)




    # #include <cstring>
# #include <cstdio>
# #define M 1010
#
# int LCS(char query[], char text[])
# {
#     int len_query=strlen(query),len_text=strlen(text);
#
#     //数组c记录匹配情况,模拟二维矩阵
#     char c[len_text];
#     int len, i, j;
#     len=0;
#
#     for(i=0; i<len_query; i++)
#     {
#         //不反过来会把之前数组元素冲掉的，因为后面的元素需要根据前面的元素计算
#         for(j=len_text-1; j>=0; j--)
#         {
#             if(query[i] == text[j])
#             {
#                 if(i==0 || j==0)
#                     c[j]=1;
#                 else
#                     c[j]=c[j-1]+1;
#             }
#             else
#                 c[j] = 0;
#
#             if(c[j] > len)
#                 len=c[j];
#         }
#     }
#     return len;
# }
#
# int main()
# {
#     char str1[M],str2[M];
#     printf("请输入字符串query:");
#
#     fgets(str1,1000,stdin);
#     printf("请输入字符串text:");
#
#     fgets(str2,1000,stdin);
#     printf("所求长度为:");
#
#     printf("%d\n",LCS(str1,str2));
#     return 0;
#
# }