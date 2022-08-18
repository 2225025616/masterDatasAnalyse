# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 23:08:57 2022

@author: Sunyali
"""




import pywt
import numpy as np
from pywt import wavedec
import matplotlib.pyplot as plt
# import copy




def dwt(data):
    #转为ndarray格式
    x=data[0]
    y=np.array(data[1])
    peakData = data[1]
    wlData = []
    
    print(len(data[1]))
    print('min y: ', min(y))
    print('min y: ', data[1].index(min(y)))
    
    
    
    coeffs = wavedec(y, 'db4', level=5)
    # coeffs_2 = copy.deepcopy(coeffs)
    for ix,val in enumerate(coeffs):
        if ix == 0:
            coeffs[ix] = np.zeros_like(val)
    y = pywt.waverec(coeffs, wavelet='db4')
    
    # for ix_2,val_2 in enumerate(coeffs_2):
    #     if ix_2 != 0: coeffs_2[ix_2] = np.zeros_like(val_2)
    # y_2 = pywt.waverec(coeffs_2,wavelet='db4') + 25
    
    print(y)
    # 根据拟合后的数据，找到大概透射深度的位置、及对应的波长
    y = y.tolist()
    pre_i = y.index(min(y))
    pre_ctwl = x[pre_i]
    print(pre_ctwl)
    print(pre_i)
    # 在预中心波长左右各120个点的范围内，再找透射深度及中心波长
    startIndex = pre_i-120 if pre_i-120>0 else 0
    endIndex = pre_i+120 if pre_i+120<len(x) else len(x)
    
    x_new = x[startIndex:endIndex]
    y_new = peakData[startIndex:endIndex]
    # 根据波谷值
    notch =min(y_new)
    # print('notch: ',notch)
    # print('peaks len: ',len(y_new))
    # print('x len: ',len(x_new))
    index = y_new.index(notch)
    # print('index orign: ', index)
    ctwl = x_new[index]
    print('ctwl orign: ', ctwl)
    print('*****')
    
    # 根据中心波长数值截取数据段，找波谷对应的索引 附近的光谱信息
    
    startIndex = index-150 if index-150>0 else 0
    endIndex = index+150 if index+150<len(x) else len(x)
    wlData = x[startIndex:endIndex]
    peakData = peakData[startIndex:endIndex]
    return wlData, peakData
    
    
# #用样条插值
# 间隔25个点，以25个点为一组，找最大、最小，得到两个数组————形成两个包络
# 用1次样条，插值成5000个点————最大值-成上包罗；最小值成下包络
# 上包罗+下包络/2 ————均值包络
# 实际曲线-均值包络=波谷临近范围
# 波谷临近范围的绝对值，再找临界点—阈值；找阈值以上的曲线索引————即得到波谷活跃段
# 在波谷活跃段找最小值——波谷光强
# 对波谷活跃段，进行二次你拟合——————光强和波长信息本来是高斯拟合，但是光谱仪得到的是光强单位是dbm——已经对光强进行lg运算
# 二次拟合后，得到中心波长
 
#进行样条差值
import scipy.interpolate as spi

def delbaseine(data):
    x = data[0]
    y = data[1]
    print('x len: ', len(x))
    x_max =[]
    y_max =[]
    x_min =[]
    y_min =[]
    i=0
    step = 25
    for i,d in enumerate(x):
        # print(i)
        if i*step+step<len(data[0]):
            yM =max(y[i*step:i*step+step-1])
            xM = x[i*step:i*step+step-1][y[i*step:i*step+step-1].index(yM)]
            x_max.append(xM)
            y_max.append(yM)
            ym =min(y[i*step:i*step+step-1])
            xm = x[i*step:i*step+step-1][y[i*step:i*step+step-1].index(ym)]
            x_min.append(xm)
            y_min.append(ym)
  
    
    # print('len: ',x_max)
    # print('len: ',y_max)
    #进行一阶样条差值
    ipo1_max=spi.splrep(x_max,y_max,k=1) #源数据点导入，生成参数
    ipo1_min=spi.splrep(x_min,y_min,k=1) #源数据点导入，生成参数
    iy1_max=spi.splev(x,ipo1_max) #根据观测点和样条参数，生成插值
    iy1_min=spi.splev(x,ipo1_min) #根据观测点和样条参数，生成插值
    
    iy1_arg = (iy1_max+iy1_min)/2
    #进行三次样条拟合
    ipo3_max=spi.splrep(x_max,y_max,k=3) #源数据点导入，生成参数
    ipo3_min=spi.splrep(x_min,y_min,k=3) #源数据点导入，生成参数
    iy3_max=spi.splev(x,ipo3_max) #根据观测点和样条参数，生成插值
    iy3_min=spi.splev(x,ipo3_min) #根据观测点和样条参数，生成插值
    iy3_arg = (iy3_max+iy3_min)/2
    
    
    iy1 = y - iy1_arg
    iy3 = y - iy3_arg
    
    # 从图可看出1次样条插值更好
    iy1_abs = abs(iy1)
    
    # 取阈值 0.1
    iy1_final = []
    x_final = []
    y_final = []
    for i,d in enumerate(iy1_abs):
        if d>0.01:
            iy1_final.append(d)
            x_final.append(x[i])
            y_final.append(y[i])
            
    ##作图
    # plt.figure(figsize=(18,12))
    # plt.plot(x,iy1_max,'r+',label='max')
    # plt.plot(x,iy1_min,'go',label='min')
    # plt.plot(x,iy1,'b+',label='interp1')
    # plt.plot(x,iy1_abs,'k.',label='interp1-abs')
    # plt.plot(x_final,iy1_final,'r+',label='interp1-abs')
    # plt.plot(x,y,'bo',label='prime')
    # plt.plot(x_final,y_final,'r*',label='final')
    # plt.title('interp-1-final')
    
    return x_final,y_final
        




# 测试 
# from readOsa import readDatas
# dt = readDatas('../../DataSource/RFBG-PolyimideSMF28E/20220730/regenerationOSA-T/W2233.CSV')
# delbaseine(dt)