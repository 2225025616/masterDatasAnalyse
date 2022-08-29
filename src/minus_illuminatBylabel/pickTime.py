# -*- coding: utf-8 -*-
# 再生过程中间隔两秒保存数据
# 再生过程中的时间和温度数据的时间对应，挑选对应温度
# 把相同时间对应的温度保存成数组，插入到元数据中，紧跟时间之后

# file1为要插入温度的文件
# file2为温度数据文件

import pandas as pd

def pickTime(file1, file2):
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)
    time1 = df1['time']
    timeTemp = df2['time']
    print(time1[0],'/t',timeTemp[1])








pickTime("../../resultDatas/20220823-1000-H1060-7mm-49DB/regenerationTR.csv", "../../resultDatas/20220823-1000-H1060-7mm-49DB/RFBGTemp.csv")