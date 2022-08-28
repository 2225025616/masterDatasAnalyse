# 读取光源数据-to 数组

import os
import pandas as pd

def readIlluminat(filename):
    df = pd.read_csv(filename, header=32)
    # print(df.iloc(1)[0])
    # print(df.iloc(1)[1])
    # print(df.head())
    wlData = df.iloc(1)[0]
    peakData = df.iloc(1)[1]
    return wlData, peakData

# 测试
data = readIlluminat(r'../../DataSource/RFBG-PolyimideSMF28E/20220711-850/originalSpec.CSV')
# print(data[0][0])