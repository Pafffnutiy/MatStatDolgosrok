from HW2.Task2.calcDPareto import calcAllD
import numpy as np
import matplotlib.pyplot as plt

data = calcAllD(0)
res = np.zeros((8, 8), dtype=str)
cnts = [5, 10, 100, 200, 400, 600, 800, 1000]

for i in range(7):
    for j in range(i + 1, 8):
        D = data[i][j]
        m = cnts[j]
        tnm = 1.22
        res[i][j] = '+' if D <= tnm else '-'
        res[j][i] = '+' if D <= tnm else '-'


def draw_table():
    plt.table(rowLabels=cnts, colLabels=cnts, cellText=res, loc="center")
    plt.axis("off")
    plt.show()


draw_table()
