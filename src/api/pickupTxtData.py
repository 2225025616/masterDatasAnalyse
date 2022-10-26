# -*- coding: utf-8 -*- coding

# 把txt文件集合成一个文件
import os

def repeatFiles(dirName, fileType):
    # 文件夹对象化
    # 遍历指定目录下所有文件,显示所有文件名
    files = os.listdir(dirName)
    print('dirName: ', files)
    # 在文件夹下找到所有符合类型的文件名
    csvArr = []
    for i, path in enumerate(files):
        # 文件按照时间顺序命名，文件名从大到小排列
        if path.find(fileType) > 0:
            # print('****************')
            # print(path)
            csvArr.append(dirName + '/' +path)



