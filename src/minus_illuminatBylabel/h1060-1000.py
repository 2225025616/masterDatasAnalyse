from readSpec import readSpec
import pandas as pd
from readTemp import readTemp
from pickTime import pickTime
from readCtwl import readCtwl

# 测试
# df = pd.DataFrame(
#     columns=('time', 'ctwl/nm', 'thresh/dBm', 'notch/dB', 'reflection/%'))
# regenerationSpec = readSpec(
#     "../../DataSource/H1060/1000-7mm-down_600/regeneration/1000-R.txt",  "../../DataSource/H1060/1000-7mm-down_600/regeneration/1000-T.txt","../../DataSource/H1060/1000-7mm-down_600/originalT.CSV")
# df['time'] = regenerationSpec[0]
# # df['timeStamp'] = regenerationSpec[1]
# df['ctwl/nm'] = regenerationSpec[2]
# df['thresh/dBm'] = regenerationSpec[3]
# df['notch/dB'] = regenerationSpec[4]
# df['reflection/%'] = regenerationSpec[5]
# df.to_csv("../../resultDatas/20220823-1000-H1060-7mm-49DB/regenerationTR.csv")
#
#
# timeDf = pd.DataFrame(columns=['time', 'temperature'])
# datetime = readTemp("../../DataSource/H1060/1000-7mm-down_600/regeneration/temperature.txt", "../../DataSource/H1060/1000-7mm-down_600/regeneration/temperature.TST")
# timeDf["time"] = datetime[0]
# # timeDf["timeStamp"] = datetime[1]
# timeDf["temperature"] = datetime[2]
# # print('hh:mm:ss: ',datetime[0][89])
# timeDf.to_csv("../../resultDatas/20220823-1000-H1060-7mm-49DB/RFBGTemp.csv")
#

# dt=pickTime("../../resultDatas/20220823-1000-H1060-7mm-49DB/regenerationTR.csv", "../../resultDatas/20220823-1000-H1060-7mm-49DB/RFBGTemp.csv")
# dt.to_csv("../../resultDatas/20220823-1000-H1060-7mm-49DB/rfbgTempTR.csv")


wlDt = pd.DataFrame(columns=['time', 'ctwl'])
data = readCtwl("../../DataSource/H1060/1000-7mm-down_600/tempCheck/ctwlDatas.txt")
wlDt["time"] = data[0]
wlDt["ctwl"] = data[1]
wlDt.to_csv("../../resultDatas/20220823-1000-H1060-7mm-49DB/tempCheckCTWL.csv")


timeDf = pd.DataFrame(columns=['time', 'temperature'])
datetime = readTemp("../../DataSource/H1060/1000-7mm-down_600/tempCheck/temperature.txt", "../../DataSource/H1060/1000-7mm-down_600/tempCheck/temperature.TST")
timeDf["time"] = datetime[0]
# timeDf["timeStamp"] = datetime[1]
timeDf["temperature"] = datetime[2]
# print('hh:mm:ss: ',datetime[0][89])
timeDf.to_csv("../../resultDatas/20220823-1000-H1060-7mm-49DB/tempCheck0.csv")


dt=pickTime("../../resultDatas/20220823-1000-H1060-7mm-49DB/tempCheckCTWL.csv", "../../resultDatas/20220823-1000-H1060-7mm-49DB/tempCheck0.csv")
dt.to_csv("../../resultDatas/20220823-1000-H1060-7mm-49DB/checkTempCtwl.csv")