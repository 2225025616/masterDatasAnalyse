from readSpec import readSpec
import pandas as pd
from readTemp import readTemp


# 测试
df = pd.DataFrame(
    columns=('time', 'ctwl/nm', 'thresh/dBm', 'notch/dB', 'reflection/%'))
regenerationSpec = readSpec(
    "../../DataSource/H1060/1000-7mm-down_600/regeneration/1000-R.txt",  "../../DataSource/H1060/1000-7mm-down_600/regeneration/1000-T.txt","../../DataSource/H1060/1000-7mm-down_600/originalT.CSV")
df['time'] = regenerationSpec[0]
df['ctwl/nm'] = regenerationSpec[1]
df['thresh/dBm'] = regenerationSpec[2]
df['notch/dB'] = regenerationSpec[3]
df['reflection/%'] = regenerationSpec[4]
df.to_csv("../../resultDatas/20220823-1000-H1060-7mm-49DB/1000-regeneration.csv")


timeDf = pd.DataFrame(columns=['time', 'temperature'])
datetime = readTemp("../../DataSource/H1060/1000-7mm-down_600/regeneration/temperature.txt", "../../DataSource/H1060/1000-7mm-down_600/regeneration/temperature.TST")
timeDf["time"] = datetime[0]
timeDf["temperature"] = datetime[1]
# print('hh:mm:ss: ',datetime[0][89])
timeDf.to_csv("../../resultDatas/20220823-1000-H1060-7mm-49DB/RFBGTemp.csv")

