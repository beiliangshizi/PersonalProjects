# *_*coding:utf-8 *_*
# date:
__author__ = 'beiliangshizi'



# import sys
# sys.setrecursionlimit(1000000) #设置递归深度，例如这里设置为一百万


# /** 请完成下面这个函数，实现题目要求的功能 **/
# /** 当然，你也可以不按照这个模板来作答，完全按照自己的想法来 ^-^  **/

def findCircleNum(M,rows,cols):
    sl = []
    if rows == cols :
        for i in range(rows):
            i_l = []
            for j in range(i,rows):
                if M[i][j] == 1 :
                    i_l.append(j+1)
            flag = 0
            for k in sl:
                if (i+1) in k:
                    k.extend(i_l)
                    flag = 1
            if flag == 0:
                sl.append(i_l)
        # print sl
        return len(sl)
    return




# _M_rows = 0
# _M_cols = 0
# _M_rows = int(raw_input())
# _M_cols = int(raw_input())
#
# _M = []
# for _M_i in xrange(_M_rows):
#     _M_temp = map(int, raw_input().strip().split(' '))
#     _M.append(_M_temp)

# _M = [[1,1,0],[1,1,0],[0,0,1]]
_M = [ [1,1,0,0,0,0], [1,1,0,0,0,0],
    [0,0,1,0, 0,0], [0,0,0,1,0,1], [0,0,0,0,1,0], [0,0,0,1,0,1]]
_M_rows = 6
_M_cols = 6
res = findCircleNum(_M,_M_rows,_M_cols)

print str(res) + "\n"






# import sys
# def CaculatePeopleGroup():
#     res=0
#     data_row= input()     #raw_input()输入二维数组的行数
#     data_col = input()  #raw_input()输入二维数组的列数
#     dataList=[]  ##[[1,1,0,0],[1,1,1,0],[0,1,0,1],[0,0,0,1]]
#     resList=[]
#     if(data_row==data_col):
#         for i in xrange(data_row):#循环输入行数次 0,1,2，data_row-1停
#             data_i=list(sys.stdin.readline().strip().split()) #1,1,0,0       # 1 1 0 0 0 0
#             dataList.append(data_i)  #如何输入1 1 0 0 0 0
#             #print ("value:%s data_i:%s" %(dataList,data_i))
#             stmList=[]
#             for col in xrange(i,len(data_i)):
#                 #print("data_i[i]:%s data_i[col]):%s" % (data_i[i], data_i[col]))
#                 if(data_i[i]==data_i[col]) and (int(data_i[col])==1) :
#                     stmList.append(col+1)   #得到和自己是朋友的有哪些人
#                     #print("stmList:%s col:%s" %(stmList,col))
#             resList.append(stmList)  #[[1,2],[2],[3],[4,6],[5],[6]] 第一个list表示1只与2是朋友，第二list表示2没有与2后面的人是朋友，第四个list表示4与后面的6是朋友
#         #print("resList:%s" % resList)
#     else:
#         print "Error:输入的数据不正确"
#     delList=[]
#     for i in xrange(len(resList)):  #len(resList)为6  index为0 resList[index]为[1,2]
#         #print ("reslist[i]:%s len(resList):%d  resList:%s" %(resList[i],len(resList),resList))
#         for j in xrange(i+1,len(resList)):#循环resList[index]后面的值
#                 #print ("reslist[j]:%s len(resList):%d  resList:%s  j:%s" % (resList[j], len(resList),resList,j))
#                 for i_i in xrange(len(resList[i])):
#                     for j_j in xrange(len(resList[j])):
#                         #print("resList[%s][%s]:%s resList[%s][%s]):%s" % (i,i_i,resList[i][i_i],j,j_j, resList[j][j_j]))
#                         if(resList[i][i_i]==resList[j][j_j]):
#                             if(len(resList[j])>1):
#                                 resList[i].append(resList[j])
#                             #print resList[j]  #打印有相同朋友
#                             delList.append(resList[j]) #删除后面重复的数
#                             break
#     for del_i in delList:
#         if(del_i in resList):
#             #print del_i
#             resList.remove(del_i)
#     #print("resList222222222:%s" % resList)
#     res=len(resList)
#     return res
#
# if __name__ == "__main__":
#     result=CaculatePeopleGroup()
#     print str(result)+"\n"