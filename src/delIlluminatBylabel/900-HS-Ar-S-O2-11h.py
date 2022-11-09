from readT import readTofWavedec, readTofInterpolate
import pandas as pd
from readTime import readTemp
from contactTempData import pickTime
from readRCtwl import readCtwl
from analyseTemp import analyze
#
# df1 = pd.DataFrame(
#     columns=('time', 'ctwl/nm', 'notch/dB', 'reflection/%', 'n_ac'))
# data1 = readTofWavedec(
#     "../../DataSource/TTlabel/Ar-900—power1.6nm-hs-Ar-s-o2/RFBG/Ar-t.txt",12000, '../../DataSource/TTlabel/Ar-900—power1.6nm-hs-Ar-s-o2/RFBG/originalT.CSV')
# df1['time'] = data1[0]
# # fTimeArr, ctwlArr, t_depthArr, rArr, n_acArr
# df1['ctwl/nm'] = data1[1]
# df1['notch/dB'] = data1[2]
# df1['reflection/%'] = data1[3]
# df1['n_ac'] = data1[4]
# df1.to_csv("../../resultDatas/900-HS-Ar-S-O2-power0.2nm/RFBG-ArS-Wavedec-T.csv")
#
# df1 = pd.DataFrame(
#     columns=('time', 'ctwl/nm', 'notch/dB', 'reflection/%', 'n_ac'))
# data1 = readTofWavedec(
#     "../../DataSource/TTlabel/Ar-900—power1.6nm-hs-Ar-s-o2/RFBG/HS-T/O2-t.txt",12000, '../../DataSource/TTlabel/Ar-900—power1.6nm-hs-Ar-s-o2/RFBG/originalT.CSV')
# df1['time'] = data1[0]
# # fTimeArr, ctwlArr, t_depthArr, rArr, n_acArr
# df1['ctwl/nm'] = data1[1]
# df1['notch/dB'] = data1[2]
# df1['reflection/%'] = data1[3]
# df1['n_ac'] = data1[4]
# df1.to_csv("../../resultDatas/900-HS-Ar-S-O2-power0.2nm/RFBG-o2S-Wavedec-T.csv")
#
# #
# df = pd.DataFrame(
#     columns=('time', 'ctwl/nm', 'notch/dB', 'reflection/%', 'n_ac'))
# data2 = readTofInterpolate(
#     "../../DataSource/TTlabel/Ar-900—power1.6nm-hs-Ar-s-o2/RFBG/Ar-t.txt",12000, '../../DataSource/TTlabel/Ar-900—power1.6nm-hs-Ar-s-o2/RFBG/originalT.CSV')
# df['time'] = data2[0]
# # fTimeArr, ctwlArr, t_depthArr, rArr, n_acArr
# df['ctwl/nm'] = data2[1]
# df['notch/dB'] = data2[2]
# df['reflection/%'] = data2[3]
# df['n_ac'] = data2[4]
# df.to_csv("../../resultDatas/900-HS-Ar-S-O2-power0.2nm/RFBG-ArS-Interpolate-T.csv")

# df = pd.DataFrame(
#     columns=('time', 'ctwl/nm', 'notch/dB', 'reflection/%', 'n_ac'))
# data2 = readTofInterpolate(
#     "../../DataSource/TTlabel/Ar-900—power1.6nm-hs-Ar-s-o2/RFBG/O2-t.txt",12000, '../../DataSource/TTlabel/Ar-900—power1.6nm-hs-Ar-s-o2/RFBG/originalT.CSV')
# df['time'] = data2[0]
# # fTimeArr, ctwlArr, t_depthArr, rArr, n_acArr
# df['ctwl/nm'] = data2[1]
# df['notch/dB'] = data2[2]
# df['reflection/%'] = data2[3]
# df['n_ac'] = data2[4]
# df.to_csv("../../resultDatas/900-HS-Ar-S-O2-power0.2nm/RFBG-o2S-Interpolate-T.csv")
#
# timeDf = pd.DataFrame(columns=['time', 'temperature'])
# datetime = readTemp("../../DataSource/TTlabel/Ar-900—power1.6nm-hs-Ar-s-o2/RFBG/temperature.txt", "../../DataSource/TTlabel/Ar-900—power1.6nm-hs-Ar-s-o2/RFBG/temperature.TST")
# timeDf["time"] = datetime[0]
# # timeDf["timeStamp"] = datetime[1]
# timeDf["temperature"] = datetime[2]
# # print('hh:mm:ss: ',datetime[0][89])
# timeDf.to_csv("../../resultDatas/900-HS-Ar-S-O2-power0.2nm/RFBG-temperature.csv")


# dt=pickTime("../../resultDatas/900-HS-Ar-S-O2-power0.2nm/RFBG-ArS-Interpolate-T.csv", "../../resultDatas/900-HS-Ar-S-O2-power0.2nm/RFBG-temperature.csv")
# dt.to_csv("../../resultDatas/900-HS-Ar-S-O2-power0.2nm/RFBG-ArS-Interpolate-TT.csv")
dt=pickTime("../../resultDatas/900-HS-Ar-S-O2-power0.2nm/RFBG-o2S-Interpolate-T.csv", "../../resultDatas/900-HS-Ar-S-O2-power0.2nm/RFBG-temperature.csv")
dt.to_csv("../../resultDatas/900-HS-Ar-S-O2-power0.2nm/RFBG-o2S-Interpolate-TT.csv")


# wlDt = pd.DataFrame(columns=['time', 'ctwl'])
# data = readCtwl("../../DataSource/TTlabel/Ar-900—power1.6nm-hs-Ar-s-o2/tempCheck/ctwlDatas.txt")
# wlDt["time"] = data[0]
# wlDt["ctwl"] = data[1]
# wlDt.to_csv("../../resultDatas/900-HS-Ar-S-O2-power0.2nmtempCheckCTWL0.csv")
#
#
# timeDf = pd.DataFrame(columns=['time', 'temperature'])
# datetime = readTemp("../../DataSource/TTlabel/Ar-900—power1.6nm-hs-Ar-s-o2/tempCheck/temperature.txt", "../../DataSource/TTlabel/Ar-900—power1.6nm-hs-Ar-s-o2/tempCheck/temperature.TST")
# timeDf["time"] = datetime[0]
# # timeDf["timeStamp"] = datetime[1]
# timeDf["temperature"] = datetime[2]
# print('hh:mm:ss: ',datetime[0][89])
# timeDf.to_csv("../../resultDatas/900-HS-Ar-S-O2-power0.2nmtempCheck0.csv")
#
#
# dt=pickTime("../../resultDatas/900-HS-Ar-S-O2-power0.2nmtempCheckCTWL0.csv", "../../resultDatas/900-HS-Ar-S-O2-power0.2nmtempCheck0.csv")
# dt.to_csv("../../resultDatas/900-HS-Ar-S-O2-power0.2nmcheckTempCtwl0.csv")

# # analyze the temperaturetest resultDatas
datas={
    350: [1490, 16374, 31249, 45659],
    450: [2729, 13680, 17606, 28560, 32560, 42979],
    550: [3980, 11284, 18857, 26167, 333748, 41024],
    650: [5231, 8877, 20112, 23745, 35001, 38652],
    750: [6490, 21356, 36235],
}

tempDts = analyze('../../resultDatas/900-HS-Ar-S-O2-power0.2nm/checkTempCtwl.csv', datas)
stepTemp = tempDts[0]
stepDf = pd.DataFrame(columns=stepTemp)
# for i in range(len(stepTemp)):
#     stepDf[stepTemp[i]] = tempDts[1][i] + [0] * (1200 - len(tempDts[1][i]))
# stepDf.to_csv("../../resultDatas/900-HS-Ar-S-O2-power0.2nmstepTempResult.csv")
print(tempDts[2])
print(tempDts[3])
