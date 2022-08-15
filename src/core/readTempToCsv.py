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
import numpy as np

def readTempToCav(txtFile, tstFile):
    tempDatas = []
    timeDatas = []
    wlDatas = []
    startTime = 0
    
    # 读取温度数据
    with open(txtFile) as f:
        tempDatas = [ data.strip('\n') for data in f.readlines()][1:]
    f.close()
    # print(tempDatas[0])
    tempDatas = [eval(i) for i in tempDatas]
    wlDatasMin = []
    wlDatasMax = []
    for i,temp in enumerate(tempDatas):
        wlDatasMin.append(0.0013*(temp-tempDatas[0])+1535)
        wlDatasMax.append(0.00155*(temp-tempDatas[0])+1535)
        
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
    
    return timeDatas, tempDatas, wlDatasMin, wlDatasMax
    

# 测试
# datas = readTempToCav("../../DataSource/RFBG-PolyimideSMF28E/20220730/temperatureDatas/TEMP.txt", "../../DataSource/RFBG-PolyimideSMF28E/20220730/temperatureDatas/20220804RFBG.TST")
# temp_time_datas = pd.DataFrame(columns=('time','temperature', 'min-wl', 'max-wl'))
# temp_time_datas['time'] = datas[0]
# temp_time_datas['temperature'] = datas[1]
# temp_time_datas['min-wl'] = datas[2]
# temp_time_datas['max-wl'] = datas[3]
# temp_time_datas.to_csv("temp_time.csv")