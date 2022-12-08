import matplotlib.pyplot as plt
from scipy.stats import binom
from HW2.binData import binomData
from BaseFuncs import ecdf


def draw_plot():
    colors = ['b', 'g', 'r', 'c',
              'm', "teal", "darkviolet", "sienna"]
    cnts = [5, 10, 100, 200, 400, 600, 800, 1000]
    n = 71
    r_values = list(range(n + 1))

    for i in range(8):
        realiz = binomData[i][4]
        y = [ecdf(realiz, t) for t in r_values]
        plt.step(r_values, y, color=colors[i])

    plt.xlim([20, 50])
    dist = [binom.cdf(r, 71, 0.5) for r in r_values]
    plt.scatter(r_values, dist, color="black")

    plt.xlabel("x")
    plt.ylabel(r'$\hat{F}(x)$')
    plt.legend([*cnts, "real"], loc='upper left')
    plt.title("The fifth realizations with different sizes")
    plt.show()

draw_plot()