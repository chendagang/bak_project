__author__ = 'cdg'
# -*- coding: utf-8 -*-
from numpy import *
import string
#############################################
#用户向量u=(0.7, 0.2, 0.1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0),从题目来看每个用户向量
# 都做了归一化处理（行加和等于1），每一维值的大小代表了对类别的喜好程度
#物品向量i=(0.3, 0.1, 0.5, 0.1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0),每一维值的大小代表了
# 所属类别的可能性大小
#算法描述：1.取出用户向量中的非零项
#        2.取出第一步中非零项的所有的维度值（即由1000维列向量构成）
#        3.按照降序排列第2步中的列向量
#        4.取出3步中topN(N值由第一步非零向量的值×10确定，如第0维就取top7，第1维就取top2)
#
#############################################
class RandomRecomm(object):
    def __init__(self):
        # self.dataSet=[]
        self.item_vec = []
        self.item_mat=[]

    def loadItemsVec(self, path):
        fp = open(path, "rb")  # 读取文件内容
        content = fp.read()
        fp.close()
        rowlist = content.splitlines()  # 按行转换为一维表
        self.item_vec = [(row.split("\t")[0],row.split("\t")[1:]) for row in rowlist if row.strip()]
        for i in self.item_vec:
            self.item_mat.append(i[1])

    def user_recommend(self,user_vec):
        try:
            if sum(user_vec)!=1.0:
                print "please input validate user vector"
                return
        except:
            print "exception"
        nonzeroindex = nonzero(user_vec)[0]
        temp=[]
        re_list={}
        for j in self.item_vec:
            temp.append((j[0],[j[1][i] for i in nonzeroindex]))
        # print temp
        for i,j in enumerate(nonzeroindex):
            l=sorted(temp,key=lambda x:x[1][i],reverse=True)[:int(round(user_vec[j]*10))]
            re_list[j]=zip(*l)[0]
        return re_list

if __name__ == '__main__':
    a=RandomRecomm()
    a.loadItemsVec("/home/cdg/PycharmProjects/Test/randomrecommend/photos_vec.txt")
    b=a.item_vec
    d=[0.2,0.0,0.2,0.7]
    c=a.user_recommend(d)
    print c