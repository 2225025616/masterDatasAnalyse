# -*- coding: utf-8 -*-
"""
Created on Sun Aug  23 15:35:12 2022

@author: sunyali
"""
# 减去光源曲线
# 得到透射深度
# 根据光谱在透射峰对应的索引位置，找适合拟合的数据段


from decimal import Decimal
def minus(data, dataSource):
    # 确保一一对应
    # 波长一一对应，找打索引，对应减去光强
    # 由此，减到了波长的光源干扰，最大-最小=透射深度
    peaks = [eval(i) for i in data[1:]]

    # x = dataSource[0]
    y = dataSource[1]
    # print(y)
    # print(peaks)
    # specStart = peaks.index(y[0])
    # specLen = len(y)

    # peaks = peaks[specStart:specLen]

    # 分别对应减去光源
    peakData = [Decimal(peaks[i])-Decimal(y[i]) for i,d in enumerate(peaks)]
    notch = Decimal(max(peakData)) - Decimal(min(peakData))
    #
    # index = peaks.index(notch)
    # fitData = wlDatas[index-5:index+5]
    return notch