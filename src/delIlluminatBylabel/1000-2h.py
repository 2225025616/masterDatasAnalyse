from readT import readTdelOriginalSpec, readTofWavedec, readTofInterpolate
import pandas as pd
from readTime import readTemp
from contactTempData import pickTime
from readRCtwl import readCtwl
from analyseTemp import analyze

#
# df = pd.DataFrame(
#     columns=('time', 'ctwl/nm', 'notch/dB', 'reflection/%', 'n_ac'))
# regenerationSpec = readTdelOriginalSpec(
#     "../../DataSource/RTlabel/H1060-7mm-48dB-1000-re2h-600-end/regeneration/T.txt",12000, '../../DataSource/RTlabel/H1060-7mm-48dB-1000-re2h-600-end/originalSpec.CSV')
# df['time'] = regenerationSpec[0]
# # fTimeArr, ctwlArr, t_depthArr, rArr, n_acArr
# df['ctwl/nm'] = regenerationSpec[1]
# df['notch/dB'] = regenerationSpec[2]
# df['reflection/%'] = regenerationSpec[3]
# df['n_ac'] = regenerationSpec[4]
# df.to_csv("../../resultDatas/H1060-7mm-48dB-1000-re2h-600-end/RFBG-T-delOriginalSpec.csv")
#

# df1 = pd.DataFrame(
#     columns=('time', 'ctwl/nm', 'notch/dB', 'reflection/%', 'n_ac'))
# data1 = readTofWavedec(
#     "../../DataSource/RTlabel/H1060-7mm-48dB-1000-re2h-600-end/regeneration/T.txt",12000, '../../DataSource/RTlabel/H1060-7mm-48dB-1000-re2h-600-end/originalSpec.CSV')
# df1['time'] = data1[0]
# # fTimeArr, ctwlArr, t_depthArr, rArr, n_acArr
# df1['ctwl/nm'] = data1[1]
# df1['notch/dB'] = data1[2]
# df1['reflection/%'] = data1[3]
# df1['n_ac'] = data1[4]
# df1.to_csv("../../resultDatas/H1060-7mm-48dB-1000-re2h-600-end/RFBG-T-Wavedec.csv")

#
# df = pd.DataFrame(
#     columns=('time', 'ctwl/nm', 'notch/dB', 'reflection/%', 'n_ac'))
# data2 = readTofInterpolate(
#     "../../DataSource/RTlabel/H1060-7mm-48dB-1000-re2h-600-end/regeneration/T.txt",12000, '../../DataSource/RTlabel/H1060-7mm-48dB-1000-re2h-600-end/originalSpec.CSV')
# df['time'] = data2[0]
# # fTimeArr, ctwlArr, t_depthArr, rArr, n_acArr
# df['ctwl/nm'] = data2[1]
# df['notch/dB'] = data2[2]
# df['reflection/%'] = data2[3]
# df['n_ac'] = data2[4]
# df.to_csv("../../resultDatas/H1060-7mm-48dB-1000-re2h-600-end/RFBG-T-Interpolate.csv")

#
# timeDf = pd.DataFrame(columns=['time', 'temperature'])
# datetime = readTemp("../../DataSource/RTlabel/H1060-7mm-48dB-1000-re2h-600-end/regeneration/temperature.txt", "../../DataSource/RTlabel/H1060-7mm-48dB-1000-re2h-600-end/regeneration/temperature.TST")
# timeDf["time"] = datetime[0]
# # timeDf["timeStamp"] = datetime[1]
# timeDf["temperature"] = datetime[2]
# # print('hh:mm:ss: ',datetime[0][89])
# timeDf.to_csv("../../resultDatas/H1060-7mm-48dB-1000-re2h-600-end/RFBG-temperature.csv")

dt=pickTime("../../resultDatas/H1060-7mm-48dB-1000-re2h-600-end/RFBG-T-Interpolate.csv", "../../resultDatas/H1060-7mm-48dB-1000-re2h-600-end/RFBG-temperature.csv")
dt.to_csv("../../resultDatas/H1060-7mm-48dB-1000-re2h-600-end/RFBG-T-Interpolate-TT.csv")

dt=pickTime("../../resultDatas/H1060-7mm-48dB-1000-re2h-600-end/RFBG-T-Wavedec.csv", "../../resultDatas/H1060-7mm-48dB-1000-re2h-600-end/RFBG-temperature.csv")
dt.to_csv("../../resultDatas/H1060-7mm-48dB-1000-re2h-600-end/RFBG-T-Wavedec-TT.csv")

dt=pickTime("../../resultDatas/H1060-7mm-48dB-1000-re2h-600-end/RFBG-T-delOriginalSpec.csv", "../../resultDatas/H1060-7mm-48dB-1000-re2h-600-end/RFBG-temperature.csv")
dt.to_csv("../../resultDatas/H1060-7mm-48dB-1000-re2h-600-end/RFBG-T-delOriginalSpec-TT.csv")


# wlDt = pd.DataFrame(columns=['time', 'ctwl'])
# data = readCtwl("../../DataSource/RTlabel/H1060-7mm-48dB-1000-re2h-600-end/tempCheck/ctwlDatas.txt")
# wlDt["time"] = data[0]
# wlDt["ctwl"] = data[1]
# wlDt.to_csv("../../resultDatas/H1060-7mm-48dB-1000-re2h-600-end/tempCheckCTWL0.csv")
#
#
# timeDf = pd.DataFrame(columns=['time', 'temperature'])
# datetime = readTemp("../../DataSource/RTlabel/H1060-7mm-48dB-1000-re2h-600-end/tempCheck/temperature.txt", "../../DataSource/RTlabel/H1060-7mm-48dB-1000-re2h-600-end/tempCheck/temperature.TST")
# timeDf["time"] = datetime[0]
# # timeDf["timeStamp"] = datetime[1]
# timeDf["temperature"] = datetime[2]
# print('hh:mm:ss: ',datetime[0][89])
# timeDf.to_csv("../../resultDatas/H1060-7mm-48dB-1000-re2h-600-end/tempCheck0.csv")
#
#
# dt=pickTime("../../resultDatas/H1060-7mm-48dB-1000-re2h-600-end/tempCheckCTWL0.csv", "../../resultDatas/H1060-7mm-48dB-1000-re2h-600-end/tempCheck0.csv")
# dt.to_csv("../../resultDatas/H1060-7mm-48dB-1000-re2h-600-end/checkTempCtwl0.csv")

# # analyze the temperaturetest resultDatas
datas={
    350: [1490, 16374, 31249, 45659],
    450: [2729, 13680, 17606, 28560, 32560, 42979],
    550: [3980, 11284, 18857, 26167, 333748, 41024],
    650: [5231, 8877, 20112, 23745, 35001, 38652],
    750: [6490, 21356, 36235],
}

tempDts = analyze('../../resultDatas/H1060-7mm-48dB-1000-re2h-600-end/checkTempCtwl.csv', datas)
stepTemp = tempDts[0]
stepDf = pd.DataFrame(columns=stepTemp)
# for i in range(len(stepTemp)):
#     stepDf[stepTemp[i]] = tempDts[1][i] + [0] * (1200 - len(tempDts[1][i]))
# stepDf.to_csv("../../resultDatas/H1060-7mm-48dB-1000-re2h-600-end/stepTempResult.csv")
print(tempDts[2])
print(tempDts[3])
