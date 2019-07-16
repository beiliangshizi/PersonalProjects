# *_*coding:utf-8 *_*
# date:
__author__ = 'beiliangshizi'

# 题目描述
# 继MIUI8推出手机分身功能之后，MIUI9计划推出一个电话号码分身的功能：首先将电话号码中的每个数字加上8取个位，然后使用
# 对应的大写字母代替 （"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"），
# 然后随机打乱这些字母，所生成的字符串即为电话号码对应的分身。
# 输入描述:
# 第一行是一个整数T（1 ≤ T ≤ 100)表示测试样例数；接下来T行，每行给定一个分身后的电话号码的分身（长度在3到10000之间）。
#
# 输出描述:
# 输出T行，分别对应输入中每行字符串对应的分身前的最小电话号码（允许前导0）。
# 示例1
# 输入
#
# 4
# EIGHT
# ZEROTWOONE
# OHWETENRTEO
# OHEWTIEGTHENRTEO
# 输出
#
# 0
# 234
# 345
# 0345

def deriveNum(str):
    n = [0 for i in range(10)]
    n[0] = str.count('Z')
    n[2] = str.count('W')
    n[6] = str.count('X')
    n[8] = str.count('G')
    n[7] = str.count('S') - n[6]
    n[5] = str.count('V') - n[7]
    n[4] = str.count('F') - n[5]
    n[3] = str.count('H') - n[8]
    n[1] = str.count('O') - n[0] - n[2] - n[4]
    n[9] = str.count('I') - n[5] - n[6] - n[8]
    """
    tab = [0 for i in range(26)]
    for s in str:
        tab[ord(s)-ord('A')] +=1
    if tab[ord('Z')-ord('A')]:
        tmp = tab[ord('Z')-ord('A')]    # the number of symbol 0
        n[0]=tmp
        tab[ord('Z')-ord('A')] = 0
        tab[ord('E')-ord('A')] -=tmp
        tab[ord('R')-ord('A')] -=tmp
        tab[ord('O')-ord('A')] -=tmp

    if tab[ord('W')-ord('A')]:
        tmp = tab[ord('W')-ord('A')]    # the number of symbol 2
        n[2]=tmp
        tab[ord('W')-ord('A')] = 0
        tab[ord('T')-ord('A')] -=tmp
        tab[ord('O')-ord('A')] -=tmp


    if tab[ord('X')-ord('A')]: 
        tmp = tab[ord('S')-ord('A')]    # the number of symbol 6
        n[6]=tmp
        tab[ord('X')-ord('A')] = 0
        tab[ord('S')-ord('A')] -=tmp
        tab[ord('I')-ord('A')] -=tmp

    if tab[ord('G')-ord('A')]:
        tmp = tab[ord('G')-ord('A')]   # the number of symbol 8
        n[8]=tmp
        tab[ord('G')-ord('A')] = 0
        tab[ord('E')-ord('A')] -=tmp
        tab[ord('I')-ord('A')] -=tmp
        tab[ord('H')-ord('A')] -=tmp
        tab[ord('T')-ord('A')] -=tmp

    if tab[ord('S')-ord('A')]:    # S only in 6 and 7
        tmp = tab[ord('G')-ord('A')]    # the number of symbol 7
        n[7]=tmp
        tab[ord('S')-ord('A')] = 0
        tab[ord('E')-ord('A')] -=2*tmp
        tab[ord('V')-ord('A')] -=tmp
        tab[ord('N')-ord('A')] -=tmp

    if tab[ord('V')-ord('A')]:    #V only for 5 and 7, since 7 has been removed
        tmp = tab[ord('V')-ord('A')]    # the number of symbol 5
        n[5]=tmp
        tab[ord('V')-ord('A')] = 0
        tab[ord('F')-ord('A')] -=tmp
        tab[ord('I')-ord('A')] -=tmp
        tab[ord('E')-ord('A')] -=tmp

    if tab[ord('F')-ord('A')]:    #V only for 5 and 4, since 5 has been removed
        tmp = tab[ord('F')-ord('A')]    # the number of symbol 4
        n[4]=tmp
        tab[ord('F')-ord('A')] = 0
        tab[ord('I')-ord('A')] -=tmp
        tab[ord('V')-ord('A')] -=tmp
        tab[ord('E')-ord('A')] -=tmp

    if tab[ord('I')-ord('A')]:    # I only in 6,8,9
        tmp = tab[ord('I')-ord('A')]   # the number of 9
        n[9]=tmp
        tab[ord('I')-ord('A')] = 0
        tab[ord('N')-ord('A')] -=2*tmp
        tab[ord('E')-ord('A')] -=tmp

    if tab[ord('T')-ord('A')]:    # I only in 2,3,8
        tmp = tab[ord('T')-ord('A')]   # the number of 3
        n[3] =tmp
        tab[ord('T')-ord('A')] = 0
        tab[ord('H')-ord('A')] -=tmp
        tab[ord('R')-ord('A')] -=tmp
        tab[ord('2')-ord('A')] -=2*tmp

    if tab[ord('O')-ord('A')]:
        tmp = tab[ord('O')-ord('A')]   # the number of 1
        n[1]=tmp
        tab[ord('O')-ord('A')] = 0
        tab[ord('N')-ord('A')] -=tmp
        tab[ord('E')-ord('A')] -=tmp
    """
    return n


t = input()
for i in range(t):
    line = raw_input()
    n1 = deriveNum(line)
    n = n1[8:10] + n1[0:9]
    out = ''
    for i in range(10):
        out = out + n[i] * str(i)
    print out