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
    wlDatas = list(df['ctwl/nm'])
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
        wl=[]
        # # t=[]
        wl.extend([wlDatas[j-200:j] for j in datas[i]])
        stepWlDatas.append([i for dt in wl for i in dt])
        # t.append([tempDatas[j-200:j] for j in datas[i]])
        # stepWlDatas[temp[i]] = wlList[0]
        # realTemps.extend(t)
        # break
    # tempPoints=dict(zip(temp, avargeWl))
    return temp, stepWlDatas, avargeWl









# 测试

# datas={
#     350: [883, 9854, 18828],
#     450: [1664, 8386, 10631, 17365, 19609, 26338],
#     550: [2441, 6918, 11415, 15891, 20387, 24867],
#     650: [3215, 5457, 12189, 14433, 21163, 23406],
#     750: [4725, 15990, 27234],
# }
# analyze('../../resultDatas/20220711-850-SMF28E/temperatureTest.csv', datas)