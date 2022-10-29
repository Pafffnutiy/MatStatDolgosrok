from HW2.paretoData import paretoData
import numpy as np
from math import log
from math import sqrt
import matplotlib.pyplot as plt


def calcThetasPar():
    res = np.zeros((5, 8))

    for i in range(8):
        for j in range(5):
            logs = [log(x) for x in paretoData[i][j]]
            n = len(logs)
            rev = 1/sum(logs)
            coef = sqrt(n-2)*(n-1)/n
            res[j][i] = round(coef * rev, 3)

    return res


def draw_table():
    cnts = [5, 10, 100, 200, 400, 600, 800, 1000]

    data = calcThetasPar()
    rows = ["Sample {0}".format(x) for x in range(5)]

    plt.table(rowLabels=rows, colLabels=cnts,
              cellText=data, loc="center")
    plt.axis("off")
    plt.show()

# draw_table()

print(1000/sum([log(x) for x in paretoData[7][0]]))