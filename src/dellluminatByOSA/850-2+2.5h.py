from readSpecCSV import readCSV
import pandas as pd
from findTCtwl import findTR
from readTemp import readTemp
from pickTime import pickTime
from readRCSV import readR
from analyseTemp import analyze

# 850°C 再生过程。减去光源光谱，计算透射深度

# 读取T文件，集中数据
# df = pd.DataFrame(
#     columns=('time', 'ctwl/nm', 'notch/dB', 'reflection/%'))
# originalT = readCSV('../../DataSource/RFBG-PolyimideSMF28E/20220711-850-re4.5h/originalSpec.CSV')
# regenerationSpec = findTR('../../DataSource/RFBG-PolyimideSMF28E/20220711-850-re4.5h/regenerationOSA-T', originalT)
# df['time'] = regenerationSpec[0]
# # df['timeStamp'] = regenerationSpec[1]
# df['ctwl/nm'] = regenerationSpec[1]
# df['notch/dB'] = regenerationSpec[2]
# df['reflection/%'] = regenerationSpec[3]
# df.to_csv("../../resultDatas/20220711-850-SMF28E/delOriginalSpecRFBG-TInfo.csv")

#  读取R文件，集中R数据和反射峰
# df = pd.DataFrame(
#     columns=('time', 'ctwl/nm', 'thresh/dBm', 'reflection/%'))
# regenerationR = readR('../../DataSource/RFBG-PolyimideSMF28E/20220711-850-re4.5h/regenerationOSA-R')
# df['time'] = regenerationR[0]
# # df['timeStamp'] = regenerationSpec[1]
# df['ctwl/nm'] = regenerationR[1]
# df['thresh/dBm'] = regenerationR[2]
# df.to_csv("../../resultDatas/20220711-850-SMF28E/delOriginalSpecRFBG-RChanges.csv")



# analyze the temperaturetest resultDatas
datas = {
    350: [883, 9854, 18828],
    450: [1664, 8386, 10631, 17365, 19609, 26338],
    550: [2441, 6918, 11415, 15891, 20387, 24867],
    650: [3215, 5457, 12189, 14433, 21163, 23406],
    750: [4725, 15990, 27234],
}

tempDts = analyze('../../resultDatas/20220711-850-SMF28E/temperatureTest.csv', datas)
stepTemp = tempDts[0]
stepDf = pd.DataFrame(columns=stepTemp)
for i in range(len(stepTemp)):
    stepDf[stepTemp[i]] = tempDts[1][i] + [0] * (1200 - len(tempDts[1][i]))
stepDf.to_csv("../../resultDatas/20220711-850-SMF28E/stepTempResult.csv")
print(tempDts[2])
print(tempDts[3])


dt={
    350: [841, 12101, 23345],
    450: [1618, 10577, 12880, 21821, 24124, 33089],
    550: [2393, 9112, 13657, 20379, 24902, 31621],
    650: [3170, 7646, 14433, 18915, 25678, 30159],
    750: [3946, 6188, 15210, 17451, 26454, 28697],
    850: [4725, 15990, 27234],
}

