# -*- coding: utf-8 -*-
"""
Created on Sun Aug  23 15:35:12 2022

@author: sunyali
"""
# 减去光源曲线
# 得到透射深度
# 根据光谱在透射峰对应的索引位置，找适合拟合的数据段, 二次拟合出中心波长

import os
from decimal import Decimal, ROUND_HALF_UP
import math
import numpy as np
import time
from readT import readT


def findTR(TDir, originalSpec):
    # 在T文件下循环读取csv文件，和光源T波长一一对应减去光源光谱
    # 遍历指定目录下所有文件,显示所有文件名
    files = os.listdir(TDir)
    # print('dirName: ', files)

    # 在文件夹下找到所有符合类型的文件名
    notchDatas = []
    rDatas = []
    ctwlDatas = []
    timeDatas = []
    for i, path in enumerate(files):
        # 文件按照时间顺序命名，文件名从大到小排列
        if path.find('CSV') > 0:
            # print('****************')
            # print(path)
            # csvArr.append(TDir + '/' + path)
            dt = readT(TDir + '/' + path)
            # 波长一一对应，找打索引，对应减去光强
            # 由此，减到了波长的光源干扰，最大-最小=透射深度
            peaks = dt[1]
            wlDatas = list(dt[0])
            # print(wlDatas[-1])
            # print(list(originalSpec[0])[-1])
            # print(list(originalSpec[2])[-1])
            # 判断投射文件的波长范围和光源波长范围相同
            if list(originalSpec[0])[-1] == wlDatas[-1]:
                # print(wlDatas[-1])
                i = wlDatas.index(list(originalSpec[2])[0])
                originalT = list(originalSpec[1])
                peaks = list(peaks[i:-1])
                wlDatas = wlDatas[i:]
                # print(originalT[-1])
            elif len(originalSpec) > 2 or list(originalSpec[2])[-1] == wlDatas[-1]:
                # print(wlDatas[-1])
                i = wlDatas.index(list(originalSpec[2])[0])
                originalT = list(originalSpec[3])
                peaks = list(peaks[i:-1])
                wlDatas = wlDatas[i:]
                # print(originalT[-1])
            # 分别对应减去光源

            # print(wlDatas[-1])
            tData = [float((Decimal(peaks[i]) - Decimal(originalT[i])).quantize(Decimal("0.0000"), ROUND_HALF_UP)) for i in range(len(peaks))]
            print('tData: ', len(tData))
            notch = Decimal(max(tData)) - Decimal(min(tData)).quantize(Decimal("0.0000"), ROUND_HALF_UP)
            notchDatas.append(float(notch))
            # 找到透射点所在索引
            index = tData.index(min(tData))
            # 根据索引，找对应的中心波长，截取数据段
            sIndex = index-10 if index-10>0 else 0
            eIndex = index+10 if index+10<len(wlDatas) else len(wlDatas)
            x = wlDatas[sIndex:eIndex]
            y = tData[sIndex: eIndex]
            # 二次拟合
            coef = np.polyfit(x, y, 2)

            # 找出其中的峰值/对称点
            if coef[0] != 0:
                ctwl = Decimal(-0.5 * coef[1] / coef[0]).quantize(Decimal("0.0000"), ROUND_HALF_UP)
                ctwlDatas.append(ctwl)
                # plt.plot([ctwl]*5, np.linspace(min(y_final),max(y_final),5),'g--')
                # print('ctwl : ', ctwl)
            else:
                raise ValueError('Fail to fit.')
            r = Decimal((1 - Decimal(math.pow(10, -notch / 10)))) * 100
            # print(notch)
            rDatas.append(r.quantize(Decimal("0.0000"), ROUND_HALF_UP))
            f_time = os.path.getmtime(TDir + '/' + path)
            fTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(f_time))
            timeDatas.append(fTime)
    return timeDatas, ctwlDatas, notchDatas, rDatas


# 测试
# originalT = readCSV('../../DataSource/RFBG-PolyimideSMF28E/202207328-900-re11h/originalSpec-1.CSV')
# originalT+=(readCSV('../../DataSource/RFBG-PolyimideSMF28E/202207328-900-re11h/originalSpec-2.CSV'))
# regenerationSpec = findTR('../../DataSource/RFBG-PolyimideSMF28E/202207328-900-re11h/regenerationOSA-T', originalT)
