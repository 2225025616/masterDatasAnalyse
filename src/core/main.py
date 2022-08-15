# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 22:18:53 2022

@author: Administrator
"""

# 操作文件，导出数据，写入指定的目录下
from toDataframeFormat import transTDatas, transRDatas, transRegenerateDatas, transTempDatas, transTempTime

#  20220711 实验数据导出
datasT = transTDatas("../../DataSource/RFBG-PolyimideSMF28E/20220711/regenerationOSA-T")
# print('TTTTTTTTTTTTTTTTTTTTTTTT')
datasTemp = transTempDatas("../../DataSource/RFBG-PolyimideSMF28E/20220711/TEMP-Check")
# print('*******************')
datasR = transRDatas("../../DataSource/RFBG-PolyimideSMF28E/20220711/regenerationOSA-R")
# print('RRRRRRRRRRRRRRR')
# /resultDatas/20220711
outputPath = "../../resultDatas/20220711"
datasT.to_csv(outputPath+"/regenerateT.csv")
datasTemp.to_csv(outputPath+"/temperatureTest.csv")
datasR.to_csv(outputPath+"/regenerateR.csv")


# 20220730实验数据导出
# outputPath = "../../resultDatas/20220728"
# dataTempTime = transTempTime("../../DataSource/RFBG-PolyimideSMF28E/20220730/temperatureDatas/TEMP.txt", "../../DataSource/RFBG-PolyimideSMF28E/20220730/temperatureDatas/20220804RFBG.TST")
# datasR = transRDatas("../../DataSource/RFBG-PolyimideSMF28E/20220730/regenerationOSA-R")
# datasR.to_csv(outputPath+"/regenerateR.csv")
# datasT = transTDatas("../../DataSource/RFBG-PolyimideSMF28E/20220730/regenerationOSA-T")
# datasT.to_csv(outputPath+"/regenerateT.csv")
# datasTempTest = transTempDatas("../../DataSource/RFBG-PolyimideSMF28E/20220730/TEMP-Check")
# datasTempTest.to_csv(outputPath+"/temperatureTest.csv")
# dataTempTime.to_csv(outputPath+"/temp_time.csv")
