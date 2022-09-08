# 读取光源数据-to 数组

import time
import os
import pandas as pd

def readR(RDir):
    files = os.listdir(RDir)
    wlDatas = []
    peaks = []
    times = []

    for i, path in enumerate(files):
        # 文件按照时间顺序命名，文件名从大到小排列
        if path.find('CSV') > 0:

            # 波长一一对应，找打索引，对应减去光强
            # 由此，减到了波长的光源干扰，最大-最小=透射深度
            f_time = os.path.getmtime(RDir + '/' + path)
            fTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(f_time))
            times.append(fTime)
            df = pd.read_csv(RDir + '/' + path, header=32)
            wlData = list(df.iloc(1)[0])
            peakData = list(df.iloc(1)[1])
            thresh = max(peakData)
            ctwl = wlData[peakData.index(thresh)]
            wlDatas.append(ctwl)
            peaks.append(thresh)
            # print(df.iloc(1)[1])
            # print(df.head())

    return times, wlDatas, peaks

# 测试
# data = readR('../../DataSource/RFBG-PolyimideSMF28E/20220711-850-re4.5h/regenerationOSA-R')
# print(data[0][0])