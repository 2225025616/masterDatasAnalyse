# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 15:23:01 2022

@author: Administrator
"""

# 读取光谱仪的数据

# DT8文件分析无效， 删除对DT8文件的分析和数据处理
# DT8文件中有保存的带宽、半宽高，拿到半宽高

# CSV文件中有光谱数据，拿到光谱
# 获得光谱的所有信息——波长及能量

# 个别光谱透射深度并不是最小的值
    
    # 利用透射光谱的光强信息dbm的绝对值，找到波峰——即实际光谱的波谷
    # 利用波谷的索引——左右各找125个点

# 得到对应的光源光谱数据___——————拿到所有的光谱信息，根据温度判断大概范围在选取数据段
    # 找到适合高斯拟合的数据段
# import math
# from scipy.signal import find_peaks


# 去基线
# 小波变换
# 原曲线—去基线后的曲线=新曲线
# 在新曲线找极值点，找范围
# 再根据极值点找索引，找需要的范围

import os
import time

def readTDatas(csvName):
    
    # CSV 文件
    # 拿到光谱信息
    # print('csvName: ',csvName)
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
    # ctwl=0
    # notch=0
    
    
    print('spec info *********')
    # print(specDatas)
    for wl in specDatas:
        wlData.append(eval(wl[0].split(',')[0]))
        peakData.append(eval(wl[0].split(',')[1]))
    
    
    # 高斯拟合预备工作，得到某一文件的中心波长和透射深度 他们附近的数值取出来
   
    # 根据中心波长数值截取数据段
    # 根据波谷值，找附近的光谱信息
    
    
    notch =min(peakData)
    # print(peaks)
    # print('notch: ',notch)
    # print('peaks len: ',len(peaks))
    # print('*****')
    index = peakData.index(notch)
    ctwl = wlData[peakData.index(notch)]
    
    startIndex = index-125 if index-125>0 else 0
    endIndex = index+125 if index+125<len(wlData) else len(wlData)
    wlData = wlData[startIndex:endIndex]
    peakData = peakData[startIndex:endIndex]
    
    # print('ctwl: ',ctwl)
    # print('notch : ', notch)
    
    f_time = os.path.getmtime(csvName)
    fTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(f_time))
    return wlData, peakData, fTime
    




# 测试
# dt = readTDatas('../../DataSource/RFBG-PolyimideSMF28E/20220730/regenerationOSA-T/W2234.CSV')
# print(dt)