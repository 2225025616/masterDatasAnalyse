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
from collections import Counter


# 读光谱文件，提取出中心波长、透射深度、反射峰值
def readSpec(rFile,tFile,originalSpec):
    # 读取光谱数据
    with open(originalSpec) as f:
        df = f.readlines()[39:]
    f.close()
    print(df)
    originalY = [Decimal(i.strip('\n').split(',')[1]) for i in df]

    timeDatas=[]
    ctwlDatas=[]
    tDepthDatas = []
    peakDatas=[]
    # 读反射文件
    rDatas = pd.read_csv(rFile, header=None)
    print('*******RRRRRRRRRRRRRRRRRRRR***')
    for i in rDatas.index:
        line = rDatas.iloc[i][0].strip('\n').split('\t')
        time = line[0]+' '+line[1]
        ctwl=line[2]
        timeDatas.append(time)
        ctwlDatas.append(ctwl)
        y = list(line[4:])
        # print('y: ',len(y))
        # 光栅反射光谱-光源反射光谱
        y = [eval(i) for i in y]
        # 得到反射峰值
        peak = Decimal(max(y))
        peakDatas.append(peak)
    # ****************反射数据读取结束******************************

    # 读取透射文件
    TDatas = pd.read_csv(tFile, header=None)
    reflection = []
    # print(len(fDatas))
    print('TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT')
    print('originalY: ', len(originalY))
    for i in TDatas.index:
        # print(i)
        # print(tt.strip('\n').split('\t') for tt in fDatas.iloc[i])
        # print(fDatas.iloc[i])
        line = TDatas.iloc[i][0].strip('\n').split('\t')
        # print(line)
        # print('YYYYYYYYYYYYYYYYYYYYYYYY')
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
    return timeDatas, ctwlDatas, peakDatas, tDepthDatas, reflection

