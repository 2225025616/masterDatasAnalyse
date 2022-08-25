# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 15:46:30 2022

@author: Administrator
"""

# 读取解调仪存的数据文件
# 第一列为时间，第二列为中心波长
# 实验过程只有一个通道，只有一列中心波长
# 得到时间、中心波长


# from datetime import datetime

def readText(TXTFile):
    fDatas = []
    if TXTFile.split('/')[-1].startswith('D'):
        with open(TXTFile) as f:
            fDatas = f.readlines()
        f.close()
        print('txtfile name: ', TXTFile)
    data = [d.split('|')[0] for d in fDatas]
    # print(data[0][0:19].replace(',', ' '))
    # print(data[0][20:])
    # timeData = list(datetime.strptime(d[0:19].replace(',', ' '), '%Y-%m-%d %H:%M:%S') for d in data)
    timeData = [d[0:19].replace(',', ' ') for d in data]
    wlData = list(eval(d[20:]) for d in data)
    return timeData, wlData

#  测试
# data = readText("..\\..\\DataSource\\RFBG-PolyimideSMF28E\\20220711\\TEMP-Check\\Data_20220716_070000.txt")
# print(data[0])
# print(data[1])
