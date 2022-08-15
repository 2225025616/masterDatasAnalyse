# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 15:23:01 2022

@author: Administrator
"""

# 读取光谱仪的数据
# DT8文件无效，对DT8文件的分析删除
# DT8文件中有保存的带宽、半宽高，拿到半宽高

# CSV文件中有光谱数据，拿到光谱
# 获得光谱的所有信息——波长及能量
# 波峰+、-1，得到要的波段
# 得到对应的光源光谱数据
# 找到适合高斯拟合的数据段


import os
import time
def readRDatas(csvName):
 
    # CSV 文件
    # print('csvName: ',csvName)
    specDatas = []
    with open(csvName) as f:
        if csvName.split('/')[-1].startswith('W'):
            # csvDatas =f.readlines()
            csvDatas = list(map(lambda x: x.strip().split('\n'), f.readlines()))
            # 拿到光谱数据
            l_arr = list(d[0] for d in csvDatas)
            i = l_arr.index('"[TRACE DATA]"')
            specDatas = csvDatas[i+1:-1]
          
    f.close()  
    # 处理光谱数据，各放到一个数组中
    peakData = []
    wlData = []
    
    print('spec info *********')
    # print(specDatas)
    # print(len(specDatas))
    # print(specDatas[45])
    # print(specDatas[1])
    for data in specDatas:
        wlData.append(eval(data[0].split(',')[0]))
        peakData.append(eval(data[0].split(',')[1]))
        
    f_time = os.path.getmtime(csvName)
    fTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(f_time))
    
    return wlData, peakData, fTime
    




# 测试
# data = readRDatas('../../DataSource/RFBG-PolyimideSMF28E/20220730/regenerationOSA-T/W0302.CSV')
