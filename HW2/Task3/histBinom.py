import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom
from HW2.binData import binomData


def draw_hist():
    n = 71
    theta = 0.5
    array = binomData[7][0]

    x = np.arange(0, n, 1)
    y_true = list(binom.pmf(t, n, theta) for t in x)
    plt.title("Realization with {0} elements".format(len(array)))
    plt.hist(array, density=True)
    plt.scatter(x, y_true, color='r')
    plt.legend(["pdf", len(array)])
    plt.ylim(0, 0.15)
    plt.show()


def draw_bandwidth():
    n = 71
    theta = 0.5
    colors = ['b', 'g', 'r', 'c',
              'm', "teal", "darkviolet", "sienna"]
    cnts = [5, 10, 100, 200, 400, 600, 800, 1000]
    # cnts1 = [5, 10]
    # cnts1 = [100, 200, 400, 600]
    cnts1 = [800, 1000]
    x = np.arange(start=0, stop=71, step=1)
    y_true = list(binom.pmf(t, n, theta) for t in x)

    for i in range(len(cnts1)):
        array = binomData[cnts.index(cnts1[i])][0]

        d = dict()
        array.sort()
        for elem in array:
            d[elem] = array.count(elem)/len(array)

        plt.plot(d.keys(), d.values(), color=colors[i])

    plt.ylim(0, 0.15)
    plt.scatter(x, y_true, color="black")
    plt.legend([*cnts1, "real"])
    plt.show()

draw_bandwidth()