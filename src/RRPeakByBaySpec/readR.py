#  读反射峰的两个

## 小波变换
# 找到峰值
import pandas as pd
import os
import time
import numpy as np
import pywt
from pywt import wavedec
import linecache
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

def readRInfo(RDir):
    files = os.listdir(RDir)
    timeDatas = []
    H_wlData = []
    H_peakData = []
    S_wlData = []
    S_peakData = []

    # 循环读取文件下的csv文件
    # 遍历指定目录下所有文件,显示所有文件名
    for i in range(len(files)):
        # 文件按照时间顺序命名，文件名从大到小排列
        # i = i+43571
        # print(RDir + "/" + files[i])
        # timeDatas
        f_time = os.path.getmtime(RDir + '/' + files[i])
        fTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(f_time))
        timeDatas.append(fTime)

        with open(RDir + "/" + files[i], encoding='utf-8') as f:
            # print(linecache.getline(RDir + "/" + files[i], 530).split(','))
            peaks = int(linecache.getline(RDir + "/" + files[i], 530).split(',')[-1])
            # print(peaks)

        dt = pd.read_csv(RDir + "/" +files[i], header=16, skiprows=lambda x: x > 528, dtype={'a': float})
        dt_wl = list(dt['WL'])
        dt_peak = list(dt['Power'])




        # 根据文件判断，如果文件读出有峰——根据峰的数量，找两个峰；根据阈值3500判断峰
        if peaks == 2:
            df = pd.read_csv(RDir + "/" + files[i], header=530)
            peakWl = df['Peak_WL']
            peakPower = df['Peak_Power']
            peakFwhm = df['Peak_FWHM']
            H_wlData.append(peakWl[0])
            S_wlData.append(peakWl[1])
            H_peakData.append(peakPower[0])
            S_peakData.append(peakPower[1])
        elif peaks > 2:
            # 光谱找两个大的
            df = pd.read_csv(RDir + "/" + files[i], header=530)
            peakWl = df['Peak_WL']
            peakPower = df['Peak_Power']
            peakFwhm = df['Peak_FWHM']
            # print('Peak_WL')
            # print(peakWl)
            # print(peakPower)
            wl = [peakWl[i] - peakWl[0] for i in range(len(peakWl))]
            # print(wl)

            ps = [len(str(int(peakPower[i])))-len(str(int(peakPower[0]))) for i in range(len(peakPower))]
            # print(ps)
            Hps = [i for i in ps if i==0]
            Sps = [i for i in ps if i>0]
            Hwl = wl[0:len(Hps)]
            Swl = wl[len(Hps):len(Hps)+len(Sps)]
            S_peakData.append(peakPower[Swl.index(max(Swl))])
            S_wlData.append(peakWl[Swl.index(max(Swl))])
            H_wlData.append(peakPower[Hwl.index(max(Hwl))])
            H_peakData.append(peakWl[Hwl.index(max(Hwl))+len(Sps)])
            # print('oooo')
        else:
            # 至少其中一个在擦除或再生的临界
            # 以3500为阈值
            peakData = list(dt_peak)
            # peaks, properties = find_peaks(peakData, height=3500, distance=4, prominence=1, width=5)
            indexs, properties = find_peaks(peakData, height=3175)
            # print(properties)
            # print(indexs)
            # print(len(indexs))
            peaks = properties['peak_heights']
            # print(peaks)

            for p in peaks:
                print(dt_wl[peakData.index(p)])

            plt.plot(dt_wl,peakData, 'r-')
            wl = []
            for p in peaks:
                wl.append(dt_wl[peakData.index(p)])
                plt.plot(wl, p, "x")

            plt.show()
            # 找到波峰的位置、及对应的波长
            # 只有两个峰、一个峰、无波峰的情况
            if len(indexs) == 2:
                H_peakData.append(peaks[0])
                H_wlData.append(dt_wl[peakData.index(peaks[0])])
                S_peakData.append(peaks[1])
                S_wlData.append(dt_wl[peakData.index(peaks[1])])
            elif len(indexs) == 0:
                H_peakData.append(0)
                H_wlData.append(H_wlData[i-1])
                S_peakData.append(0)
                S_wlData.append(S_wlData[i-1])
            else:
                pre_hWl = H_wlData[i-1]
                pre_sWl = S_wlData[i-1]
                wl0 = dt_wl[peakData.index(peaks[0])]
                if abs(wl0-pre_sWl)<0.5:
                    S_peakData.append(peaks[0])
                    S_wlData.append(dt_wl[peakData.index(peaks[0])])
                    H_peakData.append(0)
                    H_wlData.append(H_wlData[i - 1])
                else:
                    H_peakData.append(peaks[0])
                    H_wlData.append(dt_wl[peakData.index(peaks[0])])
                    S_peakData.append(0)
                    S_wlData.append(S_wlData[i - 1])


    return timeDatas, H_wlData, H_peakData, S_wlData, S_peakData


# 测试
readRInfo('../../DataSource/HS/H-S-850-N2/regeneration/HS-R')