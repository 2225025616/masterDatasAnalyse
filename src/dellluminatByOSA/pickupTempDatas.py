# utf-8
# 把解调仪存的数据放到一起
#  按照通道数、抽样频率拿到数据


import os
import pandas as pd
import numpy as np



# 根据需要拿到所有数据
    # dir——解调仪放数据的文件夹
    # passage—数组[]格式，存放通道数
    # frequency 抽样频率——观察数据存的频率，按照自己想要的在进行抽样
def concentrateTempDatas(dir, passageNum=(1,2,3), frequency=1):
    # 遍历指定目录下所有文件,显示所有文件名
    files = os.listdir(dir)
    passage = dict.fromkeys(passageNum)
    print(passage)
    # 在文件夹下找到所有符合类型的文件名
    for i, path in enumerate(files):
        # 文件按照时间顺序命名，文件名从大到小排列
        if path.find('Data-text') > -1:
            print(path)
            txt = pd.read_table(dir+'/'+path, sep='|', header=None)
            print(txt[0][0])
            print(txt[0][0].strip('\t').split('\t'))
            pass1 = [dd.strip('\t').split('\t')[0] for dd in txt[0]]
            print(pass1[0])
            print(type(passageNum[1]))
            print(passageNum[1])
            # print(txt[2][0])
            # print(txt[3][0])
            # print(txt[4][0])
            # print(txt[5][0])
            # print(txt[6][0])
            # print(txt[7][0])

        break




# 测试
concentrateTempDatas('../../DataSource/HS/H-S-1000/tempCheck')