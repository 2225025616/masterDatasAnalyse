# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 15:23:01 2022

@author: Administrator
"""

# 读取光谱仪的数据
# DT8文件无效，对DT8文件的分析删除
# DT8文件中有保存的带宽、半宽高，拿到半宽高

# CSV文件中有光谱数据，拿到光谱
# 获得光谱的所有信息——波长及能量
# 波峰+、-1，得到要的波段
# 得到对应的光源光谱数据
# 找到适合高斯拟合的数据段


def readRDatas(dt8Name, csvName):
 
    # CSV 文件
    # print('csvName: ',csvName)
    specDatas = []
    with open(csvName) as f:
        if csvName.split('/')[-1].startswith('W'):
            # csvDatas =f.readlines()
            csvDatas = list(map(lambda x: x.strip().split('\n'), f.readlines()))
            # 拿到光谱数据
            l_arr = list(d[0] for d in csvDatas)
            i = l_arr.index('"[TRACE DATA]"')
            specDatas = csvDatas[i+1:-1]
          
    f.close()  
    # 处理光谱数据，各放到一个数组中
    peakData = []
    wlData = []
    ctwl=0
    peak=0
    
    print('spec info *********')
    # print(specDatas)
    # print(len(specDatas))
    # print(specDatas[45])
    print(specDatas[1])
    for data in specDatas:
        wlData.append(eval(data[0].split(',')[0]))
        peakData.append(eval(data[0].split(',')[1]))
        
    print('*****')
    print(len(wlData))
    # 高斯拟合预备工作，得到某一文件的中心波长和透射深度 他们附近的数值取出来
    
    span = wlData[1]-wlData[0]
    print('span: ',span)
   
    # 找到峰值对应的波长
    ctwl = wlData[peakData.index(max(peakData))]
    peak = max(peakData)
    index = peakData.index(max(peakData))
    print(index)
    # 根据峰值索引，左右取1/0.004个点
    start = index-125 if index-125>0 else 0
    end = index+125 if index+125<len(wlData) else len(wlData)
    
    wlData = wlData[start:end+1]
    peakData = peakData[start:end+1]
 
   
    return wlData, peakData, ctwl, peak
    




# 测试
# data = readRDatas('../../DataSource/RFBG-PolyimideSMF28E/20220730/regenerationOSA-R/D0035.DT8','../../DataSource/RFBG-PolyimideSMF28E/20220730/regenerationOSA-T/W0035.CSV')
