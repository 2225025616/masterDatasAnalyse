# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 17:57:37 2022

@author: Sunyali
"""

# 计算n_dc
# n_dc = 1.456*(ctwl1-ctwl0)/(overlapFactor*ctwl1)
# print('反射率：', r)
# print('平均折射率：',n_ac)
# 读取T透射数据文件，根据波长差值，计算n_dc

import pandas as pd
import numpy as np
# 根据公式计算n_dc
def calTn_dc(file):
    n_eff = 1.456
    overlap_factor = 0.8
    # 读取csv文件，拿出中心波长数据
    df = pd.read_csv(file)
    # print(df.head())
    wlDatas = df['ctwl/nm']
    # print(len(wlDatas))
    datas = np.diff(wlDatas,1)
    n_dc = []
    # print(datas)

    for i,ctwl in enumerate(wlDatas):
        if i==0:
            n_dc.append(0)
        else:
            n_dc.append(n_eff*datas[i-1]/(overlap_factor*ctwl))

    # print(len(n_dc))
    if list(df.columns).index('n_dc')<0:
        df.insert(loc=len(df.columns), column='n_dc', value=n_dc)
    else:
        df['n_dc'] = n_dc
    df.to_csv(file)

# 测试
# calTn_dc('../../resultDatas/20220711/regenerateT.csv')