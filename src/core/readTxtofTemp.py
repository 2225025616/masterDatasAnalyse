# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 15:41:17 2022

@author: Administrator
"""

# 读取热电偶温度数据
# 手动写入开始时间
# 间隔1s
# 把txt中的温度数据放到csv文件中


import time
import pandas as pd

def readTempToCav(txtFile, tstFile):
    tempDatas = []
    timeDatas = []
    startTime = 0
    
    # 读取温度数据
    with open(txtFile) as f:
        tempDatas = [ data.strip('\n') for data in f.readlines()][1:]
    f.close()
    # print(tempDatas[0])
    
    with open(tstFile) as f:
        file = f.readlines()
        startTime = file[19].split('=')[-1][0:19]
    f.close()
    
    print('**************************')
    
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
    


# readTempToCav("../../DataSource/RFBG-PolyimideSMF28E/20220730/temperatureDatas/TEMP.txt", "../../DataSource/RFBG-PolyimideSMF28E/20220730/temperatureDatas/20220804RFBG.TST")