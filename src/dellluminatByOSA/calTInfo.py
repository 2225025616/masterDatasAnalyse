# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 16:03:48 2022

@author: Sunyali
"""

# 计算反射率、有效折射率
# 计算透射深度，找差值
# print('透射深度: ', t_depth)
# 并记下结果
# 反射率单位为%， 要乘以100

import math
# import numpy as np
from decimal import Decimal

# 根据斜率，找基准
def calTInfo(ctwl, t_depth, L=12):

    r = Decimal((1 - Decimal(abs(math.pow(10, -t_depth/10)))*100))
    overlapFactor = 0.8
    # print('r: ', r)
    # print(math.sqrt(r))
    a = Decimal(Decimal(math.sqrt(r)) if Decimal(math.sqrt(r))<0.99 else 0.99)
    # print('a: ', a)
    # print(float(format(math.atanh(a),'.4f')))
    # print(float(format(math.atanh(a),'.4f'))*ctwl)
    n_ac = Decimal(math.atanh(a))*ctwl/Decimal(Decimal(overlapFactor*math.pi)*float(L)*10**6)
    # print('反射率：', r)
    # print('平均折射率：',n_ac)
    return r, n_ac
    
