import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pareto
from HW2.paretoData import paretoData


def ecdf(realization, x):
    cnt = 0
    for elem in realization:
        if elem <= x:
            cnt += 1

    return cnt / len(realization)


def draw_plot():
    colors = ['b', 'g', 'r', 'c',
              'm', "teal", "darkviolet", "sienna"]
    cnts = [5, 10, 100, 200, 400, 600, 800, 1000]
    r_values = np.linspace(start=1, stop=3, num=100)

    for i in range(8):
        realiz = paretoData[i][4]
        y = [ecdf(realiz, elem) for elem in r_values]
        plt.step(r_values, y, color=colors[i])
        plt.xlim([1, 2])

    theta = 8
    dist = pareto.cdf(r_values, theta)
    plt.plot(r_values, dist, color="black")

    plt.xlabel("x")
    plt.ylabel(r'$\hat{F}(x)$')
    plt.legend([*cnts, "real"], loc='lower right')
    plt.title("The fifth realizations with different sizes")
    plt.show()
