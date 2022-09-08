# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 22:21:01 2022

@author: Sunyali
"""

# 读取热电偶程序保存的数据
# 读出来开始时间、温度
# 温度是1s记录1次，根据开始时间记录时间



import time
import numpy as np

def readTemp(txtFile, tstFile):
    tempStamp = []
    timeDatas = []
    # 读取温度数据
    with open(txtFile) as f:
        tempDatas = [data.strip('\n') for data in f.readlines()][1:]
    f.close()
    # print(tempDatas[0])
    tempDatas = [eval(i) for i in tempDatas]
    with open(tstFile) as f:
        file = f.readlines()
        startTime = file[19].split('=')[-1][0:19]
        endTime = file[21].split('=')[-1][0:19]
    f.close()
     
    # time.strptime 转为时间格式
    # time.mktime  转为时间戳格式
    # time.strftime 转为时间
    startTime = time.mktime(time.strptime(startTime, "%Y/%m/%d %H:%M:%S"))
    endTime = time.mktime(time.strptime(endTime, "%Y/%m/%d %H:%M:%S"))
    start = startTime+41 if endTime-len(tempDatas)==startTime else endTime -len(tempDatas) +41
    # start = endTime -len(tempDatas) +41
    # print(startTime)
    # 从开始，加上最开始的时间戳；再转为时间格式
    for i in np.arange(0, len(tempDatas)):
        timeDatas.append(str(time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(float(i)+start))))
        # tempStamp.append(time.mktime(time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(float(i)+start))))
        
    # print('时间戳')
    # print(type(timeDatas[500]))
    
    return timeDatas, tempStamp, tempDatas
 
    
 
# 测试 
# data = readTemp("../../DataSource/RFBG-PolyimideSMF28E/20220730-900/temperatureDatas/TEMP.txt", "../../DataSource/RFBG-PolyimideSMF28E/20220730-900/temperatureDatas/20220804RFBG.TST")
# print(data[0][232])