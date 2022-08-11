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
from repeatReadFiles import repeatFiles
from readRByOSA import readRDatas
from readTByOSA import readTDatas
from findNotch import findNotch
from findThresh import findThresh
from readTxtofModem import readText
from readTxtofTemp import readTempToCav


def transTDatas(dirName):
    # 循环读csv文件
    csvTFiles = repeatFiles(dirName, 'CSV')
    # 循环读DT8文件
    dt8TFiles = repeatFiles(dirName, 'DT8')
    
    dataT = pd.DataFrame(columns=('ctwl/nm','transmissionDepth/dB', 'r/%', 'n_ac','n_dc'))
    # 建立临时数组变量
    ctwlData = []
    peakData = []
    rData = []
    n_ac_Data = []
    # n_dc_Data = []
    # 对透射文件遍历，拟合得到中心波长、透射深度、反射率、NAC、NDC
    for i,file in enumerate(csvTFiles):
        # print(file)
        data = readTDatas(dt8TFiles[i], csvTFiles[i])
        data = findNotch(data)
        # print('ttttttTTTTTTTTTTTTTTT')
        # print(data)
        ctwlData.append(data[0])
        peakData.append(data[1])
        rData.append(data[2])
        n_ac_Data.append(data[3])
        
    dataT['ctwl/nm'] = ctwlData
    dataT['transmissionDepth/dB'] = peakData
    dataT['r/%'] = rData
    dataT['n_ac'] = n_ac_Data
    return dataT


def transRDatas(dirName):
    # 循环读csv文件
    csvRFiles = repeatFiles(dirName, 'CSV')
    # 循环读DT8文件
    dt8RFiles = repeatFiles(dirName, 'DT8')
    
    dataR = pd.DataFrame(columns=('ctwl/nm','peak/dB')) 
    # 建立临时数组变量
    ctwlData = []
    peakData = []
    # 对反射文件遍历，拿到中心波长和峰值
    for i,file in enumerate(csvRFiles):
        data = list(readRDatas(dt8RFiles[i], csvRFiles[i]))
        # print(data)
        # ctwlData.append(data[2])
        # peakData.append(abs(data[3]))
        
        data = findThresh(data)
        ctwlData.append(data[0])
        peakData.append(abs(data[1]))
        break
        
    dataR['ctwl/nm'] = ctwlData
    dataR['peak/dB'] = peakData
    # print(datasR)
    return dataR


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


def transTempTime(txtFile, tstFile):
    data = readTempToCav(txtFile, tstFile)
    datas = pd.DataFrame(columns=('time','temperature'))
    datas['time'] = data[0]
    datas['temperature/℃'] = data[1]
    return datas
