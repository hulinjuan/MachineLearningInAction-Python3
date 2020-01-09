# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 14:51:31 2020

@author: lindsay.hu
"""

from numpy import *
from math import *

'''k均值算法中要用到的辅助函数'''

#将文本文件导入列表，返回值是一个包含许多其他列表的列表
def loadDataSet(filename):
    dataMat = []
    fr = open(filename)
    for line in fr.readlines():
        curLine = line.strip().split('\t')
        fltLine = list(map(float,curLine))
        dataMat.append(fltLine)
    return dataMat

#计算两个向量的欧几里得距离
def distEclud(vecA,vecB):
    return sqrt(sum(power(vecA - vecB,2)))

#函数为给定数据集构建一个包含k个随机质心的集合
def randCent(dataSet,k):
    n = shape(dataSet)[1]  #数据集列数
    centroids = mat(zeros((k,n))) #质心的0矩阵
    for j in range(n):
        minJ = min(dataSet[:,j]) #第j列的最小值
        rangeJ = float(max(dataSet[:,j]) - minJ) #第j列的极差
        centroids[:,j] = minJ + rangeJ * random.rand(k,1) #随机生成min到max之间的值
    return centroids

'''k均值聚类算法'''

#kMeans()函数，数据集和簇数目是必选参数，用来计算距离和创建初始质心的函数都是可选的
#簇分配结果矩阵clusterAssment包含两列：一列记录簇索引值，第二列存储误差，
#这里的误差指当前点到簇质心的距离，后边使用该误差来评价聚类的效果


 
def kMeans(dataSet,k,distMeas=distEclud,createCent=randCent):
    m = shape(dataSet)[0]
    clusterAssment = mat(zeros((m,2)))
    centroids = createCent(dataSet,k)
    clusterChanged = True
    while clusterChanged:
        clusterChanged = False
        for i in range(m):
            minDist = inf
            minIndex = -1
            for j in range(k):
                distJI = distMeas(centroids[j,:],dataSet[i,:])
                if distJI < minDist:
                    minDist = distJI
                    minIndex=j
            if clusterAssment[i,0] != minIndex:
                clusterChanged = True
            clusterAssment[i,:] = minIndex,minDist**2
        print(centroids)
        #遍历所有的质心，并更新它们的取值
        for cent in range(k):
            ptsInClust = dataSet[nonzero(clusterAssment[:,0].A == cent)[0]]
            centroids[cent,:] = mean(ptsInClust,axis=0)
    return centroids,clusterAssment


                    