from readR import readRInfo

import pandas as pd











# 读取反射文件，集合反射数据
rDatas = readRInfo('../../DataSource/H-S-1000/regeneration/HS-R')
dt = pd.DataFrame(columns=['time', 'H1060WL', 'H1060Peak_Power', 'SMF28EWL', 'SMF28EPeak_Power'])
dt['time'] = rDatas[0]
dt['H1060WL'] = rDatas[1]
dt['H1060Peak_Power'] = rDatas[2]
dt['SMF28EWL'] = rDatas[3]
dt['SMF28EPeak_Power'] = rDatas[4]

