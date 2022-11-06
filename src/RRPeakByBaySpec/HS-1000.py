from readR import readRInfo
from pickTime import pickTime

import pandas as pd
import time
import numpy as np










# 读取反射文件，集合反射数据
rDatas = readRInfo('../../DataSource/H-S-1000/regeneration/HS-R')
dt = pd.DataFrame(columns=['time', 'H1060WL', 'H1060Peak_Power', 'SMF28EWL', 'SMF28EPeak_Power'])
dt['time'] = rDatas[0]
dt['H1060WL'] = rDatas[1]
dt['H1060Peak_Power'] = rDatas[2]
dt['SMF28EWL'] = rDatas[3]
dt['SMF28EPeak_Power'] = rDatas[4]
dt.to_csv('../../resultDatas/20220905-HS-r11h/rfbgR.csv')
# 温度与时间一一对应
# def readTempTime(txtFile, startTime):
#     timeDatas = []
#     # 读取温度数据
#     with open(txtFile) as f:
#         tempDatas = [data.strip('\n') for data in f.readlines()][1:]
#     f.close()
#     # print(tempDatas[0])
#     tempDatas = [eval(i) for i in tempDatas]
#
#     # time.strptime 转为时间格式
#     # time.mktime  转为时间戳格式
#     # time.strftime 转为时间
#     start = time.mktime(time.strptime(startTime, "%Y/%m/%d %H:%M:%S"))
#     # start = endTime -len(tempDatas) +41
#     # print(startTime)
#     # 从开始，加上最开始的时间戳；再转为时间格式
#     for i in np.arange(0, len(tempDatas)):
#         timeDatas.append(str(time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(float(i) + start))))
#
#     return timeDatas, tempDatas
#
# ttD = readTempTime('../../DataSource/H-S-1000/regeneration/temperature.txt', '2022/9/5 21:59:37')
# td = pd.DataFrame(columns=['time', 'temperature'])
# td['time'] = ttD[0]
# td['temperature'] = ttD[1]
# td.to_csv('../../resultDatas/20220905-HS-r11h/rfbgTempTime.csv')

# 热电偶温度时间 与 再生过程的数据时间 对应
# dt=pickTime("../../resultDatas/20220829-850-re11h-SMF28E/regenerationTR.csv", "../../resultDatas/20220829-850-re11h-SMF28E/RFBGTemp.csv")
# dt.to_csv("../../resultDatas/20220905-HS-r11h/rfbgTime-TR.csv")