# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 16:46:28 2022

@author: Administrator
"""

# 文件重命名 


import os 
def rename(dir1Name,dirName):
    
    # 文件夹对象化
    # 遍历指定目录下所有文件,显示所有文件名
    pathes1 = os.listdir(dir1Name)
    pathes2 = os.listdir(dirName)
    
    # 在文件夹下找到所有符合类型的文件名
    csvArr = []
    
    os.chdir(dirName)
    for i, path in enumerate(pathes2):
        # 文件按照时间顺序命名，文件名从大到小排列
        t=1
        if path.find('DT8')>-1:
            # 原文件名
            n1 = path
            # print(n1)
            # print(len(pathes1)/3)
            # # 新文件名
            # n2 = 'D'+str(len(pathes1)//3+t)+'.DT8' if len(pathes1)//3+t>1000 else 'D0'+str(len(pathes1)//3+t)+'.DT8'
            # print(n2)
            # # 调用改名函数，完成改名操作
            # # os.chdir(dirName)
            # os.rename(n1, n2)
        elif path.find('BMP')>-1:
            # 原文件名
            n1 = path
            # print(n1)
            # print(len(pathes1))
            # # 新文件名
            # n2 = 'G'+str(len(pathes1)//3+t)+'.BMP' if len(pathes1)//3+t>1000 else 'G0'+str(len(pathes1)//3+t)+'.BMP'
            # print(n2)
            # # 调用改名函数，完成改名操作
            # # os.chdir(dirName)
            # os.rename(n1, n2)
        else:
            n1 = path
            # print(n1)
            # print(len(pathes1))
            # # 新文件名
            # n2 = 'W'+str(t+len(pathes1)//3)+'.CSV' if t+len(pathes1)//3>1000 else 'W0'+str(t+len(pathes1)//3)+'.CSV'
            # print(n2)
            # # 调用改名函数，完成改名操作
            # os.rename(n1, n2)

        t=t+1
    # 获取修改时间
    file_time = os.path.getmtime('D0000.DT8')
    print(file_time)
    for i, path in enumerate(pathes2):
        if path.find('CSV') > 0:
            csvArr.append(path)
    print(len(csvArr))
    for i, path in enumerate(csvArr):
        if i>911:
            n1 = path
            # 新文件名
            n2 = 'W'+str(i+1006)+'.CSV'
            print(n2)
            # 调用改名函数，完成改名操作
            os.rename(n1, n2)
    # DT8文件按照时间顺序命名，使DT8文件名从大到小排列
    

# 测试
# rename("../../DataSource/RFBG-PolyimideSMF28E/20220730/regenerationOSA-R/r-1","../../DataSource/RFBG-PolyimideSMF28E/20220730/regenerationOSA-R")
