# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 20:35:12 2022

@author: Administrator
"""

# 寻峰功能实现
# 根据最大点及带宽，通过高斯拟合，找到峰值


import numpy as np
import math

def findThresh(data, L=12):
    xData = data[0]
    yData = data[1]
    print(data[2])
    print(data[3])
    peak = 0
    y = [abs(i) for i in yData]
#    根据光谱的能量进行高斯拟合
    y = np.array(y)
    # y = np.array(yData)
    # print(y)
    print('guss**********************')
    
    zMatrix = np.matrix(np.log(y))
    # print('z 矩阵: ',zMatrix)
    # 构造 X 矩阵
    xMatrixT = np.matrix(np.reshape(np.concatenate((np.ones((len(y))), xData, np.multiply(np.array(xData), np.array(xData)))), (3, len(y))))
    xMatrix = np.matrix(xMatrixT.T)
    # print("X矩阵: ", xMatrix)
    # 根据最小二乘原理，构成B的广义最小二乘解
    print('B')
    det = np.linalg.det((xMatrixT*xMatrix))
    print(det)
    if det == 0:
        peak=max(data[1])
        ctwl=data[0][data[1].index(peak)]
    else:
        print((xMatrixT*xMatrix).I*xMatrixT)
        print(((xMatrixT*xMatrix).I*xMatrixT))
        bMatrix = ((xMatrixT*xMatrix).I*xMatrixT)*zMatrix.T
        print('B矩阵:', bMatrix)
    
        # 根据高斯函数，利用b、x求得峰值信息和半宽高
        # lnYmax - (Xmax*Xmax/S) =B0
        # B1 =2Xmax/S
        # - 1/S =B2
        b0, b1, b2 = float(bMatrix[0][0]), float(bMatrix[1][0]), float(bMatrix[2][0])
        # print('b0={} ,b1={}, b2={}'.format(b0,b1,b2))
        s = -1/b2
        ctWl = s*b1/2
        peak = math.exp(b0+ctWl**2/s)
    print('半宽={} ,波谷={}, 中心波长={}'.format(s, peak, ctWl))
    # 计算反射率、有效折射率
    # 并记下结果
    # r = 1 - abs(math.pow(10, -peak/10))
    # overlapFactor = 0.8
    # a = math.sqrt(r) if math.sqrt(r)<0.99 else 0.99
    # # print(math.sqrt(r))
    # # print(math.atanh(a))
    # # print(math.atanh(a)*ctWl)
    # n_ac = math.atanh(a)*ctWl/(overlapFactor*math.pi*float(L)*10**6)
    # n_dc = 1.456/(overlapFactor*ctWl)
    # print('反射率：', r)
    # print('平均折射率：',n_ac)
    # print('dc: ', n_dc)
    return ctWl, peak



# 测试
# from readTByOSA import readTDatas
# osaDatas = readTDatas('../../DataSource/RFBG-PolyimideSMF28E/20220711/regenerationOSA-T/D0016.DT8','../../DataSource/RFBG-PolyimideSMF28E/20220711/regenerationOSA-T/W0016.csv')
# data = findThresh(osaDatas)
# print(data)



