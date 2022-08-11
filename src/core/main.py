# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 22:18:53 2022

@author: Administrator
"""

# 操作文件，导出数据，写入指定的目录下
from toDataframeFormat import transRDatas, transTDatas, transTempDatas, transTempTime

#  20220711 实验数据导出
# datasR = transRDatas("../../DataSource/RFBG-PolyimideSMF28E/20220711/regenerationOSA-R")
# datasT = transTDatas("../../DataSource/RFBG-PolyimideSMF28E/20220711/regenerationOSA-T")
# datasTemp = transTempDatas("../../DataSource/RFBG-PolyimideSMF28E/20220711/TEMP-Check")
# # /resultDatas/20220711
# outputPath = "../../resultDatas/20220711"
# datasR.to_csv(outputPath+"/reflection.csv")
# datasT.to_csv(outputPath+"/transmission.csv")
# datasTemp.to_csv(outputPath+"/temp-check.csv")


# 20220730实验数据导出
outputPath = "../../resultDatas/20220728"
dataTempTime = transTempTime("../../DataSource/RFBG-PolyimideSMF28E/20220730/temperatureDatas/TEMP.txt", "../../DataSource/RFBG-PolyimideSMF28E/20220730/temperatureDatas/20220804RFBG.TST")
# datasR = transRDatas("../../DataSource/RFBG-PolyimideSMF28E/20220730/regenerationOSA-R")
# datasR.to_csv(outputPath+"/reflection.csv")
datasT = transTDatas("../../DataSource/RFBG-PolyimideSMF28E/20220730/regenerationOSA-T")
datasT.to_csv(outputPath+"/transmission.csv")
# datasTempTest = transTempDatas("../../DataSource/RFBG-PolyimideSMF28E/20220730/TEMP-Check")
# datasTempTest.to_csv(outputPath+"/tempCheckTest.csv")
dataTempTime.to_csv(outputPath+"/tempCheckTest.csv")
