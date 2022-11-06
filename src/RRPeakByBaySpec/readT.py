# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 15:41:00 2022

@author: Sunyali
"""
import numpy as np
# 读取label存的txt文件数据
# 时间、中心波长、带宽，光谱信息

import pandas as pd
from decimal import Decimal
import math
import time
import matplotlib.pyplot as plt
# from collections import Counter

# 反射时间和透射时间对应
# 修正——两台光谱仪卡顿，时间不一致，调整时间对应，波长对应

# 读光谱文件，提取出中心波长、透射深度、反射峰值
def readSpec(rFile,tFile,originalSpec):
    # 读取光谱数据
    with open(originalSpec) as f:
        df = f.readlines()[39:]
    f.close()
    # print(df)
    originalY = [Decimal(i.strip('\n').split(',')[1]) for i in df]

    timeR=[]
    timeT=[]
    ctwlDatas=[]
    tDepthDatas = []
    peakDatas=[]
    reflection = []
    # 读反射文件
    rDatas = pd.read_csv(rFile, header=None)
    # print('*******RRRRRRRRRRRRRRRRRRRR***')
    for i in rDatas.index:
        line = rDatas.iloc[i][0].strip('\n').split('\t')

        # time.strptime 转为时间格式
        t = line[0]+' '+line[1]
        # t = time.strptime(t, "%Y/%m/%d %H:%M:%S")
        timeR.append(t)

    # ****************反射数据读取时间结束******************************
    # 读取透射文件
    TDatas = pd.read_csv(tFile, header=None)
    # print(len(fDatas))
    # print('TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT')
    # print('originalY: ', len(originalY))
    for i in TDatas.index:
        # print(i)
        # print(tt.strip('\n').split('\t') for tt in fDatas.iloc[i])
        # print(fDatas.iloc[i])
        line = TDatas.iloc[i][0].strip('\n').split('\t')
        # print(line)
        # print('YYYYYYYYYYYYYYYYYYYYYYYY')
        # time.strptime 转为时间格式
        t = line[0] + ' ' + line[1]
        timeT.append(t)

    # *************************读取透射数据时间结束******************************

    # 清洗数据
    # 透射时间、反射时间 对比，挑选R、透射深度数据
    timeDatas = timeR if len(timeR)<len(timeT) else timeT
    # 根据时间，挑选R文件中的波长、光谱【得到峰值】
    for i in rDatas.index:
        line = rDatas.iloc[i][0].strip('\n').split('\t')

        # time.strptime 转为时间格式
        t = line[0] + ' ' + line[1]
        if t in timeDatas:
            ctwl = line[2]
            ctwlDatas.append(ctwl)
            y = list(line[4:])
            # print('y: ',len(y))
            # 光栅反射光谱-光源反射光谱
            y = [eval(i) for i in y]
            # 得到反射峰值
            peak = Decimal(max(y))
            peakDatas.append(peak)

    # 根据时间，挑选T文件中的光谱，算出透射深度、R
    for i in TDatas.index:
        i = i+117
        line = TDatas.iloc[i][0].strip('\n').split('\t')
        # time.strptime 转为时间格式
        t = line[0] + ' ' + line[1]
        t = time.strptime(t, "%Y/%m/%d %H:%M:%S")
        # 还有不进if的？
        if t in timeDatas:
            # y = list(line[4:])
            # print('y: ',len(y))
            y=[eval(i) for i in y]
            # 光栅透射光谱-光源透射光谱
            # print(y[0])
            fbgY = [Decimal(y[i]) - Decimal(originalY[i]) for i, d in enumerate(y)]
            print(fbgY[0])
            # 得到透射深度
            #
            #作图
            plt.figure(figsize=(18,12))
            # 上包络
            # plt.plot(x,y_max,'r-',label='max')
            # # 下包络
            # plt.plot(x,y_min,'g-',label='min')
            # 去基线
            plt.plot(np.arange(len(fbgY)),fbgY,'r+',label='interp1')
            plt.plot(np.arange(len(fbgY)),y,'b-',label='original')
            plt.show()
            notch = Decimal(max(fbgY)) - Decimal(min(fbgY))
            r = Decimal((1 - Decimal(math.pow(10, -notch/10))))*100
            # print(notch)
            tDepthDatas.append(notch)
            reflection.append(r)
            # print(r)
            # break
    # stamp = time.mktime(time.strptime(t, "%Y/%m/%d %H:%M:%S"))
    timeStamp = [time.mktime(time.strptime(t, "%Y/%m/%d %H:%M:%S")) for t in timeDatas]

    return timeDatas, timeStamp, ctwlDatas, peakDatas, tDepthDatas, reflection


import pywt
from pywt import wavedec
# 读光谱文件，提取出中心波长、透射深度
def readT(tFile,originalSpec):
    # 读取光谱数据
    with open(originalSpec) as f:
        df = f.readlines()[39:]
    f.close()
    # print(df)
    originalY = [Decimal(i.strip('\n').split(',')[1]) for i in df]

    timeDatas=[]
    ctwlDatas=[]
    tDepthDatas = []
    reflection = []

    # 读取透射文件
    TDatas = pd.read_csv(tFile, header=None)
    # print(len(fDatas))
    # print('TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT')
    # print('originalY: ', len(originalY))
    for i in TDatas.index:
        # print(i)
        # print(tt.strip('\n').split('\t') for tt in fDatas.iloc[i])
        # print(fDatas.iloc[i])
        line = TDatas.iloc[i][0].strip('\n').split('\t')
        # print(line)
        # print('YYYYYYYYYYYYYYYYYYYYYYYY')
        # time.strptime 转为时间格式
        t = line[0] + ' ' + line[1]
        timeDatas.append(t)

    # *************************读取透射数据时间结束******************************


    # 根据时间，挑选T文件中的光谱，算出透射深度、R
    for i in TDatas.index:
        i = i+169
        line = TDatas.iloc[i][0].strip('\n').split('\t')
        # time.strptime 转为时间格式
        t = line[0] + ' ' + line[1]
        t = time.strptime(t, "%Y/%m/%d %H:%M:%S")
        print(t)
        y = list(line[4:])
        # print('y: ',len(y))
        yT=[eval(i) for i in y]
        # 光栅透射光谱-光源透射光谱
        # print(y[0])
        fbgY = [Decimal(yT[i]) - Decimal(originalY[i]) for i, d in enumerate(y)]
        print(fbgY[0])
        # 得到透射深度
        #
        #作图
        plt.figure(figsize=(18,12))
        # 上包络
        # plt.plot(x,y_max,'r-',label='max')
        # # 下包络
        # plt.plot(x,y_min,'g-',label='min')

        # 小波变换找到波谷
        # 转为ndarray格式
        peakData = list(yT)

        print('min y: ', min(yT))
        # print('index y: ', peakData.index(min(y)))

        coeffs = wavedec(yT, 'db4', level=5)
        # coeffs_2 = copy.deepcopy(coeffs)
        for ix, val in enumerate(coeffs):
            if ix == 0:
                coeffs[ix] = np.zeros_like(val)
        y = list(pywt.waverec(coeffs, wavelet='db4'))
        print(np.array(y)-7.6)
        plt.plot(np.arange(len(fbgY)),fbgY,'r-',label='T-original')
        # plt.plot(np.arange(len(fbgY)),yT,'b-',label='original')
        plt.plot(np.arange(len(fbgY)),np.array(y)-7.2,'g-',label='db4')
        plt.legend(loc='upper left')
        plt.show()
        # 去基线
        notch = Decimal(max(fbgY)) - Decimal(min(fbgY))
        r = Decimal((1 - Decimal(math.pow(10, -notch/10))))*100
        # print(notch)
        tDepthDatas.append(notch)
        reflection.append(r)
        # print(r)
        # break
    # stamp = time.mktime(time.strptime(t, "%Y/%m/%d %H:%M:%S"))
    timeStamp = [time.mktime(time.strptime(t, "%Y/%m/%d %H:%M:%S")) for t in timeDatas]

    return timeStamp, ctwlDatas, tDepthDatas, reflection


# 测试
data = readT(
    "../../DataSource/RFBG-PolyimideSMF28E/20220829-850-re11h/regeneration/850_T.txt",
    '../../DataSource/RFBG-PolyimideSMF28E/20220829-850-re11h/originalT.CSV'
)
print(data)
