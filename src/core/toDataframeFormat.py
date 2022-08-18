# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 13:55:53 2022

@author: Sunyali
"""

# 把所有osa-透射数据读出来，保存成DataFrame格式——中心波长、峰值
# 把所有osa-反射数据读出来，保存成DataFrame格式——中心波长、投身深度、反射率、交流折射率、直流折射率
# 把解调仪一个通道的数据全部读出来，保存正Dataframe格式——时间、中心波长
# 该寻峰使用比较算法

import pandas as pd
# 循环读文件夹下的文件
from repeatReadFiles import repeatFiles
# 读取光谱仪透射、反射数据
from readOsa import readDatas
# from readTByOSA import readTDatas
# from readRByOSA import readRDatas
# 读取温度特性实验--解调仪的数据
from readTxtofModem import readText
# 读取热电偶的数据
from readTempDatas import readTemp
# 读取label存的光谱仪的数据
from readTxtOfLabel import readSpecInfo
# 读取BaseSpec存的反射光谱的数据
from readCSVByModem import readInfo

# 去基线，拿到波谷及附近的点
from delBaseline import delbaseine
# 二次拟合，拿到透射相关的数据
from calTDepth import calTInfo

# 读全过程的透射数据
def transTDatas(dirName):
    # 循环读csv文件
    csvTFiles = repeatFiles(dirName, 'CSV')
   
    tDataInfo = pd.DataFrame(columns=('time', 'ctwl/nm','transmissionDepth/dB','reflection/%','n_ac','n_dc'))
    # 建立临时数组变量
    ctwlDatas = []
    peakDatas = []
    timeData = []
    n_ac_Data = []
    r_Data = []
    # 对透射文件遍历，拟合得到中心波长、透射深度、反射率、NAC、NDC
    for i,file in enumerate(csvTFiles):
        # print(file)
        # 拿到光谱信息
        spec_info = readDatas(csvTFiles[i])
        notch_datas = delbaseine(spec_info)
        data = calTInfo(notch_datas)
        # return ctwl,t_depth,r,n_ac
        # print('ttttttTTTTTTTTTTTTTTT')
        # print(data)
        timeData.append(spec_info[2])
        ctwlDatas.append(data[0])
        peakDatas.append(data[1])
        r_Data.append(data[2])
        n_ac_Data.append(data[3])
        # 'reflection/%','n_ac'
        
    tDataInfo['ctwl/nm'] = ctwlDatas
    tDataInfo['transmissionDepth/dB'] = peakDatas
    tDataInfo['time'] = timeData
    tDataInfo['reflection/%'] = r_Data
    tDataInfo['n_ac'] = n_ac_Data
    
    return tDataInfo


# 读取全过程的反射数据
def transRDatas(dirName):
    # 循环读csv文件
    csvRFiles = repeatFiles(dirName, 'CSV')
    
    dataR = pd.DataFrame(columns=('time', 'ctwl/nm')) 
    # 建立临时数组变量
    ctwlDatas = []
    timeData = []
    # 对反射文件遍历，拿到中心波长和峰值
    for i,file in enumerate(csvRFiles):
        data = list(readDatas(csvRFiles[i]))
        # print(data)
        #  wlData, peakData, fTime
        ctwlDatas.append(data[0][data[1].index(max(data[1]))])
        timeData.append(data[2])
         
        
    dataR['ctwl/nm'] = ctwlDatas
    dataR['time'] = timeData
    return dataR


# 读取label存的光谱仪OSA数据
def transRegenerateDatas(dirName):
    # 循环读txt文件
    csvRFiles = repeatFiles(dirName, 'txt')
    
    datas = pd.DataFrame(columns=('time', 'ctwl/nm','peak/dBm')) 
    # 建立临时数组变量
    ctwlDatas = []
    specInfo = []
    timeData = []
    # 对反射文件遍历，拿到中心波长和峰值
    for i,file in enumerate(csvRFiles):
        data = list(readSpecInfo(csvRFiles[i]))
        # print(data)
        ctwlDatas.extend(data[1])
        specInfo.extend(data[2])
        timeData.extend(data[0])
         
        
    datas['ctwl/nm'] = ctwlDatas
    datas['transmissionDepth/dBm'] = specInfo
    datas['time'] = timeData
    return datas

# 读取温度特性实验过程的数据
def transTempDatas(dirName):
    # 循环读txt文件
    txtFiles = repeatFiles(dirName, 'txt')
    
    dataTemp = pd.DataFrame(columns=('time','ctwl/nm'))
    # 建立临时数组变量
    ctwlData = []
    timeData = []
    # 对解调仪读的温度特性文件遍历，拿到时间和中心波长
    for file in txtFiles:
        txt_data = readText(file)
        print(txt_data)
        ctwlData.extend(txt_data[1])
        timeData.extend(txt_data[0])
        
    dataTemp['time'] = timeData
    dataTemp['ctwl/nm'] = ctwlData
    return dataTemp


# 读取热电偶数据——温度时间
def transTempTime(txtFile, tstFile):
    data = readTemp(txtFile, tstFile)
    datas = pd.DataFrame(columns=('time','temperature'))
    datas['time'] = data[0]
    datas['temperature/℃'] = data[1]
    return datas

# 读取BaseSpec解调仪保存的csv数据
def transRInfo(dirName):
    # 循环读csv文件
    csvTFiles = repeatFiles(dirName, 'CSV')
   
    rDataInfo = pd.DataFrame(columns=('time', 'ctwl/nm','reflection/mv'))
    # 建立临时数组变量
    ctwlDatas = []
    peakDatas = []
    timeData = []
    # 对csv文件遍历，拟合得到中心波长、反射光谱
    for i,file in enumerate(csvTFiles):
        # print(file)
        # 拿到光谱信息
        data = readInfo(csvTFiles[i])
        # return ctwl, peak, fTime
        timeData.append(data[2])
        ctwlDatas.append(data[0])
        peakDatas.append(data[1])
       
        
    rDataInfo['ctwl/nm'] = ctwlDatas
    rDataInfo['time'] = timeData
    rDataInfo['reflection/mv'] = peakDatas
    
    return rDataInfo
