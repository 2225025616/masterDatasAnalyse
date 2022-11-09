# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 15:41:00 2022

@author: Sunyali
"""
import numpy
# 读取label存的txt文件数据
# 时间、中心波长、带宽，光谱信息

import pandas as pd
from decimal import Decimal, ROUND_HALF_UP
import math
import time
import os
import matplotlib.pyplot as plt
# from collections import Counter

# 反射时间和透射时间对应
# 修正——两台光谱仪卡顿，时间不一致，调整时间对应，波长对应

# 读光谱文件，提取出中心波长、透射深度、反射峰值
# 透射光谱减去光源透射，得到的光谱信息
# T-depth = max- min
def readSpec(rFile,tFile,originalSpec):
    # 读取光谱数据
    with open(originalSpec) as f:
        df = f.readlines()[39:]
    f.close()
    # print(df)
    originalY = [Decimal(i.strip('\n').split(',')[1]) for i in df]

    timeR=[]
    timeT=[]
    ctwlDatas=[]
    tDepthDatas = []
    peakDatas=[]
    reflection = []
    n_acArr = []
    # 读反射文件
    rDatas = pd.read_csv(rFile, header=None)
    # print('*******RRRRRRRRRRRRRRRRRRRR***')
    for i in rDatas.index:
        line = rDatas.iloc[i][0].strip('\n').split('\t')

        # time.strptime 转为时间格式
        t = line[0]+' '+line[1]
        # t = time.strptime(t, "%Y/%m/%d %H:%M:%S")
        timeR.append(t)

    # ****************反射数据读取时间结束******************************
    # 读取透射文件
    TDatas = pd.read_csv(tFile, header=None)
    # print(len(fDatas))
    # print('TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT')
    # print('originalY: ', len(originalY))
    for i in TDatas.index:
        # print(i)
        # print(tt.strip('\n').split('\t') for tt in fDatas.iloc[i])
        # print(fDatas.iloc[i])
        line = TDatas.iloc[i][0].strip('\n').split('\t')
        # print(line)
        # print('YYYYYYYYYYYYYYYYYYYYYYYY')
        # time.strptime 转为时间格式
        t = line[0] + ' ' + line[1]
        timeT.append(t)

    # *************************读取透射数据时间结束******************************

    # 清洗数据
    # 透射时间、反射时间 对比，挑选R、透射深度数据
    timeDatas = timeR if len(timeR)<len(timeT) else timeT
    # 根据时间，挑选R文件中的波长、光谱【得到峰值】
    for i in rDatas.index:
        line = rDatas.iloc[i][0].strip('\n').split('\t')

        # time.strptime 转为时间格式
        t = line[0] + ' ' + line[1]
        if t in timeDatas:
            ctwl = line[2]
            ctwlDatas.append(ctwl)
            y = list(line[4:])
            # print('y: ',len(y))
            # 光栅反射光谱-光源反射光谱
            y = [eval(i) for i in y]
            # 得到反射峰值
            peak = Decimal(max(y))
            peakDatas.append(peak)

    # 根据时间，挑选T文件中的光谱，算出透射深度、R
    for i in TDatas.index:
        line = TDatas.iloc[i][0].strip('\n').split('\t')
        # time.strptime 转为时间格式
        t = line[0] + ' ' + line[1]
        # t = time.strptime(t, "%Y/%m/%d %H:%M:%S")
        if t in timeDatas:
            y = list(line[4:])
            # print('y: ',len(y))
            y=[eval(i) for i in y]
            # 光栅透射光谱-光源透射光谱
            # print(y[0])
            fbgY = [Decimal(y[i]) - Decimal(originalY[i]) for i, d in enumerate(y)]
            # print(fbgY[0])
            # 得到透射深度
            notch = Decimal(max(fbgY)) - Decimal(min(fbgY))
            r = Decimal((1 - Decimal(math.pow(10, -notch/10))))*100
            # print(notch)
            tDepthDatas.append(notch)
            reflection.append(r)
            overlapFactor = 0.8
            # print('r: ', r)
            # print(math.sqrt(r))
            a = Decimal(math.sqrt(r) if math.sqrt(r) < 0.99 else 0.99)
            # print('a: ', a)
            n_ac = Decimal(math.atanh(a) * ctwl / (overlapFactor * math.pi * float(12000) * 10 ** 6)).quantize(
                Decimal("0.0000000000000"), ROUND_HALF_UP)
            n_acArr.append(n_ac)
            # print(r)
            # break
    # stamp = time.mktime(time.strptime(t, "%Y/%m/%d %H:%M:%S"))
    timeStamp = [time.mktime(time.strptime(t, "%Y/%m/%d %H:%M:%S")) for t in timeDatas]

    return timeDatas, timeStamp, ctwlDatas, n_acArr, tDepthDatas, reflection



# 透射光谱减去光源，
# 利用小波变化，对减之后的光谱信息找透射波谷C
# 利用差分找两端的A、B，T-depth = C - (A+B)/2
import pywt
from pywt import wavedec
def readTdelOriginalSpec(tFile, L, illuminant):
    df = pd.read_csv(illuminant, header=31)
    illuminantWl = np.array(df.iloc(1)[0])
    illuminantPeak = np.array(df.iloc(1)[1])

    with open(tFile, 'r') as f:
        dfT = f.readlines()
    f.close()
    # print(dfT[0].split('\t').index('Y'))
    # print(len(dfT))
    fTimeArr=[]
    ctwlArr=[]
    t_depthArr=[]
    rArr=[]
    n_acArr=[]

    yIndex = dfT[0].split('\t').index('Y')
    xIndex = -1 if dfT[0].find('X')<0 else dfT[0].split('\t').index('X')
    for i in range(len(dfT)):
        if dfT[i].find('ctwl')<0:
            # print(dfT[i])n、\r、\t
            specD = dfT[i].rstrip('\n').rstrip('\t').split('\t')

            f_time = specD[0] + ' ' + specD[1]
            # f_time = time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(f_time))
            fTimeArr.append(f_time)

            # print(len(specD))
            # print('last: ',specD[-1])
            yT = numpy.array([eval(i) for i in specD[yIndex:]])


            if xIndex>0:
                x = specD[xIndex:yIndex]
                # 波长对应，——根据第一个波长数值判断
                if x[0] == illuminantWl[0] and len(x) == len(illuminantWl):
                    y = yT - illuminantPeak
                else:
                    # 找到原透射光谱在光源透射谱中的对应的索引，并比对值，然后找到波长对应的一一相减
                    s = np.where(illuminantWl == x[0])[0][0]
                    e = np.where(illuminantWl == x[-1])[0][0]
                    # print(illuminantPeak[s:e])
                    y = yT - illuminantPeak[s:e + 1]
            else:
                if len(yT) == len(illuminantPeak):
                    x = illuminantWl
                    y = yT - illuminantPeak
                else:
                    x = illuminantWl[0:len(yT)]
                    y = yT - illuminantPeak[0:len(yT)]
            # ************减去光源的光谱找到***********

            # 小波变换找到波谷
            # 转为ndarray格式
            peakData = list(y)

            # print('min y: ', min(y))
            # print('index y: ', peakData.index(min(y)))

            coeffs = wavedec(y, 'db4', level=5)
            # coeffs_2 = copy.deepcopy(coeffs)
            for ix, val in enumerate(coeffs):
                if ix == 0:
                    coeffs[ix] = np.zeros_like(val)
            y = list(pywt.waverec(coeffs, wavelet='db4'))
            # print(y)
            # plt.figure(figsize=(18,32))
            # plt.plot(x,y,'b+')
            # plt.plot(x,peakData,'r-')
            # plt.show()
            # 根据拟合后的数据，找到大概透射深度的位置、及对应的波长
            pre_i = y.index(min(y))
            # pre_ctwl = x[pre_i]
            # print(pre_ctwl)
            # print(pre_i)
            # 取以最小点为参考 两边对称的点
            # 在预中心波长左右各150个点的范围内，再找透射深度及中心波长
            startIndex = pre_i - 150 if pre_i - 150 > 0 else 0
            endIndex = pre_i + 150 if pre_i + 150 < len(x) else len(x)
            xFinal = x[startIndex:endIndex]
            yFinal = peakData[startIndex:endIndex]
            # 根据波谷值
            notch = min(yFinal)
            # print('notch: ', notch)
            # print('peaks len: ', len(yFinal))

            # 二次拟合
            coef = np.polyfit(xFinal, yFinal, 2)
            # y_fit = np.polyval(coef, xFinal)
            # 找出其中的峰值/对称点
            if coef[0] != 0:
                ctwl = -0.5 * coef[1] / coef[0]
                ctwl = round(ctwl, 4)
                ctwlArr.append(ctwl)
                # plt.plot(x_final, y_fit, 'b.')
                # plt.plot([ctwl]*5, np.linspace(min(y_final),max(y_final),5),'g--')
                # print('ctwl : ', ctwl)
            else:
                raise ValueError('Fail to fit.')

            # print('notch: ', notch)
            # print('x length: ', len(xFinal))

            # 找基准
            # 根据y差值，——间隔10个点，看差值
            index = yFinal.index(min(yFinal))
            y_10_l = yFinal[0:index]
            y_10_l.reverse()
            y_10_l = np.array(y_10_l)
            y_10_r = np.array(yFinal[index:-1])
            step = len(y_10_l) // 6 if len(y_10_l) < len(y_10_r) else len(y_10_r) // 6

            # 窗口滑动求差分，依次滑动
            dy_10_l = abs(np.diff(y_10_l, step))
            dy_10_r = abs(np.diff(y_10_r, step))
            # print(step)
            # print('--------------diff-----------------')
            # print(len(y_10_l))
            # print(len(y_10_r))
            #
            # print(len(dy_10_l))
            # print(len(dy_10_r))
            # 如果只有一侧长度为0，说明透射峰并没有完整的被记录——用一侧的最小值代替
            if len(y_10_r) == 0:
                print('no right: ', i)
                l_i = np.argwhere(dy_10_l == min(dy_10_l))[0][0]
                ref_l = y_10_l[l_i]
                ref_r = 0
            elif len(y_10_l) == 0:
                print('no lift: ', i)
                l_r = np.argwhere(dy_10_r == min(dy_10_r))[0][0]
                ref_r = y_10_r[l_r]
                ref_l = 0
            else:
                l_i = np.argwhere(dy_10_l == min(dy_10_l))[0][0]
                l_r = np.argwhere(dy_10_r == min(dy_10_r))[0][0]
                ref_l = y_10_l[l_i]
                ref_r = y_10_r[l_r]
            # print(ref_l)
            # print(ref_r)
            # 得到透射深度
            t_depth = Decimal(abs((ref_l + ref_r) / 2 - notch)).quantize(Decimal("0.0000"), ROUND_HALF_UP)
            t_depthArr.append(t_depth)
            # 计算反射率、有效折射率
            # 计算透射深度，找差值
            # print('透射深度: ', t_depth)
            # 并记下结果
            # 反射率单位为%， 要乘以100

            r = Decimal((1 - abs(math.pow(10, -t_depth / 10))) * 100).quantize(Decimal("0.00"), ROUND_HALF_UP)
            rArr.append(r)
            overlapFactor = 0.8
            # print('r: ', r)
            # print(math.sqrt(r))
            a = Decimal(math.sqrt(r) if math.sqrt(r) < 0.99 else 0.99)
            # print('a: ', a)
            n_ac = Decimal(math.atanh(a) * ctwl / (overlapFactor * math.pi * float(L) * 10 ** 6)).quantize(
                Decimal("0.0000000000000"), ROUND_HALF_UP)
            n_acArr.append(n_ac)
            # break

    return fTimeArr, ctwlArr, t_depthArr, rArr, n_acArr


# 不管光源的透射光谱如何
# 直接利用小波变换找透射峰
# 找T-depth的方法同上
def readTofWavedec(tFile, L, illuminant):
    if illuminant is None:
        print("Please   ")
    df = pd.read_csv(illuminant, header=31)
    x = np.array(df.iloc(1)[0])
    with open(tFile, 'r') as f:
        dfT = f.readlines()
    f.close()
    # print(dfT[0].split('\t').index('Y'))
    # print(len(dfT))
    fTimeArr = []
    ctwlArr = []
    t_depthArr = []
    rArr = []
    n_acArr = []

    yIndex = dfT[0].split('\t').index('Y')
    xIndex = -1 if dfT[0].find('X') < 0 else dfT[0].split('\t').index('X')

    for i in range(len(dfT)):
        # i=83
        if dfT[i].find('ctwl')<0:
            # print(dfT[i].split('\t'))
            specD =  dfT[i].rstrip('\n').rstrip('\t').split('\t')
            y = numpy.array([eval(i) for i in specD[yIndex:]])
            # print(specD[0])
            # print(specD[1])
            f_time = specD[0] + ' ' + specD[1]
            # f_time = time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(f_time))
            fTimeArr.append(f_time)
            if xIndex>0:
                x = [eval(i) for i in specD[xIndex:yIndex]]
    # ************透射光谱波长范围找到***********

            # 小波变换找到波谷
            # 转为ndarray格式
            peakData = list(y)

            # print('min y: ', min(y))
            # print('index y: ', peakData.index(min(y)))

            coeffs = wavedec(y, 'db4', level=5)
            # coeffs_2 = copy.deepcopy(coeffs)
            for ix, val in enumerate(coeffs):
                if ix == 0:
                    coeffs[ix] = np.zeros_like(val)
            y = list(pywt.waverec(coeffs, wavelet='db4'))
            # print(len(y))
            # print(y[-1])
            # plt.figure(figsize=(32,18))
            # plt.plot(x,peakData,'r-')
            # # plt.plot(x,y,'b+')
            # plt.show()
            # 根据拟合后的数据，找到大概透射深度的位置、及对应的波长
            pre_i = y.index(min(y))
            # pre_ctwl = x[pre_i]
            # print(pre_ctwl)
            # print(pre_i)
            # 取以最小点为参考 两边对称的点
            # 在预中心波长左右各150个点的范围内，再找透射深度及中心波长
            startIndex = pre_i - 150 if pre_i - 150 > 0 else 0
            endIndex = pre_i + 150 if pre_i + 150 < len(peakData) else len(peakData)
            xFinal = list(x[startIndex:endIndex])
            yFinal = list(peakData[startIndex:endIndex])
            # 根据波谷值
            if len(yFinal) > 0:
                notch = min(yFinal)
                # 二次拟合
                # print(i)
                # print(xFinal)
                # print(x[-1])
                # print('x: ', len(xFinal))
                # print('y: ', len(yFinal))
                coef = np.polyfit(xFinal, yFinal, 2)
                # y_fit = np.polyval(coef, xFinal)
                # 找出其中的峰值/对称点
                if coef[0] != 0:
                    ctwl = -0.5 * coef[1] / coef[0]
                    ctwl = round(ctwl, 4)
                    ctwlArr.append(ctwl)

                    # plt.plot(x_final, y_fit, 'b.')
                    # plt.plot([ctwl]*5, np.linspace(min(y_final),max(y_final),5),'g--')
                    # print('ctwl : ', ctwl)
                else:
                    raise ValueError('Fail to fit.')
                    # print('notch: ', notch)
                    # print('x length: ', len(xFinal))

                # 找基准
                # 根据y差值，——间隔10个点，看差值
                index = yFinal.index(min(yFinal))
                y_10_l = yFinal[0:index]
                y_10_l.reverse()
                y_10_l = np.array(y_10_l)
                y_10_r = np.array(yFinal[index:-1])
                step = len(y_10_l) // 6 if len(y_10_l) < len(y_10_r) else len(y_10_r) // 6

                # 窗口滑动求差分，依次滑动
                dy_10_l = abs(np.diff(y_10_l, step))
                dy_10_r = abs(np.diff(y_10_r, step))
                # print(step)
                print('--------------diff-----------------')
                # print(i)
                # print(len(y_10_l))
                # print(len(y_10_r))
                #
                # print(len(dy_10_l))
                # print(len(dy_10_r))

                # 如果只有一侧长度为0，说明透射峰并没有完整的被记录——用一侧的最小值代替
                if len(y_10_r) == 0:
                    print('no right: ', i)
                    l_i = np.argwhere(dy_10_l == min(dy_10_l))[0][0]
                    ref_l = y_10_l[l_i]
                    ref_r = 0
                elif len(y_10_l) == 0:
                    print('no lift: ', i)
                    l_r = np.argwhere(dy_10_r == min(dy_10_r))[0][0]
                    ref_r = y_10_r[l_r]
                    ref_l = 0
                else:
                    l_i = np.argwhere(dy_10_l == min(dy_10_l))[0][0]
                    l_r = np.argwhere(dy_10_r == min(dy_10_r))[0][0]
                    ref_l = y_10_l[l_i]
                    ref_r = y_10_r[l_r]
                # print(ref_l)
                # print(ref_r)
                # 得到透射深度
                t_depth = Decimal(abs((ref_l + ref_r) / 2 - notch)).quantize(Decimal("0.0000"), ROUND_HALF_UP)
                t_depthArr.append(t_depth)
            else:
                # notch = 0
                ctwl = ctwlArr[-1]
                ctwlArr.append(ctwl)
                # 得到透射深度
                t_depth = 0
                t_depthArr.append(t_depth)
            # print('notch: ', notch)
            # print('peaks len: ', len(yFinal))





            # 计算反射率、有效折射率
            # 计算透射深度，找差值
            # print('透射深度: ', t_depth)
            # 并记下结果
            # 反射率单位为%， 要乘以100

            r = Decimal((1 - abs(math.pow(10, -t_depth / 10))) * 100).quantize(Decimal("0.00"), ROUND_HALF_UP)
            rArr.append(r)

            overlapFactor = 0.8
            # print('r: ', r)
            # print(math.sqrt(r))
            a = Decimal(math.sqrt(r) if math.sqrt(r) < 0.99 else 0.99)
            # print('a: ', a)
            n_ac = Decimal(math.atanh(a) * ctwl / (overlapFactor * math.pi * float(L) * 10 ** 6)).quantize(
                Decimal("0.0000000000000"), ROUND_HALF_UP)
            n_acArr.append(n_ac)

    return fTimeArr, ctwlArr, t_depthArr, rArr, n_acArr



# 样条插值找透射峰波谷
# 计算T-depth的方法同上
import pandas as pd
import numpy as np
import math
import time
import os
from decimal import Decimal, ROUND_HALF_UP
#进行样条差值
import scipy.interpolate as spi

def readTofInterpolate(tFile, L, illuminant):
    with open(tFile, 'r') as f:
        dfT = f.readlines()
    f.close()
    # print(dfT[0].split('\t').index('Y'))
    print(tFile)
    fTimeArr = []
    ctwlArr = []
    t_depthArr = []
    rArr = []
    n_acArr = []

    if illuminant:
        # print("Please")
        df = pd.read_csv(illuminant, header=31)
        x = np.array(df.iloc(1)[0])
        xIndex = -1
    else:
        print("只有两个参数，光源数据可以不需要")
        xIndex = dfT[0].split('\t').index('X')

    yIndex = dfT[0].split('\t').index('Y')

    for i in range(len(dfT)):
        # i = 250
        if dfT[i].find('ctwl')<0:
            # print(dfT[i].split('\t'))
            specD = dfT[i].rstrip('\n').rstrip('\t').split('\t')
            y = numpy.array([eval(i) for i in specD[yIndex:]])
            f_time = specD[0] + ' ' + specD[1]
            # f_time = time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(f_time))
            fTimeArr.append(f_time)
            # print('i: ',i)
            # print(tFile)
            if xIndex>0:
                x =[eval(i) for i in specD[xIndex:yIndex]]
            # ************透射光谱波长范围找到***********


            # 样条插值找到波谷
            x_max = []
            y_max = []
            x_min = []
            y_min = []
            step = 25
            # # print(len(x))
            # print(len(y))
            print('i: ',i)
            for i, d in enumerate(y):
                if i * step + step < len(y):
                    # print("yyyyyy")
                    # print(y[i * step:i * step + step - 1])
                    # s=i * step
                    # l = i * step + step if i * step + step<len(x) else len(x)
                    print(len(x))
                    print('y: ',len(y))

                    print(i*step+step)
                    print('last: ',x[i*step+step])
                    print('l: ',i * step+step -i * step)
                    yM = max(y[i * step:i * step + step])
                    xM = x[i * step: i*step+step][list(y[i * step:i * step + step]).index(yM)]
                    x_max.append(xM)
                    y_max.append(yM)
                    ym = min(y[i * step:i * step + step])
                    # print(list(y[i * step:i * step + step]).index(ym))
                    # print(len(x[i*step: i*step+step]))
                    # print('all',x[i*step: i*step+step])
                    # print('s: ',x[i*step])
                    # print(len(y))

                    xm = x[i * step: i*step+step][list(y[i * step:i * step + step]).index(ym)]
                    x_min.append(xm)
                    y_min.append(ym)

            # print('len: ',x_max)
            # print('len: ',y_max)
            # 进行一阶样条差值
            ipo_max = spi.splrep(x_max, y_max, k=1)  # 源数据点导入，生成参数
            ipo_min = spi.splrep(x_min, y_min, k=1)  # 源数据点导入，生成参数
            y_max = spi.splev(x[0:len(y)], ipo_max)  # 根据观测点和样条参数，生成插值
            y_min = spi.splev(x[0:len(y)], ipo_min)  # 根据观测点和样条参数，生成插值
            y_arg = (y_max + y_min) / 2
            iy1 = y - y_arg
            # 通过差值，找到透射深度索引
            n_i = list(iy1).index(min(iy1))
            notch = list(y)[n_i]
            # print('1: ',notch)
            # print('iy1: ',min(iy1))

            iy1_abs = abs(iy1)
            # 取阈值 0.1
            iy1_final = []
            x_final = []
            y_final = []
            # 阈值合理化
            y_abs = list(abs(iy1))
            threshold = max(iy1_abs) * 0.5
            for i, d in enumerate(y_abs):
                if d > threshold:
                    iy1_final.append(d)
                    x_final.append(x[i])
                    y_final.append(y[i])

            # print('threshold: ', threshold)
            # print(y_final)
            # print(len(y_final))
            # print(min(y_final))
            ##作图
            # plt.figure(figsize=(18,12))
            # # 上包络
            # plt.plot(x,y_max,'r-',label='max')
            # # 下包络
            # plt.plot(x,y_min,'g-',label='min')
            # # 去基线
            # plt.plot(x,iy1-25.5,'b+',label='interp1')
            #
            # plt.show()
            # # 把所有的都翻上去
            # plt.plot(x,iy1_abs,'g*',label='interp1-abs')
            # plt.plot(x_final,iy1_final,'r+',label='interp1-abs')
            # plt.plot(x,y,'b-',label='prime')
            # plt.plot(x_final,y_final,'r*',label='final')
            # plt.title('interp-1-final')
            # plt.show()
            # 取以最小点为参考 两边对称的点
            index = list(y).index(notch)
            # print(len(y))
            # print('index = %d' % index)
            startI = index - 150 if index - 150 > 0 else 0
            endI = index + 150 if index + 150 < len(y) else len(y)
            # print('startI:',startI)
            # print('endI:',endI)
            yFinal = list(y[startI: endI])
            xFinal = x[startI: endI]
            # print('min: ',min(yFinal))
            # print('t: ',notch)
            # print(yFinal.index(notch))
            # plt.plot(x_final, y_final, 'k.')
            # 二次拟合
            coef = np.polyfit(xFinal, yFinal, 2)
            # y_fit = np.polyval(coef, xFinal)
            # 找出其中的峰值/对称点
            if coef[0] != 0:
                ctwl = -0.5 * coef[1] / coef[0]
                ctwl = round(ctwl, 4)
                ctwlArr.append(ctwl)
                # plt.plot(x_final, y_fit, 'b.')
                # plt.plot([ctwl]*5, np.linspace(min(y_final),max(y_final),5),'g--')
                # print('ctwl : ', ctwl)
            else:
                raise ValueError('Fail to fit.')

            peaks = yFinal
            # print('len peaks: ',len(peaks))
            # 找基准
            # 根据y差值，——间隔10个点，看差值
            # print('error i: ',i)

            ii = peaks.index(notch)
            y_10_l = peaks[0:ii]
            y_10_l.reverse()
            y_10_l = np.array(y_10_l)
            y_10_r = np.array(peaks[ii:-1])
            step = len(y_10_l) // 6 if len(y_10_l) < len(y_10_r) else len(y_10_r) // 6

            # 窗口滑动求差分，依次滑动
            dy_10_l = abs(np.diff(y_10_l, step))
            dy_10_r = abs(np.diff(y_10_r, step))
            # print(step)
            print('3333333333333-diff--33333333333')
            # print(len(dy_10_l))
            # print(len(dy_10_r))
            # 如果只有一侧长度为0，说明透射峰并没有完整的被记录——用一侧的最小值代替
            if len(y_10_r) == 0:
                print('no right: ', i)
                l_i = np.argwhere(dy_10_l == min(dy_10_l))[0][0]
                ref_l = y_10_l[l_i]
                ref_r = 0
            elif len(y_10_l) == 0:
                print('no lift: ', i)
                l_r = np.argwhere(dy_10_r == min(dy_10_r))[0][0]
                ref_r = y_10_r[l_r]
                ref_l = 0
            else:
                l_i = np.argwhere(dy_10_l == min(dy_10_l))[0][0]
                l_r = np.argwhere(dy_10_r == min(dy_10_r))[0][0]
                ref_l = y_10_l[l_i]
                ref_r = y_10_r[l_r]
            # print(ref_l)
            # print(ref_r)
            # 得到透射深度
            t_depth = Decimal(abs((ref_l + ref_r) / 2 - notch)).quantize(Decimal("0.0000"), ROUND_HALF_UP)
            t_depthArr.append(t_depth)
            # 计算反射率、有效折射率
            # 计算透射深度，找差值
            # print('透射深度: ', t_depth)
            # 并记下结果
            # 反射率单位为%， 要乘以100

            r = Decimal((1 - abs(math.pow(10, -t_depth / 10))) * 100).quantize(Decimal("0.00"), ROUND_HALF_UP)
            rArr.append(r)
            overlapFactor = 0.8
            # print('r: ', r)
            # print(math.sqrt(r))
            a = Decimal(math.sqrt(r) if math.sqrt(r) < 0.99 else 0.99)
            # print('a: ', a)
            n_ac = Decimal(math.atanh(a) * ctwl / (overlapFactor * math.pi * float(L) * 10 ** 6)).quantize(Decimal("0.0000000000000"), ROUND_HALF_UP)
            n_acArr.append(n_ac)
    return fTimeArr, ctwlArr, t_depthArr, rArr, n_acArr


# 测试
# data = readTdelOriginalSpec('../../DataSource/RTlabel/202207328-900-re11h/regeneration/T.txt', 12000, '../../DataSource/RFBG-PolyimideSMF28E/202207328-900-re11h/originalSpec.CSV')
# data = readTdelOriginalSpec('../../DataSource/RTlabel/H1060-7mm-48dB-1000-re2h-600-end/regeneration/T.txt', 12000, '../../DataSource/RTlabel/H1060-7mm-48dB-1000-re2h-600-end/originalSpec.CSV')
# data1 = readTofWavedec('../../DataSource/RTlabel/H1060-7mm-48dB-1000-re2h-600-end/regeneration/T.txt', 12000, '../../DataSource/RTlabel/H1060-7mm-48dB-1000-re2h-600-end/originalSpec.CSV')
# data3 = readTofInterpolate('../../DataSource/RTlabel/H1060-7mm-48dB-1000-re2h-600-end/regeneration/T.txt', 12000, '../../DataSource/RTlabel/H1060-7mm-48dB-1000-re2h-600-end/originalSpec.CSV')

# print(data)
