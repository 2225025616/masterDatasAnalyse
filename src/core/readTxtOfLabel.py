# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 15:41:00 2022

@author: Sunyali
"""

# 读取label存的txt文件数据
# 时间、中心波长、带宽，光谱信息


def readSpecInfo(fileName):
    time = []
    ctwl = []
    specInfo = []
    with open(fileName) as f:
        fDatas = f.readlines()
    f.close()
    fDatas = [i.strip('\n').split('\t') for i in fDatas]
    print('*********************')
    time = [i[0]+' '+i[1] for i in fDatas]
    # print(time[0])
    ctwl = [i[2] for i in fDatas]
    for data in fDatas:
        dt = [eval(i) for i in data[4:]]
        specInfo.append(dt)
    # for spec in specInfos:
    #     for i in spec:
    #         i = eval(i)
    # print('peak: ', min(specInfo))
    # print('txtfile name: ', time[0])
    # print('txtfile name: ', specInfo[0])
    # print('txtfile name: ', ctwl[0])
    # print('txtfile name: ', fwhm[0])
    return time, ctwl, specInfo



# 测试
data_r = readSpecInfo("../../DataSource/RFBG-PolyimideSMF28E/20220730/overHigh/1000-r.txt")
data_t = readSpecInfo("../../DataSource/RFBG-PolyimideSMF28E/20220730/overHigh/1000-t.txt")

# 利用
# print(data)
# datas['ctwl/nm'] = ctwlDatas
# datas['transmissionDepth/dBm'] = specInfo
# datas['time'] = timeData
# data_1000_r = transRegenerateDatas('../../DataSource/RFBG-PolyimideSMF28E/20220730/overHigh/1000-r.txt')
# data_1000_t = transRegenerateDatas('../../DataSource/RFBG-PolyimideSMF28E/20220730/overHigh/1000-t.txt')
# data_1000_t.to_csv(outputPath+"/overHighT.csv")
# data_1000_r.to_csv(outputPath+"/overHighR.csv")