from HW2.binData import binomData
from scipy.stats import chisquare
import numpy as np
import matplotlib.pyplot as plt

res = np.zeros((8, 8), dtype=str)
cnts = [5, 10, 100, 200, 400, 600, 800, 1000]

for i in range(7):
    for j in range(i + 1, 8):
        s1 = binomData[i][0]
        s2 = binomData[j][0]
        expec = chisquare(s1, s2)
        res[i][j] = '+' if expec[1] >= 0.1 else "-"
        res[j][i] = '+' if expec[1] >= 0.1 else "-"


def draw_table():
    plt.table(rowLabels=cnts, colLabels=cnts, cellText=res, loc="center")
    plt.axis("off")
    plt.show()


draw_table()