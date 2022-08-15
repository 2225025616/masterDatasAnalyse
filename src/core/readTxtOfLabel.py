# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 15:41:00 2022

@author: Administrator
"""

# 读取label存的txt文件数据
# 时间、中心波长、带宽，光谱信息

def readOsaInfo(fileName):
    time = []
    ctwl = []
    fwhm = []
    specInfo = []
    with open(fileName) as f:
        fDatas = f.readlines()
    f.close()
    fDatas = [i.strip('\n').split('\t') for i in fDatas]
    print('*********************')
    # print(fDatas[0])
    time = [i[0]+' '+i[1] for i in fDatas]
    ctwl = [i[2] for i in fDatas]
    fwhm = [i[3] for i in fDatas]
    specInfo = [i[4:] for i in fDatas]
    # print('txtfile name: ', len(fDatas))
    # print('txtfile name: ', time[0])
    # print('txtfile name: ', specInfo[0])
    # print('txtfile name: ', ctwl[0])
    # print('txtfile name: ', fwhm[0])
    return time, ctwl, fwhm, specInfo
    


# 测试 
# data = readOsaInfo("../../DataSource/RFBG-PolyimideSMF28E/20220730/003.txt") 