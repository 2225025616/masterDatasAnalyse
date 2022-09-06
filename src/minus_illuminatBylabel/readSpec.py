# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 15:41:00 2022

@author: Sunyali
"""

# 读取label存的txt文件数据
# 时间、中心波长、带宽，光谱信息

import pandas as pd
from decimal import Decimal
import math
import time
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
        line = TDatas.iloc[i][0].strip('\n').split('\t')
        # time.strptime 转为时间格式
        t = line[0] + ' ' + line[1]
        # t = time.strptime(t, "%Y/%m/%d %H:%M:%S")
        if t in timeDatas:
            y = list(line[4:])
            # print('y: ',len(y))
            y=[eval(i) for i in y]
            # 光栅透射光谱-光源透射光谱
            # print(y[0])
            fbgY = [Decimal(y[i]) - Decimal(originalY[i]) for i, d in enumerate(y)]
            # print(fbgY[0])
            # 得到透射深度
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

