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
def concentrateTempDatas(dir, passageNum=(0,1,2), frequency=6):
    # 遍历指定目录下所有文件,显示所有文件名
    files = os.listdir(dir)
    passage = dict.fromkeys(passageNum)
    # 在文件夹下找到所有符合类型的文件名
    for i, path in enumerate(files):
        # 文件按照时间顺序命名，文件名从大到小排列
        if path.find('Data') > -1:
            print(path)
            txt = pd.read_table(dir+'/'+path, sep='|', header=None)
            # print(txt[0][0])
            # print(txt[0][0].strip('\t').split('\t'))
            pass0 = [dd.strip('\t').split('\t')[0] for dd in txt[0]]
            pass1 = [dd.strip('\t').split('\t')[1] for dd in txt[0]]
            passage[passageNum[0]] = pass0
            if passageNum[1] == 1:
                passage[passageNum[1]] = pass1
            else:
                passage[passageNum[1]] = txt[passageNum[1]]
            for i in range(len(passageNum)):
                if i>1:
                    passage[passageNum[i]] = txt[i-1]

            # print(passage[passageNum[-1]][0])
            # print(passageNum[-1])
            # print(txt[2][0])

            ## print(len(passage[0]))
            ## print('****抽样*****')
            # 抽样
            # 在字典里，根据频率抽样数据
            for i in range(len(passageNum)):
                sig = np.array(passage[passageNum[i]])
                n = sig.size
                sig_sample = np.zeros(int(n/frequency))
                sig_sample = sig[np.arange(0, n, frequency)]
                passage[passageNum[i]] = list(sig_sample)

            ## print(len(passage[0]))
            ## print(len(passage[1]))
            ## print(len(passage[2]))





# 测试
# concentrateTempDatas('../../DataSource/HS/H-S-1000/tempCheck')