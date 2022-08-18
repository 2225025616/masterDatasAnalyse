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
    tempDatas = []
    timeDatas = []
    startTime = 0
    # 读取温度数据
    with open(txtFile) as f:
        tempDatas = [data.strip('\n') for data in f.readlines()][1:]
    f.close()
    # print(tempDatas[0])
    tempDatas = [eval(i) for i in tempDatas]
    with open(tstFile) as f:
        file = f.readlines()
        startTime = file[19].split('=')[-1][0:19]
    f.close()
     
    # time.strptime 转为时间格式
    # time.mktime  转为时间戳格式
    # time.strftime 转为时间
    startTime = time.mktime(time.strptime(startTime,"%Y/%m/%d %H:%M:%S"))
    # print(startTime)
    # 从开始，加上最开始的时间戳；再转为时间格式
    for i in np.arange(0, len(tempDatas)):
        timeDatas.append(time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(float(i)+startTime)))
        
    # print('时间戳')
    # print(timeDatas[500])
    
    return timeDatas, tempDatas
 
    
 
# 测试 
data = readTemp("../../DataSource/RFBG-PolyimideSMF28E/20220730/temperatureDatas/TEMP.txt", "../../DataSource/RFBG-PolyimideSMF28E/20220730/temperatureDatas/20220804RFBG.TST") 
print(data[0][232])