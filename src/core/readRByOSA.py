# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 15:23:01 2022

@author: Administrator
"""

# 读取光谱仪的数据
# DT8文件中有保存的带宽、半宽高，拿到半宽高
# CSV文件中有光谱数据，拿到光谱
# 获得光谱的所有信息——波长及能量
# 得到对应的光源光谱数据
# 找到适合高斯拟合的数据段


def readRDatas(dt8Name, csvName):
    # DT8文件
    fwhm = 0
    fileData = []
    # print('dt8 file name : ',  dt8Name)
    with open(dt8Name) as f:
        if dt8Name.split('/')[-1].startswith('D'):
            # print('222')
            fileData = list(map(lambda x: x.strip().split('\n'), f.readlines()))
            # print('fileData: ', fileData)
            data = fileData[4]
            # print('data: ',data)
            # print(fileData[5][0].strip(' ').split(' ')[-1])
            fwhm = eval(data[0].strip(' ').split(' ')[-1][0:6])
    f.close()
   
       
    
    
    # CSV 文件
    # print('csvName: ',csvName)
    specDatas = []
    with open(csvName) as f:
        if csvName.split('/')[-1].startswith('W'):
            csvDatas = list(map(lambda x: x.strip().split('\n'), f.readlines()))
            # 拿到光谱数据
            specDatas = csvDatas[34:-1]
            
         # 处理光谱数据，各放到一个数组中
        peakData = []
        wlData = []
        ctwl=0
        peak=0
        
        print('spec info *********')
        # print(specDatas)
        for wl in specDatas:
            wlData.append(eval(wl[0].split(',')[0]))
            peakData.append(eval(wl[0].split(',')[1]))
        print('*****')
        print(wlData)
        print(wlData[-1]-wlData[0])
        print("specDatas")
        print(len(wlData))
        # 高斯拟合预备工作，得到某一文件的中心波长和透射深度 他们附近的数值取出来
        
        span = (wlData[-1]-wlData[0])/len(wlData)
        # 根据半宽高的一半
        halfDic = int(fwhm//span//2)
        # 找到峰值对应的波长
        ctwl = wlData[peakData.index(max(peakData))]
        peak = max(peakData)
        # 找到峰值所在的索引
        index = wlData.index(ctwl)
        # 根据峰值索引，半宽高——找到适合高斯拟合的数据段
        startIndex = 0 if index-halfDic<0 else index-halfDic
        endIndex = index+halfDic+1 if index+halfDic+1<len(wlData) else len(wlData)
        wlData = list(wlData)[startIndex:endIndex]
        peakData = peakData[startIndex:endIndex]
        
        # print(halfDic)
        # print(span)
        # print('ctwl: ',ctwl)
        # print('peak index: ', peakIndex)
        # print(len(wlData))
    f.close()
    
   
    return wlData, peakData, ctwl, peak
    




# 测试
readRDatas('../../DataSource/RFBG-PolyimideSMF28E/20220730/regenerationOSA-R/D0035.DT8','../../DataSource/RFBG-PolyimideSMF28E/20220730/regenerationOSA-T/W0035.CSV')