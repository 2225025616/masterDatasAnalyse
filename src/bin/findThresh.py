# -*- coding: utf-8 -*-
"""
Created on Sun Aug  23 15:35:12 2022

@author: sunyali
"""


# 对光谱强度 寻峰功能实现
# 根据最大点，找到峰值


from pywt import wavedec, waverec
import copy
import math
import numpy as np


def findPeak(data):
    peak = max(data)
    return abs(peak)
# 寻峰功能实现
# 非均匀最小二乘


def findNotch(data):
    x = np.array(len(data))
    y = data
    notch = 0
    r = 0
    # 小波变换求notch
    coeffs = wavedec(y, 'db4', level=5)
    # coeffs_2 = copy.deepcopy(coeffs)
    for ix, val in enumerate(coeffs):
        if ix == 0:
            coeffs[ix] = np.zeros_like(val)
    y = waverec(coeffs, wavelet='db4')
    # print('777777777777777777777777')
    # 根据拟合后的数据，找到大概透射深度的位置、及对应的波长
    y = y.tolist()
    pre_i = y.index(min(y))
    if pre_i > 0:
        print(pre_i)
        # print(len(x))
        # print(x)
        # pre_ctwl = x[pre_i]
        # print(pre_ctwl)
        # 在预中心波长左右各120个点的范围内，再找透射深度及中心波长
        startIndex = pre_i - 120 if pre_i - 120 > 0 else 0
        endIndex = pre_i + 120 if pre_i + 120 < len(y) else len(y)

        # x_new = x[startIndex:endIndex]
        y = y[startIndex:endIndex]
        # 根据波谷值
        notch = min(y)
        # print(notch)
        index = y.index(notch)
        y_10_l = y[0:index]
        y_10_l.reverse()
        y_10_l = np.array(y_10_l)
        y_10_r = np.array(y[index:-1])
        step = len(y_10_l)//6 if len(y_10_l) < len(y_10_r) else len(y_10_r)//6
        # 窗口滑动求差分，依次滑动
        dy_10_l = abs(np.diff(y_10_l, step))
        dy_10_r = abs(np.diff(y_10_r, step))
        # print('--------------diff-----------------')
        # print(len(dy_10_l))
        # print(len(dy_10_r))
        # print(min(dy_10_l))
        # print(min(dy_10_r))
        l_i = np.argwhere(dy_10_l == min(dy_10_l))[0][0]
        l_r = np.argwhere(dy_10_r == min(dy_10_r))[0][0]
        # print(l_i)
        # print(l_r)
        ref_l = y_10_l[l_i]
        ref_r = y_10_r[l_r]
        # print(ref_l)
        # print(ref_r)
        notch = (ref_l+ref_r)/2-notch
        # 计算反射率、有效折射率
        # 并记下结果
        r = 1 - abs(math.pow(10, -notch/10))

    return abs(notch), r


# 测试
# from readTByOSA import readTDatas
# osaDatas = readTDatas('../../DataSource/RFBG-PolyimideSMF28E/20220711/regenerationOSA-T/D0016.DT8','../../DataSource/RFBG-PolyimideSMF28E/20220711/regenerationOSA-T/W0016.csv')
# data = findThresh(osaDatas)
# print(data)
