import matplotlib.pyplot as plt
import numpy as np
from math import sqrt
from HW2.paretoData import paretoData
from HW2.Task2.paretoEmperical import ecdf


def supp(s1, s2):
    # m = max(len(s1), len(s2))
    # x = np.linspace(0, 1000, num=m)
    x = np.linspace(0, 1000, num=10000)
    f1 = list(ecdf(s1, t) for t in x)
    f2 = list(ecdf(s2, t) for t in x)
    s = 0
    for i in range(len(x)):
        s = max(s, abs(f1[i] - f2[i]))

    return s


def calcD(s1, s2):
    m = len(s1)
    n = len(s2)
    return sqrt(m * n / (m + n)) * supp(s1, s2)


def calcAllD():
    res = np.zeros((8, 8))
    for i in range(7):
        for j in range(i + 1, 8):
            realiz11 = paretoData[i][4]
            realiz22 = paretoData[j][4]

            res[i][j] = round(calcD(realiz11, realiz22), 3)
            res[j][i] = round(calcD(realiz11, realiz22), 3)

    return res


def draw_table():
    cnts = [5, 10, 100, 200, 400, 600, 800, 1000]

    a = calcAllD()

    plt.table(rowLabels=cnts, colLabels=cnts, cellText=a, loc="center")
    plt.axis("off")
    plt.show()


draw_table()
