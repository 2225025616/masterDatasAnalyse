# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 15:57:55 2022

@author: Administrator
"""

# 测试重复读取文件，获得数据

from repeatReadFiles import repeatFiles
from readRByOSA import readRDatas
from readTByOSA import readTDatas
from findNotch import findNotch
from findThresh import findThresh
from readTxtofModem import readText

# 循环读csv文件
csvRFiles = repeatFiles('../../DataSource/RFBG-PolyimideSMF28E/20220728/regenerationOSA-R', 'CSV')
csvTFiles = repeatFiles('../../DataSource/RFBG-PolyimideSMF28E/20220728/regenerationOSA-T', 'CSV')
# 循环读DT8文件
dt8RFiles = repeatFiles('../../DataSource/RFBG-PolyimideSMF28E/20220728/regenerationOSA-R', 'DT8')
dt8TFiles = repeatFiles('../../DataSource/RFBG-PolyimideSMF28E/20220728/regenerationOSA-T', 'DT8')
# 循环读txt文件
txtFiles = repeatFiles('../../DataSource/RFBG-PolyimideSMF28E/20220728/TEMP-Check', 'txt')

# print(len(csvRFiles))
# print(len(dt8RFiles))
# print(txtFiles)


import pandas as pd
# 建立dataframe数据类型，方便写入到csv文件中
datasR = pd.DataFrame(columns=('ctwl/nm','peak/dB')) 
datasT = pd.DataFrame(columns=('ctwl/nm','transmissionDepth/dB', 'r/%', 'n_ac','n_dc'))
datasTemp = pd.DataFrame(columns=('time','ctwl/nm'))


# 建立临时数组变量
ctwlData = []
peakData = []
rData = []
n_ac_Data = []
n_dc_Data = []

# 对反射文件遍历，拿到中心波长和峰值
# for i,file in enumerate(csvRFiles):
#     data = list(readRDatas(dt8RFiles[i], csvRFiles[i]))
#     data = list(findThresh(data))
#     # print(data)
#     ctwlData.append(data[2])
#     peakData.append(abs(data[3]))
#     # break
    
# datasR['ctwl/nm'] = ctwlData
# datasR['peak/dB'] = peakData
# print(datasR)

# 对透射文件遍历，拟合得到中心波长、透射深度、反射率、NAC、NDC
for i,file in enumerate(csvTFiles):
    print(file)
    osa_data = readTDatas(dt8TFiles[i], csvTFiles[i])
    data = findNotch(osa_data)
    print(data)
    ctwlData.append(data[0])
    peakData.append(data[1])
    rData.append(data[2])
    n_ac_Data.append(data[3])
    n_dc_Data.append(data[4])
    
    # break

datasT['ctwl/nm'] = ctwlData
datasT['transmissionDepth/dB'] = peakData
datasT['r/%'] = rData
datasT['n_ac'] = n_ac_Data
datasT['n_dc'] = n_dc_Data


# 对解调仪读的温度特性文件遍历，拿到时间和中心波长
# for file in txtFiles:
#     txt_data = readText(file)
#     # print(txt_data)
#     ctwlData.extend(txt_data[1])
#     peakData.extend(txt_data[0])
    
# datasT['time'] = peakData
# datasT['ctwl/nm'] = ctwlData

    

    