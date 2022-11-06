# 读取光源数据、光谱仪透射数据
# 投射数据-光源透射 = 光栅本身透射光谱
# 根据减光源之后的透射数据，根据样条插值——找到对称的透射峰；再根据二次拟合，找到中心波长
    # 用样条插值
    # 间隔25个点，以25个点为一组，找最大、最小，得到两个数组————形成两个包络
    # 用1次样条，插值成5000个点————最大值-成上包罗；最小值成下包络
    # 上包罗+下包络/2 ————均值包络
    # 实际曲线-均值包络=波谷临近范围
    # 波谷临近范围的绝对值，再找临界点—阈值；找阈值以上的曲线索引————即得到波谷活跃段
    # 在波谷活跃段找最小值——波谷光强
    # 对波谷活跃段，进行二次你拟合——————光强和波长信息本来是高斯拟合，但是光谱仪得到的是光强单位是dbm——已经对光强进行lg运算
    # 二次拟合后，得到中心波长

#     *******************************方法二*************************************
    # 小波变换

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math
import time
import os
from decimal import Decimal, ROUND_HALF_UP
#进行样条差值
import scipy.interpolate as spi

def readT1(tFile, L, illuminant):
    dfT = pd.read_csv(tFile, header=32)
    df = pd.read_csv(illuminant, header=32)
    x = dfT.iloc(1)[0].tolist()
    peakData = np.array(dfT.iloc(1)[1])
    illuminantWl = np.array(df.iloc(1)[0])
    illuminantPeak = np.array(df.iloc(1)[1])
    f_time = os.path.getmtime(tFile)
    fTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(f_time))
    # tWl = [map(lambda x: x[0] - x[1], (data[1], srcPeak))]
    print(x[0])
    print(illuminantWl[0])
    # 波长对应，——根据第一个波长数值判断
    if x[0] == illuminantWl[0] and len(peakData) == len(illuminantPeak):
        y = peakData - illuminantPeak
    else:
        # 找到原透射光谱在光源透射谱中的对应的索引，并比对值，然后找到波长对应的一一相减
        s = illuminantWl.index(x[0])
        e = illuminantWl.index(x[-1])
        y = peakData - illuminantPeak[s:e+1]
    # ************减去光源的光谱找到***********

    # 样条插值找到波谷
    x_max = []
    y_max = []
    x_min = []
    y_min = []
    step = 25
    print(len(x))
    print(len(y))
    for i, d in enumerate(x):
        if i * step + step < len(illuminantWl):
            # print("yyyyyy")
            # print(y[i * step:i * step + step - 1])
            yM = max(y[i * step:i * step + step - 1])
            xM = x[i * step:i * step + step - 1][list(y[i * step:i * step + step - 1]).index(yM)]
            x_max.append(xM)
            y_max.append(yM)
            ym = min(y[i * step:i * step + step - 1])
            xm = x[i * step:i * step + step - 1][list(y[i * step:i * step + step - 1]).index(ym)]
            x_min.append(xm)
            y_min.append(ym)

    # print('len: ',x_max)
    # print('len: ',y_max)
    # 进行一阶样条差值
    ipo_max = spi.splrep(x_max, y_max, k=1)  # 源数据点导入，生成参数
    ipo_min = spi.splrep(x_min, y_min, k=1)  # 源数据点导入，生成参数
    y_max = spi.splev(x, ipo_max)  # 根据观测点和样条参数，生成插值
    y_min = spi.splev(x, ipo_min)  # 根据观测点和样条参数，生成插值
    y_arg = (y_max + y_min) / 2
    iy1 = y - y_arg
    # 通过差值，找到透射深度索引
    n_i = list(iy1).index(min(iy1))
    notch = list(y)[n_i]
    print('1: ',notch)
    print('iy1: ',min(iy1))

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

    print('threshold: ', threshold)
    print(y_final)
    print(len(y_final))
    print(min(y_final))
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
    print(len(y))
    print('index = %d' % index)
    startI = index - 150 if index - 150 > 0 else 0
    endI = index + 150 if index + 150 < len(y) else len(y)
    print('startI:',startI)
    print('endI:',endI)
    yFinal = list(y[startI: endI])
    xFinal = x[startI: endI]
    print('min: ',min(yFinal))
    print('t: ',notch)
    print(yFinal.index(notch))
    # plt.plot(x_final, y_final, 'k.')
    # 二次拟合
    coef = np.polyfit(xFinal, yFinal, 2)
    # y_fit = np.polyval(coef, xFinal)
    # 找出其中的峰值/对称点
    if coef[0] != 0:
        ctwl = -0.5 * coef[1] / coef[0]
        ctwl = round(ctwl, 4)
        # plt.plot(x_final, y_fit, 'b.')
        # plt.plot([ctwl]*5, np.linspace(min(y_final),max(y_final),5),'g--')
        print('ctwl : ', ctwl)
    else:
        raise ValueError('Fail to fit.')

    print('notch: ', notch)
    print('wl: ', x)
    print('notch index: ', list(y).index(min(y_final)))
    wl = x[list(y).index(min(y_final))]
    l = list(x).index(wl - 1) if wl - 1 > x[0] else 0
    r = list(x).index(wl + 1) if wl + 1 < x[-1] else -1
    # print(l)
    # print(r)
    # print(i)
    peaks = list(y[l:r])
    # 找基准
    # 根据y差值，——间隔10个点，看差值

    index = peaks.index(notch)
    y_10_l = peaks[0:index]
    y_10_l.reverse()
    y_10_l = np.array(y_10_l)
    y_10_r = np.array(peaks[index:-1])
    step = len(y_10_l) // 6 if len(y_10_l) < len(y_10_r) else len(y_10_r) // 6

    # 窗口滑动求差分，依次滑动
    dy_10_l = abs(np.diff(y_10_l, step))
    dy_10_r = abs(np.diff(y_10_r, step))
    # print(step)
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
    print(ref_l)
    print(ref_r)
    # 得到透射深度
    t_depth = Decimal(abs((ref_l + ref_r) / 2 - notch)).quantize(Decimal("0.0000"), ROUND_HALF_UP)
    # 计算反射率、有效折射率
    # 计算透射深度，找差值
    print('透射深度: ', t_depth)
    # 并记下结果
    # 反射率单位为%， 要乘以100

    r = Decimal((1 - abs(math.pow(10, -t_depth / 10))) * 100).quantize(Decimal("0.00"), ROUND_HALF_UP)
    overlapFactor = 0.8
    print('r: ', r)
    # print(math.sqrt(r))
    a = Decimal(math.sqrt(r) if math.sqrt(r) < 0.99 else 0.99)
    print('a: ', a)
    n_ac = Decimal(math.atanh(a) * ctwl / (overlapFactor * math.pi * float(L) * 10 ** 6)).quantize(Decimal("0.0000000000000"), ROUND_HALF_UP)

    return fTime, ctwl, t_depth, r, n_ac



import pywt
from pywt import wavedec
def readT(tFile, L, illuminant):
    dfT = pd.read_csv(tFile, header=32)
    df = pd.read_csv(illuminant, header=30)
    x = dfT.iloc(1)[0].tolist()
    yT = np.array(dfT.iloc(1)[1])
    illuminantWl = np.array(df.iloc(1)[0])
    illuminantPeak = np.array(df.iloc(1)[1])
    f_time = os.path.getmtime(tFile)
    fTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(f_time))
    # tWl = [map(lambda x: x[0] - x[1], (data[1], srcPeak))]
    print(x[0])
    print(illuminantWl[0])
    # 波长对应，——根据第一个波长数值判断
    if x[0] == illuminantWl[0] and len(yT) == len(illuminantPeak):
        y = yT - illuminantPeak
    else:
        # 找到原透射光谱在光源透射谱中的对应的索引，并比对值，然后找到波长对应的一一相减
        s = np.where(illuminantWl==x[0])[0][0]
        e = np.where(illuminantWl==x[-1])[0][0]

        print(illuminantPeak[s:e])
        y = yT - illuminantPeak[s:e+1]
    # ************减去光源的光谱找到***********

    # 小波变换找到波谷
    # 转为ndarray格式
    peakData = list(y)

    print('min y: ', min(y))
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
    pre_ctwl = x[pre_i]
    print(pre_ctwl)
    print(pre_i)
    # 取以最小点为参考 两边对称的点
    # 在预中心波长左右各150个点的范围内，再找透射深度及中心波长
    startIndex = pre_i - 150 if pre_i - 150 > 0 else 0
    endIndex = pre_i + 150 if pre_i + 150 < len(x) else len(x)
    xFinal = x[startIndex:endIndex]
    yFinal = peakData[startIndex:endIndex]
    # 根据波谷值
    notch = min(yFinal)
    print('notch: ',notch)
    print('peaks len: ',len(yFinal))

    # 二次拟合
    coef = np.polyfit(xFinal, yFinal, 2)
    # y_fit = np.polyval(coef, xFinal)
    # 找出其中的峰值/对称点
    if coef[0] != 0:
        ctwl = -0.5 * coef[1] / coef[0]
        ctwl = round(ctwl, 4)
        # plt.plot(x_final, y_fit, 'b.')
        # plt.plot([ctwl]*5, np.linspace(min(y_final),max(y_final),5),'g--')
        print('ctwl : ', ctwl)
    else:
        raise ValueError('Fail to fit.')

    print('notch: ', notch)
    print('x length: ', len(xFinal))

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
    print(len(y_10_l))
    print(len(y_10_r))

    print(len(dy_10_l))
    print(len(dy_10_r))
    print(min(dy_10_l))
    print(min(dy_10_r))
    l_i = np.argwhere(dy_10_l == min(dy_10_l))[0][0]
    l_r = np.argwhere(dy_10_r == min(dy_10_r))[0][0]
    # print(l_i)
    # print(l_r)
    ref_l = y_10_l[l_i]
    ref_r = y_10_r[l_r]
    print(ref_l)
    print(ref_r)
    # 得到透射深度
    t_depth = Decimal(abs((ref_l + ref_r) / 2 - notch)).quantize(Decimal("0.0000"), ROUND_HALF_UP)
    # 计算反射率、有效折射率
    # 计算透射深度，找差值
    print('透射深度: ', t_depth)
    # 并记下结果
    # 反射率单位为%， 要乘以100

    r = Decimal((1 - abs(math.pow(10, -t_depth / 10))) * 100).quantize(Decimal("0.00"), ROUND_HALF_UP)
    overlapFactor = 0.8
    print('r: ', r)
    # print(math.sqrt(r))
    a = Decimal(math.sqrt(r) if math.sqrt(r) < 0.99 else 0.99)
    # print('a: ', a)
    n_ac = Decimal(math.atanh(a) * ctwl / (overlapFactor * math.pi * float(L) * 10 ** 6)).quantize(Decimal("0.0000000000000"), ROUND_HALF_UP)

    return fTime, ctwl, t_depth, r, n_ac

# 测试
# data = readT('../../DataSource/RFBG-PolyimideSMF28E/202207328-900-re11h/regenerationOSA-T/W2234.CSV', 12000, '../../DataSource/RFBG-PolyimideSMF28E/202207328-900-re11h/originalSpec.CSV')
# print(data)
