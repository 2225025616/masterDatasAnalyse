# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 20:35:12 2022

@author: Administrator
"""

# 寻峰功能实现
# 根据最大点及带宽，通过高斯拟合，找到峰值


import numpy as np
import math

# 利用波谷，左右+/-1的光谱信息
# 高斯拟合



# 利用高斯公式，最小二乘法——得到Ymax、对应的x
def findNotch(data, L=12):
    
    xData = data[0]
    yData = data[1]
    
    
    
    ref = max(data[1])
    notch=min(data[1])
    ctwl=data[0][data[1].index(min(data[1]))]
    s=0
    print('ref: ', ref)
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
        bMatrix = ((xMatrixT*xMatrix).I*xMatrixT)*zMatrix.T
        # print(((xMatrixT*xMatrix).I*xMatrixT))
        # print('B矩阵:', bMatrix)
    
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
    # 计算反射率、有效折射率
    # 计算透射深度，找差值
    # notch = abs(abs(notch)- abs(ref))
    print('last notch: ', notch)
    # 并记下结果
    # r = 1 - abs(math.pow(10, -notch/10))
    # overlapFactor = 0.8
    # print('r: ', r)
    # print(math.sqrt(r))
    # a = math.sqrt(r) if math.sqrt(r)<0.99 else 0.99
    # print(math.atanh(a))
    # print(math.atanh(a)*ctwl)
    # n_ac = math.atanh(a)*ctwl/(overlapFactor*math.pi*float(L)*10**6)
    # n_dc = 1.456/(overlapFactor*ctwl)
    # print('反射率：', r)
    # print('平均折射率：',n_ac)
    print('peak,: ', min(data[1]))
    return ctwl, notch


# 利用scipy的寻谷函数
from scipy.signal import find_peaks
def findNotchByScipy(data, L=12):
    readNotch = find_peaks()
  
    
  
    
  
    
  
    
  


from scipy.optimize import curve_fit
from scipy import stats

def gauss_function(x, a, x0, sigma):
    return a*np.exp(-(x-x0)**2/(2*sigma**2))
 
    


def findNorchByCurve(data, L=12):
    x = data[0]
    y = data[1]
    ctwl = data[2]
    print(ctwl)
    print('!!!!!!!!!!!!!*****************!!!!!!!!!!!!!!!!!!!')
   
    # popt, pcov = curve_fit(gauss_function, x, y, p0 = [1, mean, sigma])

# 测试
from readTByOSA import readTDatas
osaDatas = readTDatas("../../DataSource/RFBG-PolyimideSMF28E/20220730/regenerationOSA-T/D0302.DT8", "../../DataSource/RFBG-PolyimideSMF28E/20220730/regenerationOSA-T/W0302.CSV")
findNorchByCurve(osaDatas)




