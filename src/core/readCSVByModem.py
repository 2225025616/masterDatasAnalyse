# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 15:46:51 2022

@author: Administrator
"""

# 读取BaySpec的数据
# 所有的csv数据——中心波长、光强、FWHM、文件创立时间

import os
import time

def readInfo(fileName):
    ctwl = 0
    peak = 0
    with open(fileName) as f:
        # csvDatas =f.readlines()
        csvDatas = list(map(lambda x: x.strip().split('\n'), f.readlines()))
        # 拿到中心波长数据
        lastLine = csvDatas[-1][0]
        # print(lastLine)
        # print(len(lastLine))
        # print(lastLine.split(','))
    f.close()  
    if len(lastLine) != 0 and lastLine.find('Peak_Power')<0:
        ctwl = eval(lastLine.split(',')[0])
        peak = eval(lastLine.split(',')[1])
        
    f_time = os.path.getmtime(fileName)
    fTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(f_time))
    
    return ctwl, peak, fTime
    
    
# 测试
# data = readInfo('../../DataSource/RFBG-PolyimideSMF28E/20220730/regenerationMI-R/900_1s_0023.csv')
# print(data)
