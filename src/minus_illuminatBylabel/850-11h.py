from readSpec import readSpec
import pandas as pd
from readTemp import readTemp
from pickTime import pickTime
from readCtwl import readCtwl
from analyseTemp import analyze


# 测试
# df = pd.DataFrame(
#     columns=('time', 'ctwl/nm', 'thresh/dBm', 'notch/dB', 'reflection/%'))
# regenerationSpec = readSpec(
#     "../../DataSource/RFBG-PolyimideSMF28E/20220829-850-re11h/regeneration/850_R.txt",  "../../DataSource/RFBG-PolyimideSMF28E/20220829-850-re11h/regeneration/850_T.txt","../../DataSource/RFBG-PolyimideSMF28E/20220829-850-re11h/originalT.CSV")
# df['time'] = regenerationSpec[0]
# # df['timeStamp'] = regenerationSpec[1]
# df['ctwl/nm'] = regenerationSpec[2]
# df['thresh/dBm'] = regenerationSpec[3]
# df['notch/dB'] = regenerationSpec[4]
# df['reflection/%'] = regenerationSpec[5]
# df.to_csv("../../resultDatas/20220829-850-re11h-SMF28E/regenerationTR.csv")
#
#
# timeDf = pd.DataFrame(columns=['time', 'temperature'])
# datetime = readTemp("../../DataSource/RFBG-PolyimideSMF28E/20220829-850-re11h/regeneration/temperature.txt", "../../DataSource/RFBG-PolyimideSMF28E/20220829-850-re11h/regeneration/temperature.TST")
# timeDf["time"] = datetime[0]
# # timeDf["timeStamp"] = datetime[1]
# timeDf["temperature"] = datetime[2]
# # print('hh:mm:ss: ',datetime[0][89])
# timeDf.to_csv("../../resultDatas/20220829-850-re11h-SMF28E/RFBGTemp.csv")
#
#
# dt=pickTime("../../resultDatas/20220829-850-re11h-SMF28E/regenerationTR.csv", "../../resultDatas/20220829-850-re11h-SMF28E/RFBGTemp.csv")
# dt.to_csv("../../resultDatas/20220829-850-re11h-SMF28E/rfbgTempTR.csv")


# wlDt = pd.DataFrame(columns=['time', 'ctwl'])
# data = readCtwl("../../DataSource/RFBG-PolyimideSMF28E/20220829-850-re11h/tempCheck/ctwlDatas.txt")
# wlDt["time"] = data[0]
# wlDt["ctwl"] = data[1]
# wlDt.to_csv("../../resultDatas/20220829-850-re11h-SMF28E/tempCheckCTWL0.csv")
#
#
# timeDf = pd.DataFrame(columns=['time', 'temperature'])
# datetime = readTemp("../../DataSource/RFBG-PolyimideSMF28E/20220829-850-re11h/tempCheck/temperature.txt", "../../DataSource/RFBG-PolyimideSMF28E/20220829-850-re11h/tempCheck/temperature.TST")
# timeDf["time"] = datetime[0]
# # timeDf["timeStamp"] = datetime[1]
# timeDf["temperature"] = datetime[2]
# print('hh:mm:ss: ',datetime[0][89])
# timeDf.to_csv("../../resultDatas/20220829-850-re11h-SMF28E/tempCheck0.csv")
#
#
# dt=pickTime("../../resultDatas/20220829-850-re11h-SMF28E/tempCheckCTWL0.csv", "../../resultDatas/20220829-850-re11h-SMF28E/tempCheck0.csv")
# dt.to_csv("../../resultDatas/20220829-850-re11h-SMF28E/checkTempCtwl0.csv")

# # analyze the temperaturetest resultDatas
datas={
    350: [1490, 16374, 31249, 45659],
    450: [2729, 13680, 17606, 28560, 32560, 42979],
    550: [3980, 11284, 18857, 26167, 333748, 41024],
    650: [5231, 8877, 20112, 23745, 35001, 38652],
    750: [6490, 21356, 36235],
}

tempDts = analyze('../../resultDatas/20220829-850-re11h-SMF28E/checkTempCtwl.csv', datas)
stepTemp = tempDts[0]
stepDf = pd.DataFrame(columns=stepTemp)
# for i in range(len(stepTemp)):
#     stepDf[stepTemp[i]] = tempDts[1][i] + [0] * (1200 - len(tempDts[1][i]))
# stepDf.to_csv("../../resultDatas/20220829-850-re11h-SMF28E/stepTempResult.csv")
print(tempDts[2])
print(tempDts[3])


dt={
    350:[841, 12101, 23345],
    450: [1618, 10577, 12880, 21821, 24124, 33089],
    550: [2393, 9112, 13657, 20379, 24902, 31621],
    650: [3170, 7646, 14433, 18915, 25678, 30159],
    750: [3946, 6188, 15210, 17451, 26454, 28697],
    850: [4725, 15990, 27234],
}


dts = {
    350: [883, 9854, 18828],
    450: [1664, 8386, 10631, 17365, 19609, 26338],
    550: [2441, 6918, 11415, 15891, 20387, 24867],
    650: [3215, 5457, 12189, 14433, 21163, 23406],
    750: [4725, 15990, 27234],
}