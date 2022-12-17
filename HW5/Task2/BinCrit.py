import numpy as np
from scipy.stats import binom
from HW2.binData import binomData
import pandas as pd

cnts = [5, 10, 100, 200, 400, 600, 800, 1000]

series = np.array(binomData)[:, 0]

theta0 = 0.5
theta1 = 0.53
theta = 0

c = [binom.ppf(0.99, 71*i, theta0) for i in cnts]
sums = np.zeros(8)
data = ["Accept {0}" for i in range(8)]


def draw_table():
    for i in range(8):
        sums[i] = sum(series[i])
        theta = theta0 if sums[i] < c[i] else theta1

        data[i] = data[i].format(theta)

    cols = ['z', 'c_alpha', 'Output', 'cnts']

    df = pd.DataFrame({cols[3]: cnts,
                       cols[0]: sums, cols[1]: c,
                       cols[2]: data})

    df = df.set_index('cnts')

    return df


def draw_table1():
    data = [binom.cdf(c[i], 71*cnts[i], theta1) for i in range(8)]
    cols = ['c_alpha', 'beta', 'cnts']

    df = pd.DataFrame({cols[2]: cnts, cols[0]: c, cols[1]: data})

    df = df.set_index('cnts')

    return df

print(draw_table1())