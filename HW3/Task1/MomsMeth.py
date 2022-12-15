from HW2.binData import binomData
from HW2.paretoData import paretoData
import matplotlib.pyplot as plt
import numpy as np
from Distributions import Distributions


def calcThetasBin():
    res = np.zeros((5, 8))
    n = 71

    for i in range(8):
        for j in range(5):
            average = np.average(binomData[i][j])
            res[j][i] = round(1/n * average, 3)

    return res


def calcThetasPar():
    res = np.zeros((5, 8))

    for i in range(8):
        for j in range(5):
            average = np.average(paretoData[i][j])
            res[j][i] = round(1 + 1 / (average - 1), 3)

    return res


def calcThetas(arg: Distributions):
    if arg == Distributions.BINOMIAL:
        return calcThetasBin()
    elif arg == Distributions.PARETO:
        return calcThetasPar()


def draw_table():
    cnts = [5, 10, 100, 200, 400, 600, 800, 1000]

    data = calcThetas(Distributions.BINOMIAL)
    rows = ["Sample {0}".format(x) for x in range(5)]

    plt.table(rowLabels=rows, colLabels=cnts,
              cellText=data, loc="center")
    plt.axis("off")
    plt.show()
