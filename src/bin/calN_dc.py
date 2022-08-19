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


import numpy as np
# 根据公式计算n_dc
def calTn_dc(file):
    n_eff = 1.456
    overlap_factor = 0.8
    # 读取csv文件，拿出中心波长数据
    datas = np.loadtxt(file)
    print(datas.he)
    
    
# 