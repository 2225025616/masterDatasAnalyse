# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 16:03:48 2022

@author: Sunyali
"""


import math
# 根据斜率，找基准
def calTInfo(data, L=12):
    # 找基准
    # 根据y差值，——间隔10个点，看差值
    # x = data[0]
    y = data[1]
    ctwl = data[2]
    notch = data[3]
    index = y.index(notch)
    print('xXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx')
    # print('notch: ',notch)
    y_10_l = y[0:index]
    y_10_r = y[index:-1]
    dy_10_l=[]
    dy_10_r=[]
    step = len(y)//6
    y_10_l.reverse()
    for i,yi in enumerate(y_10_l):
        if i*step+step<len(y_10_l):
            dy_10_l.append(y_10_l[i*step:i*step+step])
    for i,yi in enumerate(y_10_r):
        if i*step+step<len(y_10_r):
            dy_10_r.append(y_10_r[i*step:i*step+step])
    # dy_10_l.reverse()
    arg_dy_l = [abs(sum(d)/len(d)) for d in dy_10_l]
    arg_dy_r = [abs(sum(d)/len(d)) for d in dy_10_r]
    # print('l len: ',len(dy_10_l))
    # print('r len: ',len(dy_10_r))
    # print(min(dy_10_l))
    # print(min(dy_10_r))
    # print('arg 10 l: ',arg_dy_l)
    # print('arg 10 r: ',arg_dy_r)
    min_i_l = arg_dy_l.index(min(arg_dy_l))
    min_i_r = arg_dy_r.index(min(arg_dy_r))
    # print('min l: ',min_i_l)
    # print('min r: ',min_i_r)
    
    
    ref_l = float(format(sum(dy_10_l[min_i_l])/len(dy_10_l[min_i_l]), '.4f'))
    ref_r = float(format(sum(dy_10_r[min_i_r])/len(dy_10_r[min_i_r]), '.4f'))
    # print('ref_l: ',ref_l)    
    # print('ref_r : ',ref_r)  
    # print(type(ref_l))
    ref = float(format((ref_l+ref_r)/2, '.4f'))
    t_depth = float(format(ref-notch,'.4f'))
    # print('ref: ',ref)    
    # print(t_depth)  
    
    # 计算反射率、有效折射率
    # 计算透射深度，找差值
    # print('透射深度: ', t_depth)
    # 并记下结果
    # 反射率单位为%， 要乘以100
    r = float(format((1 - abs(math.pow(10, -t_depth/10)))*100,'.4f'))
    overlapFactor = 0.8
    # print('r: ', r)
    # print(math.sqrt(r))
    a = float(format((math.sqrt(r) if math.sqrt(r)<0.99 else 0.99),'.4f'))
    # print('a: ', a)
    # print(float(format(math.atanh(a),'.4f')))
    # print(float(format(math.atanh(a),'.4f'))*ctwl)
    n_ac = math.atanh(a)*ctwl/(overlapFactor*math.pi*float(L)*10**6)
    # n_dc = 1.456/(overlapFactor*ctwl)
    # print('反射率：', r)
    # print('平均折射率：',n_ac)
    return ctwl,t_depth,r,n_ac
    
    

# 测试 
# from readOsa import readDatas
# dt = readDatas('../../DataSource/RFBG-PolyimideSMF28E/20220711/regenerationOSA-T/W0003.CSV')
# from delBaseline import delbaseine
# data = delbaseine(dt)
# dd = calTInfo(data)
# print(dd)