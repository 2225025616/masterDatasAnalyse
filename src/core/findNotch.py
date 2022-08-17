# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 20:35:12 2022

@author: Administrator
"""

# 寻峰功能实现
# 根据最大点，找对称的点——如果原本不对称，以少的找点
# 拿到合适的点后，高斯拟合，找到峰值及对应的中心波长
# 如果不满足高斯拟合，则按照scipy的find_peaks找光强的绝对值的峰值，在根据对应索引找到中心波长
# 以中心波长对应的索引为中心，左右各以10个点为窗口求光强差值，以求光强插值最小的数据段
# 再以5个点为窗口，求最小的数据段
# 左边从-1找差值较小的，求平均数作为左基准
# 右边从0找差值最小的，求平均数作为右基准

# 根据notch、左右基准，计算透射深度
# 根据透射深度，计算反射率、n_ac


import numpy as np
import math
# 利用scipy的寻谷函数
from scipy.signal import find_peaks

# 利用波谷，左右+/-1的光谱信息
# 高斯拟合

def calFinalInfo(data, L=12):
    # 计算反射率、有效折射率
    # 计算透射深度，找差值
    ctwl = data[0]
    tDepth = data[1]
    print('透射深度: ', tDepth)
    # 并记下结果
    r = 1 - abs(math.pow(10, -tDepth/10))
    overlapFactor = 0.8
    print('r: ', r)
    print(math.sqrt(r))
    a = math.sqrt(r) if math.sqrt(r)<0.99 else 0.99
    print(math.atanh(a))
    print(math.atanh(a)*ctwl)
    n_ac = math.atanh(a)*ctwl/(overlapFactor*math.pi*float(L)*10**6)
    # n_dc = 1.456/(overlapFactor*ctwl)
    print('反射率：', r)
    print('平均折射率：',n_ac)
    return ctwl,tDepth,r,n_ac


def findNotch(data):
    # 中心波长信息
    xData = data[0]
    # 光强信息
    yData = data[1]
    notch=min(data[1])
    ctwl=data[0][data[1].index(min(data[1]))]
    
    # 根据中心波长找对称的范围
    r_
    
    print('peak: ', min(data[1]))
    y = [abs(i) for i in yData]
#    根据光谱的能量进行高斯拟合
    y = np.array(y)
    # y = np.array(yData)
    # print(y)
    print("guss**********************")
    
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
    if det!=0:
        # 利用高斯公式，最小二乘法——得到peak、对应的中心波长
        bMatrix = ((xMatrixT*xMatrix).I*xMatrixT)*zMatrix.T
        # 根据高斯函数，利用b、x求得峰值信息和半宽高
        # lnYmax - (Xmax*Xmax/S) =B0
        # B1 =2Xmax/S
        # - 1/S =B2
        b0, b1, b2 = float(bMatrix[0][0]), float(bMatrix[1][0]), float(bMatrix[2][0])
        # print('b0={} ,b1={}, b2={}'.format(b0,b1,b2))
        s = -1/b2
        ctwl = s*b1/2
        notch = math.exp(b0+ctwl**2/s)
        print('波谷={}, 中心波长={}'.format(notch,ctwl))
    else:
        readNotch = find_peaks()
    return ctwl, notch
    
  




# 测试
from readOsa import readDatas
from delBaseline import dwt
osaDatas = readDatas("../../DataSource/RFBG-PolyimideSMF28E/20220730/regenerationOSA-T/D0302.DT8", "../../DataSource/RFBG-PolyimideSMF28E/20220730/regenerationOSA-T/W0302.CSV")
print(osaDatas)
orignData = dwt(osaDatas)




