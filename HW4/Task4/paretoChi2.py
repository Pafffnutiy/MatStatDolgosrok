from HW2.paretoData import paretoData
import numpy as np
from scipy.stats import pareto
import math
import matplotlib.pyplot as plt

cnts = [5, 10, 100, 200, 400, 600, 800, 1000]

for i in range(8):
    for j in range(5):
        ser = paretoData[i][j]
        N = len(set(ser))
        n = 1 + math.floor(3.322*np.log10(N))
        intervals = np.linspace(1, 3, n)

        print(intervals)





def draw_table():
    chi = np.zeros((5, 8), dtype=str)

    rows = ["Sample {0}".format(x) for x in range(5)]

    plt.table(rowLabels=rows, colLabels=cnts,
              cellText=chi, loc="center")
    plt.axis("off")
    plt.show()