# 分析温度特性
# 不同循环的升温、降温过程中的温度特性——3个升温、3个降温
# 同一温度——不同循环过程中的波长飘动


import pandas as pd
from collections import Counter
from decimal import Decimal, ROUND_HALF_UP
import pandas as pd

from statsmodels.tsa.arima.datasets.brockwell_davis_2002 import data


def analyze(file,dicts):
    df = pd.read_csv(file)
    tempDatas = list(df['temperature'])
    wlDatas = list(df['ctwl'])
    # print(tempDatas.most_common(3))
    # print(wlDatas.most_common(3))
    # print(wlDatas)

    temp = list(dicts.keys())
    # print('temp**********************')
    datas = [dicts[temp[i]] for i in range(len(temp))]
    avargeWl = dict()
    avargeTemp = dict()
    stepWlDatas = []
    # print(datas)
    for i in range(len(datas)):
        avargeWl[temp[i]] = [Decimal(sum(wlDatas[j-200:j])/200).quantize(Decimal("0.0000"), ROUND_HALF_UP) for j in datas[i]]
        avargeTemp[temp[i]] = [Decimal(sum(tempDatas[j-200:j])/200).quantize(Decimal("0.00"), ROUND_HALF_UP) for j in datas[i]]
        wl=[]
        # # t=[]
        wl.extend([wlDatas[j-200:j] for j in datas[i]])
        stepWlDatas.append([i for dt in wl for i in dt])
        # t.append([tempDatas[j-200:j] for j in datas[i]])
        # stepWlDatas[temp[i]] = wlList[0]
        # realTemps.extend(t)
        # break
    # tempPoints=dict(zip(temp, avargeWl))
    return temp, stepWlDatas, avargeWl, avargeTemp









# 测试
#
# datas={
#     350: [1297, 23279, 45242, 67118],
#     450: [2546, 20784, 24524, 42762, 46485, 64730],
#     550: [3796, 18379, 25776, 40345, 47745, 62324],
#     650: [5037, 15968, 27021, 37965, 48989, 59887],
#     750: [6291, 13572, 28271, 35553, 50107, 57540],
#     850: [7542, 11193, 29520, 33161, 51465, 55134],
#     950: [8794, 30779, 52742],
# }
# analyze('../../resultDatas/20220823-1000-H1060-7mm-49DB/checkTempCtwl.csv', datas)