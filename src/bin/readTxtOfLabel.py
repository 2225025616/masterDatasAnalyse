# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 15:41:00 2022

@author: Sunyali
"""

# 读取label存的txt文件数据
# 时间、中心波长、带宽，光谱信息

import pandas as pd
from findThresh import findPeak, findNotch


def readSpecR(fileName):
    time = []
    ctwl = []
    specInfo = []
    # fDatas = pd.read_csv(fileName)

    with open(fileName) as f:
        fDatas = f.readlines()
    f.close()
    fDatas = [i.strip('\n').split('\t') for i in fDatas]
    print('*******RRRRRRRRRRRRRRRRRRRR***')
    time = [i[0]+' '+i[1] for i in fDatas]
    # print(time[0])
    ctwl = [i[2] for i in fDatas]
    for data in fDatas:
        dt = [eval(i) for i in data[4:]]
        specInfo.append(dt)
    # for spec in specInfos:
    #     for i in spec:
    #         i = eval(i)
    # print('peak: ', min(specInfo))
    # print('txtfile name: ', time[0])
    # print('txtfile name: ', specInfo[0])
    # print('txtfile name: ', ctwl[0])
    print('R len: ', len(time))
    peak = []
    for y in specInfo:
        peak.append(findPeak(y))
    return time, ctwl, peak


def readSpecT(fileName):
    # time = []
    specInfo = []
    # fDatas = pd.read_csv(fileName)
    with open(fileName) as f:
        fDatas = f.readlines()
    f.close()
    fDatas = [i.strip('\n').split('\t') for i in fDatas]
    print('****TTTTTTTTTTTTTTT****')
    # time = [i[0]+' '+i[1] for i in fDatas]
    # print(time[0])
    for data in fDatas:
        dt = [eval(i) for i in data[4:]]
        specInfo.append(dt)

    print('T len: ', len(specInfo))
    notchDatas = []
    r_arr = []
    for y in specInfo:
        notchDatas.append(findNotch(y)[0])
        r_arr.append(findNotch(y)[1])
    return notchDatas, r_arr


# 测试
df = pd.DataFrame(
    columns=('time', 'ctwl/nm', 'reflection/dBm', 'transmissionDepth/dB', 'reflection/%'))

data_r = readSpecR(
    "../../DataSource/RFBG-PolyimideSMF28E/20220730/overHigh/1000-r.txt")

df['time'] = data_r[0]
df['ctwl/nm'] = data_r[1]
df['reflection/dBm'] = data_r[2]

data_t = readSpecT(
    "../../DataSource/RFBG-PolyimideSMF28E/20220730/overHigh/1000-t.txt")


df['transmissionDepth/dB'] = data_t[0]
# df['reflection/%'] = data_t[1]
df.to_csv("../../resultDatas/20220728/1000dgree-TR.csv")
