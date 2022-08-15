# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 23:08:57 2022

@author: Sunyali
"""




from readTByOSA import readTDatas
import pywt
import numpy as np
import matplotlib.pyplotot as plt

def cwt(data):
    
    x=data[0]
    y=data[1]
    
    #转为ndarray格式
    x_data=np.array(x)
    y_data=np.array(y)
    
    #设置小波变换的尺度范围，选择小波基
    wavename = 'cgau8'
    
    sampling_rate = 1000
    
    t = np.linspace(-0.5, 1, len(y))
    
    totalscal = len(y)
    
    fc = pywt.central_frequency(wavename)
    
    cparam = 2 * fc * totalscal
    
    scales = cparam / np.arange(totalscal, 1, -1)
    
    [cwtcoff, frequencies] = pywt.cwt(y_data[1][1], scales, wavename)#连续小波变换的返回值是时频图和频率
    
    #去除baseline
    
    for i in range(len(y)-1):
    
        baseline=np.mean(cwtcoff[i][0:300])#这里选了-0.2到-0.5时间范围内的功率均值作为baseline
    
    for j in range(len(y)-1):
        
        cwtcoff[i][j]=cwtcoff[i][j]-baseline#在每个频率上，原始功率减去对应的baseline值


# dt = readTDatas('../../DataSource/RFBG-PolyimideSMF28E/20220730/regenerationOSA-T/W2234.CSV')
# print(dt)