# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 19:31:09 2022

@author: Administrator
"""

# 为了方便循环读取csv文件
# 在某一文件夹中，循环找某一文件类型的所有文件
# 返回为字符串，保存到list中
# 把文件夹名+文件名，保存在数组中，方便后续引用


import os

def repeatFiles(dirName, fileType):
    # 文件夹对象化
    # 遍历指定目录下所有文件,显示所有文件名
    pathes = os.listdir(dirName)

    # 在文件夹下找到所有符合类型的文件名
    csvArr = []
    for i, path in enumerate(pathes):
        # 文件按照时间顺序命名，文件名从大到小排列
        if path.find(fileType) > 0:
            csvArr.append(dirName + '/' +path)
    
    # 把文件夹名+文件名，保存在数组中，方便后续引用
    return csvArr
    