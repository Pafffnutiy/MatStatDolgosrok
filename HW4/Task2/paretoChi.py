from HW2.paretoData import paretoData
import numpy as np
from scipy.stats import pareto
import matplotlib.pyplot as plt

cnts = [5, 10, 100, 200, 400, 600, 800, 1000]

def draw_table():
    chi = np.zeros((5, 8), dtype=str)

    chi[0][0] = '+'
    chi[0][1] = '+'
    chi[0][2] = '+'
    chi[0][3] = '+'
    chi[0][4] = '+'
    chi[0][5] = '+'
    chi[0][6] = '+'
    chi[0][7] = '+'
    chi[1][0] = '+'
    chi[1][1] = '+'
    chi[1][2] = '+'
    chi[1][3] = '+'
    chi[1][4] = '+'
    chi[1][5] = '-'
    chi[1][6] = '+'
    chi[1][7] = '+'
    chi[2][0] = '+'
    chi[2][1] = '+'
    chi[2][2] = '-'
    chi[2][3] = '+'
    chi[2][4] = '+'
    chi[2][5] = '+'
    chi[2][6] = '-'
    chi[2][7] = '+'
    chi[3][0] = '+'
    chi[3][1] = '+'
    chi[3][2] = '+'
    chi[3][3] = '+'
    chi[3][4] = '+'
    chi[3][5] = '+'
    chi[3][6] = '+'
    chi[3][7] = '+'
    chi[4][0] = '+'
    chi[4][1] = '-'
    chi[4][2] = '+'
    chi[4][3] = '+'
    chi[4][4] = '+'
    chi[4][5] = '+'
    chi[4][6] = '+'
    chi[4][7] = '+'

    rows = ["Sample {0}".format(x) for x in range(5)]

    plt.table(rowLabels=rows, colLabels=cnts,
              cellText=chi, loc="center")
    plt.axis("off")
    plt.show()

def draw_table1():
    chi = np.zeros((5, 8))

    chi[0][0] = 0.896
    chi[0][1] = 0.236
    chi[0][2] = 0.527
    chi[0][3] = 0.484
    chi[0][4] = 0.488
    chi[0][5] = 0.274
    chi[0][6] = 0.257
    chi[0][7] = 0.119
    chi[1][0] = 0.532
    chi[1][1] = 0.849
    chi[1][2] = 0.708
    chi[1][3] = 0.634
    chi[1][4] = 0.415
    chi[1][5] = 0.0962
    chi[1][6] = 0.111
    chi[1][7] = 0.734
    chi[2][0] = 0.145
    chi[2][1] = 0.849
    chi[2][2] = 0.0866
    chi[2][3] = 0.709
    chi[2][4] = 0.73
    chi[2][5] = 0.49
    chi[2][6] = 0.0419
    chi[2][7] = 0.978
    chi[3][0] = 0.145
    chi[3][1] = 0.236
    chi[3][2] = 0.17
    chi[3][3] = 0.779
    chi[3][4] = 0.994
    chi[3][5] = 0.842
    chi[3][6] = 0.962
    chi[3][7] = 0.229
    chi[4][0] = 0.284
    chi[4][1] = 0.0407
    chi[4][2] = 0.813
    chi[4][3] = 0.521
    chi[4][4] = 0.961
    chi[4][5] = 0.465
    chi[4][6] = 0.826
    chi[4][7] = 0.178

    rows = ["Sample {0}".format(x) for x in range(5)]

    plt.table(rowLabels=rows, colLabels=cnts,
              cellText=chi, loc="center")
    plt.axis("off")
    plt.show()