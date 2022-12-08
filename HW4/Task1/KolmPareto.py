from HW2.paretoData import paretoData
from Pareto import cdf
import numpy as np

variationSeries = sorted(paretoData)


def calcDnPlus(n):
    # For supporting arr indexing make substitute t=k-1
    arr = np.zeros(n, dtype=float)
    for t in range(n):
        arr[t] = (t+1)/n - cdf(variationSeries[t+1])

    return max(arr)


def calcDnMinus(n):
    # For supporting arr indexing make substitute t=k-1
    arr = np.zeros(n, dtype=float)
    for t in range(n):
        arr[t] = cdf(variationSeries[t + 1]) - t / n

    return max(arr)


def calcDn(n):
    return max(calcDnPlus(n), calcDnPlus(n))
