from readT import readTdelOriginalSpec, readTofWavedec, readTofInterpolate
import pandas as pd
from readTime import readTemp
from contactTempData import pickTime
from readRCtwl import readCtwl
from analyseTemp import analyze


# df = pd.DataFrame(
#     columns=('time', 'ctwl/nm', 'notch/dB', 'reflection/%', 'n_ac'))
# regenerationSpec = readTdelOriginalSpec(
#     "../../DataSource/TTlabel/H-S-1000/regeneration/HS-T/H_T.txt",12000, '../../DataSource/TTlabel/H-S-1000/regeneration/HS-T/H-originalT.CSV')
# df['time'] = regenerationSpec[0]
# # fTimeArr, ctwlArr, t_depthArr, rArr, n_acArr
# df['ctwl/nm'] = regenerationSpec[1]
# df['notch/dB'] = regenerationSpec[2]
# df['reflection/%'] = regenerationSpec[3]
# df['n_ac'] = regenerationSpec[4]
# df.to_csv("../../resultDatas/H-S-1000/RFBG-H-delOriginalSpec-T.csv")
#
# df = pd.DataFrame(
#     columns=('time', 'ctwl/nm', 'notch/dB', 'reflection/%', 'n_ac'))
# regenerationSpec = readTdelOriginalSpec(
#     "../../DataSource/TTlabel/H-S-1000/regeneration//HS-T/S_T.txt",12000, '../../DataSource/TTlabel/H-S-1000/regeneration/HS-T/S-originalT.CSV')
# df['time'] = regenerationSpec[0]
# # fTimeArr, ctwlArr, t_depthArr, rArr, n_acArr
# df['ctwl/nm'] = regenerationSpec[1]
# df['notch/dB'] = regenerationSpec[2]
# df['reflection/%'] = regenerationSpec[3]
# df['n_ac'] = regenerationSpec[4]
# df.to_csv("../../resultDatas/H-S-1000/RFBG-S-delOriginalSpec-T.csv")
#
#
# df1 = pd.DataFrame(
#     columns=('time', 'ctwl/nm', 'notch/dB', 'reflection/%', 'n_ac'))
# data1 = readTofWavedec(
#     "../../DataSource/TTlabel/H-S-1000/regeneration/HS-T/H_T.txt",12000, '../../DataSource/TTlabel/H-S-1000/regeneration/HS-T/H-originalT.CSV')
# df1['time'] = data1[0]
# # fTimeArr, ctwlArr, t_depthArr, rArr, n_acArr
# df1['ctwl/nm'] = data1[1]
# df1['notch/dB'] = data1[2]
# df1['reflection/%'] = data1[3]
# df1['n_ac'] = data1[4]
# df1.to_csv("../../resultDatas/H-S-1000/RFBG-H-Wavedec-T.csv")
#
# df1 = pd.DataFrame(
#     columns=('time', 'ctwl/nm', 'notch/dB', 'reflection/%', 'n_ac'))
# data1 = readTofWavedec(
#     "../../DataSource/TTlabel/H-S-1000/regeneration//HS-T/S_T.txt",12000, '../../DataSource/TTlabel/H-S-1000/regeneration/HS-T/S-originalT.CSV')
# df1['time'] = data1[0]
# # fTimeArr, ctwlArr, t_depthArr, rArr, n_acArr
# df1['ctwl/nm'] = data1[1]
# df1['notch/dB'] = data1[2]
# df1['reflection/%'] = data1[3]
# df1['n_ac'] = data1[4]
# df1.to_csv("../../resultDatas/H-S-1000/RFBG-S-Wavedec-T.csv")
#
#
# df = pd.DataFrame(
#     columns=('time', 'ctwl/nm', 'notch/dB', 'reflection/%', 'n_ac'))
# data2 = readTofInterpolate(
#     "../../DataSource/TTlabel/H-S-1000/regeneration/HS-T/H_T.txt",12000, '../../DataSource/TTlabel/H-S-1000/regeneration/HS-T/H-originalT.CSV')
# df['time'] = data2[0]
# # fTimeArr, ctwlArr, t_depthArr, rArr, n_acArr
# df['ctwl/nm'] = data2[1]
# df['notch/dB'] = data2[2]
# df['reflection/%'] = data2[3]
# df['n_ac'] = data2[4]
# df.to_csv("../../resultDatas/H-S-1000/RFBG-H-Interpolate-T.csv")
#
# df = pd.DataFrame(
#     columns=('time', 'ctwl/nm', 'notch/dB', 'reflection/%', 'n_ac'))
# data2 = readTofInterpolate(
#     "../../DataSource/TTlabel/H-S-1000/regeneration//HS-T/S_T.txt",12000, '../../DataSource/TTlabel/H-S-1000/regeneration/HS-T/S-originalT.CSV')
# df['time'] = data2[0]
# # fTimeArr, ctwlArr, t_depthArr, rArr, n_acArr
# df['ctwl/nm'] = data2[1]
# df['notch/dB'] = data2[2]
# df['reflection/%'] = data2[3]
# df['n_ac'] = data2[4]
# df.to_csv("../../resultDatas/H-S-1000/RFBG-S-Interpolate-T.csv")

timeDf = pd.DataFrame(columns=['time', 'temperature'])
datetime = readTemp("../../DataSource/TTlabel/H-S-1000/regeneration/temperature.txt", "../../DataSource/TTlabel/H-S-1000/regeneration/temperature.TST")
timeDf["time"] = datetime[0]
# timeDf["timeStamp"] = datetime[1]
timeDf["temperature"] = datetime[2]
# print('hh:mm:ss: ',datetime[0][89])
timeDf.to_csv("../../resultDatas/H-S-1000/RFBG-temperature.csv")


dt=pickTime("../../resultDatas/H-S-1000/RFBG-S-Interpolate-T.csv", "../../resultDatas/H-S-1000/RFBG-temperature.csv")
dt.to_csv("../../resultDatas/H-S-1000/RFBG-S-Interpolate-TT.csv")
dt=pickTime("../../resultDatas/H-S-1000/RFBG-H-Interpolate-T.csv", "../../resultDatas/H-S-1000/RFBG-temperature.csv")
dt.to_csv("../../resultDatas/H-S-1000/RFBG-H-Interpolate-TT.csv")

dt=pickTime("../../resultDatas/H-S-1000/RFBG-S-Wavedec-T.csv", "../../resultDatas/H-S-1000/RFBG-temperature.csv")
dt.to_csv("../../resultDatas/H-S-1000/RFBG-S-Wavedec-TT.csv")
dt=pickTime("../../resultDatas/H-S-1000/RFBG-H-Wavedec-T.csv", "../../resultDatas/H-S-1000/RFBG-temperature.csv")
dt.to_csv("../../resultDatas/H-S-1000/RFBG-H-Wavedec-TT.csv")

dt=pickTime("../../resultDatas/H-S-1000/RFBG-S-delOriginalSpec-T.csv", "../../resultDatas/H-S-1000/RFBG-temperature.csv")
dt.to_csv("../../resultDatas/H-S-1000/RFBG-S-delOriginalSpec-TT.csv")
dt=pickTime("../../resultDatas/H-S-1000/RFBG-H-delOriginalSpec-T.csv", "../../resultDatas/H-S-1000/RFBG-temperature.csv")
dt.to_csv("../../resultDatas/H-S-1000/RFBG-H-delOriginalSpec-TT.csv")


# wlDt = pd.DataFrame(columns=['time', 'ctwl'])
# data = readCtwl("../../DataSource/TTlabel/H-S-1000/tempCheck/ctwlDatas.txt")
# wlDt["time"] = data[0]
# wlDt["ctwl"] = data[1]
# wlDt.to_csv("../../resultDatas/H-S-1000/tempCheckCTWL0.csv")
#
#
# timeDf = pd.DataFrame(columns=['time', 'temperature'])
# datetime = readTemp("../../DataSource/TTlabel/H-S-1000/tempCheck/temperature.txt", "../../DataSource/TTlabel/H-S-1000/tempCheck/temperature.TST")
# timeDf["time"] = datetime[0]
# # timeDf["timeStamp"] = datetime[1]
# timeDf["temperature"] = datetime[2]
# print('hh:mm:ss: ',datetime[0][89])
# timeDf.to_csv("../../resultDatas/H-S-1000/tempCheck0.csv")
#
#
# dt=pickTime("../../resultDatas/H-S-1000/tempCheckCTWL0.csv", "../../resultDatas/H-S-1000/tempCheck0.csv")
# dt.to_csv("../../resultDatas/H-S-1000/checkTempCtwl0.csv")

# # analyze the temperaturetest resultDatas
datas={
    350: [1490, 16374, 31249, 45659],
    450: [2729, 13680, 17606, 28560, 32560, 42979],
    550: [3980, 11284, 18857, 26167, 333748, 41024],
    650: [5231, 8877, 20112, 23745, 35001, 38652],
    750: [6490, 21356, 36235],
}

tempDts = analyze('../../resultDatas/H-S-1000/checkTempCtwl.csv', datas)
stepTemp = tempDts[0]
stepDf = pd.DataFrame(columns=stepTemp)
# for i in range(len(stepTemp)):
#     stepDf[stepTemp[i]] = tempDts[1][i] + [0] * (1200 - len(tempDts[1][i]))
# stepDf.to_csv("../../resultDatas/H-S-1000/stepTempResult.csv")
print(tempDts[2])
print(tempDts[3])
