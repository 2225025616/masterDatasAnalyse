# 根据挑选出来的点，进行二次拟合，拟合出来中心波长


import numpy as np
def findCtwl(data):
    x = data[0]
    y = data[1]
    # 二次拟合
    coef = np.polyfit(x, y, 2)
    # y_fit = np.polyval(coef, x)

    # 找出其中的峰值/对称点
    if coef[0] != 0:
        ctwl = -0.5 * coef[1] / coef[0]
        ctwl = round(ctwl, 4)
        # plt.plot(x, y, 'b.')
        # plt.plot([ctwl]*5, np.linspace(min(y),max(y),5),'g--')
        print('ctwl : ', ctwl)
    else:
        ctwl = x[y.index(min(y))]

    return ctwl
