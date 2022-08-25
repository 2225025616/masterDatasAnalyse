# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 21:42:59 2022

@author: Sunyali
"""

# 读取光谱仪的数据——时间、光谱信息


import os
import time

def readDatas(csvName):
    # CSV 文件
    # 拿到光谱信息
    print('csvName: ',csvName)
    specDatas = []
    with open(csvName) as f:
        if csvName.split('/')[-1].startswith('W'):
            # csvDatas =f.readlines()
            csvDatas = list(map(lambda x: x.strip().split('\n'), f.readlines()))
            # 拿到光谱数据
            specDatas = csvDatas[39:-1]
    f.close()    
    
     # 处理光谱数据，各放到一个数组中
    peakData = []
    wlData = []
    
    print('spec info *********')
    for wl in specDatas:
        wlData.append(eval(wl[0].split(',')[0]))
        peakData.append(eval(wl[0].split(',')[1]))
    f_time = os.path.getmtime(csvName)
    fTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(f_time))
    return wlData, peakData, fTime
    




# 测试
# dt = readDatas('../../DataSource/RFBG-PolyimideSMF28E/20220730/regenerationOSA-T/W2234.CSV')
# print(dt)