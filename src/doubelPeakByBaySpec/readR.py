
import pandas as pd
import os
import time

def readRInfo(RDir):
    files = os.listdir(RDir)
    timeDatas = []
    H_wlData = []
    H_peakData = []
    S_wlData = []
    S_peakData = []
    for i in range(len(files)):
        # 文件按照时间顺序命名，文件名从大到小排列
        print(RDir + "/" + files[i])
        dt = pd.read_csv(RDir + "/" +files[i], header=16, skiprows=lambda x: x > 528, dtype={'a': float})
        dt_wl = list(dt['WL'])
        dt_peak = list(dt['Power'])
        print(len(dt_wl))
        print(dt.values[-1])

        SPeak = max(dt_peak)
        SWL = dt_wl[dt_peak.index(max(dt_peak))]
        dt_peak.remove(SPeak)
        dt_wl.remove(SWL)
        HPeak = max(dt_peak)
        HWL = dt_wl[dt_peak.index(max(dt_peak))]
        S_peakData.append(SPeak)
        S_wlData.append(SWL)
        H_wlData.append(HWL)
        H_peakData.append(HPeak)
        # peaks, pro = find_peaks(peakDatas,height=normalH)
        print('SMF28E: ', SWL, 'peak: ', SPeak)
        print('H1060: ', HWL, 'peak: ', HPeak)
        f_time = os.path.getmtime(RDir + '/' + files[i])
        fTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(f_time))
        print(fTime)
        timeDatas.append(fTime)
    return timeDatas, H_wlData, H_peakData, S_wlData, S_peakData


# 测试
# readRInfo('../../DataSource/H-S-1000/regeneration/HS-R/1000-HS_0002.csv')
# readRInfo('../../DataSource/H-S-1000/regeneration/HS-R')