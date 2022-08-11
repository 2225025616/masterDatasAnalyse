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
import math

def readTDatas(dt8Name, csvName):
    # DT8文件
    fwhm = 0
    fileData = []
    print('dt8 file name : ',  dt8Name)
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
    print('csvName: ',csvName)
    specDatas = []
    ctwl=0
    notch=0
    r=0
    n_ac=0
    n_dc=0
    with open(csvName) as f:
        if csvName.split('/')[-1].startswith('W'):
            csvDatas = list(map(lambda x: x.strip().split('\n'), f.readlines()))
            # 拿到光谱数据
            specDatas = csvDatas[39:-1]
            
         # 处理光谱数据，各放到一个数组中
        peakData = []
        wlData = []
        
        
        # print('spec info *********')
        # print(specDatas)
        for wl in specDatas:
            wlData.append(eval(wl[0].split(',')[0]))
            peakData.append(eval(wl[0].split(',')[1]))
        # print('*****')
        # print(wlData)
        # print(wlData[-1]-wlData[0])
        # print("specDatas")
        # print(len(wlData))
        # 高斯拟合预备工作，得到某一文件的中心波长和透射深度 他们附近的数值取出来
        
        ###
        # 根据1dB带宽截取数据段
        # # 根据半宽高的一半
        # span = (wlData[-1]-wlData[0])/len(wlData)
        # oneDBdic = int(fwhm//span//2)
        # # 找到波谷对应的波长
        ctwl = wlData[peakData.index(min(peakData))]
        # # 找到峰值所在的索引
        # index = peakData.index(min(peakData))
        # # 根据峰值索引，半宽高——找到适合高斯拟合的数据段
        ###
        
        
        # 根据数值截取数据段
        # 根据波谷值，找附近的光谱信息
        print(ctwl+1)
        start = ctwl-1 if ctwl-1>wlData[0] else wlData[0]
        end = ctwl+1 if ctwl+1<wlData[-1] else wlData[-1]
        # 得到附近的索引值
        startIndex = wlData.index(start)
        endIndex = wlData.index(end)
        
        # startIndex = 0 if index-oneDBdic<0 else index-oneDBdic
        # endIndex = index+oneDBdic+1 if index+oneDBdic+1<len(wlData) else len(wlData)
        
        wlData = wlData[startIndex:endIndex]
        peakData = peakData[startIndex:endIndex]
        
        print('ctwl: ',ctwl)
        # 参考值
        # print(min(peakData))
        # print(startIndex)
        # print(endIndex)
        # print(index)
        ref = sum(peakData[0:5])/5
        print(ref)
        # notch = min(peakData)-ref
        notch = min(peakData)
        # print(notch)
        print('notch : ', notch)
        # print(math.pow(10, notch/10))
        r = 1 - abs(math.pow(10, notch/10))
        overlapFactor = 0.8
        # print('r: ', r)
        # print(math.sqrt(r))
        a = math.sqrt(r) if math.sqrt(r)<0.99 else 0.99
        # print(math.atanh(a))
        # print(math.atanh(a)*ctwl)
        n_ac = math.atanh(a)*ctwl/(overlapFactor*math.pi*float(12)*10**6)
        n_dc = 1.456/(overlapFactor*ctwl)
        # print('反射率：', r)
        # print('平均折射率：',n_ac)
        # print('dc: ', n_dc)
    f.close()
    
   
    return wlData, peakData, ctwl, notch, r, n_ac, n_dc
    




# 测试
dt = readTDatas('../../DataSource/RFBG-PolyimideSMF28E/20220711/regenerationOSA-T/D0000.DT8'    ,'../../DataSource/RFBG-PolyimideSMF28E/20220711/regenerationOSA-T/W0000.CSV')
print(dt)