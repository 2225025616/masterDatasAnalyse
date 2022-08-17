# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 23:08:57 2022

@author: Sunyali
"""




import pywt
import numpy as np
from pywt import wavedec
import matplotlib.pyplot as plt
# import copy




def dwt(data):
    #转为ndarray格式
    x=data[0]
    y=np.array(data[1])
    peakData = data[1]
    wlData = []
    
    print(len(data[1]))
    print('min y: ', min(y))
    print('min y: ', data[1].index(min(y)))
    
    
    
    coeffs = wavedec(y, 'db4', level=5)
    # coeffs_2 = copy.deepcopy(coeffs)
    for ix,val in enumerate(coeffs):
        if ix == 0:
            coeffs[ix] = np.zeros_like(val)
    y = pywt.waverec(coeffs, wavelet='db4')
    
    # for ix_2,val_2 in enumerate(coeffs_2):
    #     if ix_2 != 0: coeffs_2[ix_2] = np.zeros_like(val_2)
    # y_2 = pywt.waverec(coeffs_2,wavelet='db4') + 25
    
    print(y)
    # 根据拟合后的数据，找到大概透射深度的位置、及对应的波长
    y = y.tolist()
    pre_i = y.index(min(y))
    pre_ctwl = x[pre_i]
    print(pre_ctwl)
    print(pre_i)
    # 在预中心波长左右各120个点的范围内，再找透射深度及中心波长
    startIndex = pre_i-120 if pre_i-120>0 else 0
    endIndex = pre_i+120 if pre_i+120<len(x) else len(x)
    
    x_new = x[startIndex:endIndex]
    y_new = peakData[startIndex:endIndex]
    # 根据波谷值
    notch =min(y_new)
    # print('notch: ',notch)
    # print('peaks len: ',len(y_new))
    # print('x len: ',len(x_new))
    index = y_new.index(notch)
    # print('index orign: ', index)
    ctwl = x_new[index]
    print('ctwl orign: ', ctwl)
    print('*****')
    
    # 根据中心波长数值截取数据段，找波谷对应的索引 附近的光谱信息
    
    startIndex = index-150 if index-150>0 else 0
    endIndex = index+150 if index+150<len(x) else len(x)
    wlData = x[startIndex:endIndex]
    peakData = peakData[startIndex:endIndex]
    return wlData, peakData
    
    
# 测试 
from readOsa import readDatas
dt = readDatas('../../DataSource/RFBG-PolyimideSMF28E/20220730/regenerationOSA-T/W2233.CSV')
dwt(dt)