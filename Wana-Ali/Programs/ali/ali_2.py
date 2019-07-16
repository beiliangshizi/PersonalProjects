# *_*coding:utf-8 *_*
# date:
__author__ = 'beiliangshizi'



import sys
matrix = input()
length = len(matrix)
Min_brick = 100000

for i in range(length):
    for j in range(len(matrix[i])-1):
        flag = 0
        sum_i = sum(matrix[i][:j+1])
        for k in range(length):
            if k != i:
                for p in range(len(matrix[k])-1):
                    sum_p = sum(matrix[k][:p+1])
                    if sum_p == sum_i:
                        flag += 1
        min_brick = length - flag -1
        Min_brick = min(Min_brick,min_brick)
print Min_brick




















# import sys
# if __name__ == "__main__":
#     result= 0
#     dataList = input() #[[1,2,2,1],[3,2,1],[1,1,1,1,1,1],[2,1,1,2],[4,2]]    raw_input()输入
#     lens=len(dataList)  #长度为5
#     #print dataList[0] #打印input输入的list的中第一个list的值
#     wallwidth=sum(map(int,dataList[0]))      #dataList[0]为[1,2,2,1]
#     for index in xrange(1,wallwidth):   #线从长为1开始画，每次加1循环  循环计算每一行中line画中的空格数count
#         count=0
#         for col in xrange(lens): #每一行循环计算line的值和每一行中每一个值与line比较大小如[1,2,2,1]计算1与line=1是否相等，
#             #相等则break，如果比line小,计算数组中第一个数list[0]与第二个数list[1]之和比line是否相等，比line的值大则break
#             sumnum=0
#             for row in xrange(len(dataList[col])):
#                 #data_1="-".join(map(str,dataList[col]))   #1,2,2,1
#                 #print ("data_1:%s  line:%s col:%s row:%s data_1.split('-')[row]:%s" %(data_1,index,col,row,data_1.split("-")[row]))
#                 #sumnum=sumnum+int(data_1.split("-")[row])
#                 sumnum=sumnum+dataList[col][row]
#                 if(sumnum==index):
#                     count=count+1
#                     break
#                 if(sumnum>index):
#                     break
#         print("count:%s result:%s" %(count,result))
#         if(result<count):
#             result=count
#     minwall=lens-result
#     print str(minwall) + "\n"