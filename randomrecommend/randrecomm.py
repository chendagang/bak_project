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
#用户向量表示为：旅游，摄影，音乐，美食，运动，户外，购物，街舞，游戏，钓鱼
#user_vec=(0.7, 0.2, 0.1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
#用户对旅游的偏好度是0.7，摄影的偏好度是0.2，音乐偏好度是0.1
#每张图片可以表示为：旅游，摄影，音乐，美食，运动，户外，购物，街舞，游戏，钓鱼
#photos_vec=(0.3, 0.1, 0.5, 0.1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
#表示这张图片属于旅游的概率是0.3，摄影的概率是0.1，音乐的概率是0.5,美食的概率是0.1
#假设有10张图片
#photos_vec1=(0.3, 0.1, 0.5, 0.1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
#photos_vec2=(0.1, 0.4, 0.5, 0.1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
#photos_vec3=(0.5, 0.0, 0.1, 0.2, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
#photos_vec4=(0.2, 0.3, 0.1, 0.1, 0.3, 0.0, 0.0, 0.0, 0.0, 0.0)
#photos_vec5=(0.4, 0.2, 0.1, 0.1, 0.1, 0.0, 0.0, 0.0, 0.0, 0.0)
#photos_vec6=(0.1, 0.2, 0.2, 0.3, 0.2, 0.0, 0.0, 0.0, 0.0, 0.0)
#photos_vec7=(0.5, 0.2, 0.1, 0.1, 0.1, 0.0, 0.0, 0.0, 0.0, 0.0)
#photos_vec8=(0.2, 0.1, 0.1, 0.2, 0.4, 0.0, 0.0, 0.0, 0.0, 0.0)
#photos_vec9=(0.6, 0.0, 0.1, 0.1, 0.2, 0.0, 0.0, 0.0, 0.0, 0.0)
#photos_vec10=(0.2, 0.3, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
#由于用户对旅游的偏好度是0.7，而上述10张图片的第1纬值表示该图片属于旅游这个类别的概率，因此我们只需将上述
#图片的第一维值降序排序，再选出前7个张即可，因此，我们为该用户推荐的属于旅游的图片是7张：photos_vec9，
#photos_vec3，photos_vec7，photos_vec5，photos_vec1，photos_vec4，photos_vec8；摄影图片2张
#photos_vec2，photos_vec4；音乐类图片是1张：photos_vec1
#############################################
class RandomRecomm(object):
    def __init__(self):
        # self.dataSet=[]
        self.item_vec = []
        self.item_mat=[]

    def loadItemsVec(self):
        self.item_vec =[(1,[0.3,0.1,0.5,0.1,0.0,0.0,0.0,0.0,0.0,0.0]),
              (2,[0.1,0.4,0.5,0.1,0.0,0.0,0.0,0.0,0.0,0.0]),
              (3,[0.5,0.0,0.1,0.2,0.0,0.0,0.0,0.0,0.0,0.0]),
              (4,[0.2,0.3,0.1,0.1,0.3,0.0,0.0,0.0,0.0,0.0]),
              (5,[0.4,0.2,0.1,0.1,0.1,0.0,0.0,0.0,0.0,0.0]),
              (6,[0.1,0.2,0.2,0.3,0.2,0.0,0.0,0.0,0.0,0.0]),
              (7,[0.5,0.2,0.1,0.1,0.1,0.0,0.0,0.0,0.0,0.0]),
              (8,[0.2,0.1,0.1,0.2,0.4,0.0,0.0,0.0,0.0,0.0]),
              (9,[0.6,0.0,0.1,0.1,0.2,0.0,0.0,0.0,0.0,0.0]),
              (10,[0.2,0.3,0.5,0.0,0.0,0.0,0.0,0.0,0.0,0.0])]
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
#测试分析
if __name__ == '__main__':
    a=RandomRecomm()
    a.loadItemsVec()
    b=a.item_vec
    d=[0.2,0.6,0.2,0.0]#用户对旅游偏好度0.2,摄影0.6，音乐0.2
    c=a.user_recommend(d)
    print c#{0: (9, 3), 1: (2, 4, 10, 5, 6, 7), 2: (1, 2)}
           #对该用户推荐旅游类的图片2张：图片9和3;摄影类的6张：2,4,10,5,6,7;音乐类2张：图片1和2