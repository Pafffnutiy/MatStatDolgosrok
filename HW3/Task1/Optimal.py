from HW2.paretoData import paretoData
import matplotlib.pyplot as plt
import numpy as np
from math import log


def calcThetasPar():
    res = np.zeros((5, 8))

    for i in range(8):
        for j in range(5):
            logs = list(map(log, paretoData[i][j]))
            res[j][i] = round((len(logs)-1) / np.sum(logs), 3)

    return res


def draw_table():
    cnts = [5, 10, 100, 200, 400, 600, 800, 1000]

    data = calcThetasPar()
    rows = ["Sample {0}".format(x) for x in range(5)]

    plt.table(rowLabels=rows, colLabels=cnts,
              cellText=data, loc="center")
    plt.axis("off")
    plt.show()

draw_table()