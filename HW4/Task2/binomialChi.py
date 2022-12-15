from HW2.binData import binomData
import numpy as np
from scipy.stats import binom
import matplotlib.pyplot as plt

cnts = [5, 10, 100, 200, 400, 600, 800, 1000]

def calcChiN(n, series, N=72):
    summa = 0
    for i in range(1, N):
        cnt = 0
        for j in range(1, n+1):
            cnt += (binomData[cnts.index(n)][series][j-1] == i)
        pi = binom.pmf(i, 71, 0.5)
        summa += (cnt-n*pi)**2/(n*pi)
    return summa


def draw_table():
    chi = np.zeros((5, 8))

    for j in range(5):
        for i, n in enumerate(cnts):
            chi[j][i] = round(calcChiN(n, j), 3)

    rows = ["Sample {0}".format(x) for x in range(5)]

    plt.table(rowLabels=rows, colLabels=cnts,
              cellText=chi, loc="center")
    plt.axis("off")
    plt.show()

def draw_table1():
    chi = np.zeros((5, 8), dtype=str)

    for j in range(5):
        for i, n in enumerate(cnts):
            chi[j][i] = "+" if round(calcChiN(n, j), 3) <= 85.5 else '-'

    rows = ["Sample {0}".format(x) for x in range(5)]

    plt.table(rowLabels=rows, colLabels=cnts,
              cellText=chi, loc="center")
    plt.axis("off")
    plt.show()