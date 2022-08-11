# 把osa保存的DT8文件
#  找到中間的中心波長信息
#  保存到RFBG1T、RFBG1R命名的csv文件中
# 方便後期觀察實驗過程中，中心波長反射、透射的變化
from 再生实验透反射数据.proFiles.modulesDT8.readWl import readTWl, readRWl
from 再生实验透反射数据.proFiles.modulesDT8.repeatReadFiles import onlyOneType
from 再生实验透反射数据.proFiles.api.writeWlDataToCSV import writeCsv, writeWlCsv

# 循环读所有T DT8文件中的数据
def repeatReadDT8(filePath, fileType):
    csvPathes = onlyOneType(filePath, fileType)
    CsvWlDatas = []
    for path in csvPathes:
        # print(filePath + '\\' + path)
        # readTWl返回为元祖类型
        data = readTWl(filePath + '\\' + path)

        # print(list(data))

        # 转为数组类型后，在合并到一个数组中
        CsvWlDatas.append(list(data))
    # 返回所有透射深度&对应中心波长 的集合，以数组形式返回
    return CsvWlDatas

# 讀所有的透射文件
catalogueT = '..\..\RFBG1\RFBG20220117-T'
# 循环读所有DT8文件中的数据
# 循环读指定问价目录下的关键信息：wl&透射深度；返回数组
dataT = repeatReadDT8(catalogueT, 'DT8')
# 把数组写入到csv文件中并保存
writeCsv('RFBG1T-r', dataT)

# 循环读所有R DT8文件中的数据
def repeatReadDT8(filePath, fileType):
    csvPathes = onlyOneType(filePath, fileType)
    CsvWlDatas = []

    for path in csvPathes:
        data = readRWl(filePath + '\\' + path)
        # 转为数组类型后，在合并到一个数组中
        CsvWlDatas.append(list(data))
    # 返回所有透射深度&对应中心波长 的集合，以数组形式返回
    return CsvWlDatas

# 讀所有的反射文件
# catalogueR = '..\..\RFBG1\RFBG20220117-R-11'
# dataR = repeatReadDT8(catalogueR, 'DT8')
# writeWlCsv('RFBG1R', dataR)
