# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 15:46:30 2022

@author: Administrator
"""

# 读取解调仪存的数据文件
# 第一列为时间，第二列为中心波长
# 实验过程只有一个通道，只有一列中心波长
# 得到时间、中心波长


import pandas as pd
def readCtwl(TXTFile):
    dt = pd.read_csv(TXTFile, sep='|', header=None)
    # print('txtfile name: ')
    # print(dt.columns.size)
    data = dt[0]
    # print(data[0])
    # data = [d.split('|')[0] for d in fDatas]
    # timeData = list(datetime.strptime(d[0:19].replace(',', ' '), '%Y-%m-%d %H:%M:%S') for d in data)
    timeData = [d.strip('\t').split('\t')[0].replace(',', ' ').replace('-', '/') for d in data]
    # timeData = [d[0]+' '+d[1] for d in dd]
    wlData =  [eval(d.strip('\t').split('\t')[1]) for d in data]
    # print(timeData[0])
    # print(wlData[0])
    return timeData, wlData

#  测试
# data = readCtwl("../../DataSource/H1060/1000-7mm-down_600/tempCheck/ctwlDatas.txt")
# print(data[0])
# print(data[1])
