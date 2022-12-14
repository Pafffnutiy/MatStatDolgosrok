from HW2.binData import binomData
from scipy.stats import binom
import numpy as np
import matplotlib.pyplot as plt
from BaseFuncs import ecdf

cnts = [5, 10, 100, 200, 400, 600, 800, 1000]


def supp(s1):
    x = np.linspace(0, 72, 500)
    f1 = list(ecdf(s1, t) for t in x)
    f2 = list(binom.cdf(t, 71, 0.5) for t in x)
    s = 0
    for i in range(len(x)):
        s = max(s, abs(f1[i] - f2[i]))

    return s


def calcDn(n, series):
    return supp(binomData[cnts.index(n)][series])


def draw_table():
    data = np.zeros((5, 8))
    for j in range(5):
        for i, n in enumerate(cnts):
            data[j][i] = round(calcDn(n, j), 3)

    rows = ["Sample {0}".format(x) for x in range(5)]

    plt.table(rowLabels=rows, colLabels=cnts,
              cellText=data, loc="center")
    plt.axis("off")
    plt.show()


def draw_table1():
    data = np.zeros((5, 8))
    for j in range(5):
        for i, n in enumerate(cnts):
            data[j][i] = round(np.sqrt(n)*calcDn(n, j), 3)

    rows = ["Sample {0}".format(x) for x in range(5)]

    plt.table(rowLabels=rows, colLabels=cnts,
              cellText=data, loc="center")
    plt.axis("off")
    plt.show()


def draw_table2():
    data = np.zeros((5, 8), dtype=str)
    for j in range(5):
        for i, n in enumerate(cnts):
            data[j][i] = "+" if round(np.sqrt(n)*calcDn(n, j), 3) < 1.63 else "-"

    rows = ["Sample {0}".format(x) for x in range(5)]

    plt.table(rowLabels=rows, colLabels=cnts,
              cellText=data, loc="center")
    plt.axis("off")
    plt.show()



draw_table2()
