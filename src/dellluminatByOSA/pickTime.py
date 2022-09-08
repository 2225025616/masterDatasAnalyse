# -*- coding: utf-8 -*-
# 再生过程中间隔两秒保存数据
# 再生过程中的时间和温度数据的时间对应，挑选对应温度
# 把相同时间对应的温度保存成数组，插入到元数据中，紧跟时间之后

# file1为要插入温度的文件
# file2为温度数据文件
import time
import pandas as pd

def pickTime(file1, file2):
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)
    rfbgTime = list(df1['time'])
    time1 = [time.mktime(time.strptime(i,"%Y/%m/%d %H:%M:%S")) for i in rfbgTime]
    tempTime = list(df2['time'])
    time2 = [time.mktime(time.strptime(i,"%Y/%m/%d %H:%M:%S")) for i in tempTime]
    temperatureDatas = list(df2['temperature'])
    ctwlDatas = list(df1['ctwl'])
    # print('time1: ', time1[0])
    # print(time2[627])
    # print(time2[628])
    # print(time1[0], '/t', tempTime[1])
    tempDatas = []
    wavelengths = []
    timeDatas = []
    for i, t in enumerate(time1):
        # print(time2[i])
        # print(time2[628] == t)
        if t in time2:
            j = time2.index(t)
            temp = temperatureDatas[j]
            # print('index:{}, temp:{}'.format(j, temp))
            tempDatas.append(temp)
            wavelengths.append(ctwlDatas[i])
            timeDatas.append(rfbgTime[i])

    df = pd.DataFrame(columns=['time', 'temperature', 'ctwl'])
    df["time"] = timeDatas
    df["temperature"] = tempDatas
    df["ctwl"] = wavelengths

    return df






# pickTime("../../resultDatas/20220823-1000-H1060-7mm-49DB/regenerationTR.csv", "../../resultDatas/20220823-1000-H1060-7mm-49DB/RFBGTemp.csv")