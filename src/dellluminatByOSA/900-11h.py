from readT import readT
import pandas as pd
from findTCtwl import findTR
from readTemp import readTemp
from pickTime import pickTime
from readRCSV import readR
from analyseTemp import analyze


# analyze the temperaturetest resultDatas

timeDf = pd.DataFrame(columns=['time', 'temperature'])
# datetime = readTemp("../../DataSource/RFBG-PolyimideSMF28E/202207328-900-re11h/tempCheck/temperature.txt", "../../DataSource/RFBG-PolyimideSMF28E/202207328-900-re11h/tempCheck/temperature.TST")
# timeDf["time"] = datetime[0]
# # timeDf["timeStamp"] = datetime[1]
# timeDf["temperature"] = datetime[2]
# print('hh:mm:ss: ',datetime[0][89])
# timeDf.to_csv("../../resultDatas/20220728-900-SMF28E/tempCheck.csv")
#
#
# dt=pickTime("../../resultDatas/20220728-900-SMF28E/tempCheckCTWL.csv", "../../resultDatas/20220728-900-SMF28E/tempCheck.csv")
# dt.to_csv("../../resultDatas/20220728-900-SMF28E/checkTempCtwl.csv")

datas = {
    350: [841, 12101, 23345],
    450: [1618, 10577, 12880, 21821, 24124, 33089],
    550: [2393, 9112, 13657, 20379, 24902, 31621],
    650: [3170, 7646, 14433, 18915, 25678, 30159],
    750: [3946, 6188, 15210, 17451, 26454, 28697],
    850: [4725, 15990, 27234],
}

tempDts = analyze('../../resultDatas/20220728-900-SMF28E/checkTempCtwl.csv', datas)
stepTemp = tempDts[0]
stepDf = pd.DataFrame(columns=stepTemp)
for i in range(len(stepTemp)):
    stepDf[stepTemp[i]] = tempDts[1][i] + [0] * (1200 - len(tempDts[1][i]))
stepDf.to_csv("../../resultDatas/20220728-900-SMF28E/stepTempResult.csv")
print(tempDts[2])
print(tempDts[3])

