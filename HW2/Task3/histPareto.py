import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pareto
from HW2.paretoData import paretoData


def prepareAndGetDict(cnt):
    theta=8
    cnts = [5, 10, 100, 200, 400, 600, 800, 1000]
    x1 = np.linspace(1, 2, 50)
    d = dict()
    array = paretoData[cnts.index(cnt)][0]

    for elem in array:
        for i in range(len(x1) - 1):
            if x1[i] <= elem < x1[i + 1]:
                if (x1[i] + x1[i + 1]) / 2 in d.keys():
                    d[(x1[i] + x1[i + 1]) / 2] += 1
                else:
                    d[(x1[i] + x1[i + 1]) / 2] = 1

    d1 = dict(sorted(d.items(), key=lambda a: a[0]))
    d2 = dict()
    for elem in d1.items():
        d2[elem[0]] = elem[1]/max(d1.values())*theta

    return d2


def draw_hist():
    cnt = 1000
    theta = 8
    d = prepareAndGetDict(cnt)

    x = np.linspace(0.8, 2, 1000)
    y_true = list(pareto.pdf(t, theta) for t in x)

    plt.plot(x, y_true, color='r')
    plt.title("Realization with {0} elements".format(cnt))
    plt.bar(d.keys(), d.values(), width=0.05)
    plt.legend(["real", cnt])
    plt.show()


def draw_bw():
    theta = 8
    colors = ['b', 'g', 'r', 'c',
              'm', "teal", "darkviolet", "sienna"]

    # cnts1 = [5, 10]
    # cnts1 = [100, 200, 400, 600]
    cnts1 = [800, 1000]

    dicts = []

    for cnt in cnts1:
        dicts.append(prepareAndGetDict(cnt))

    for elem in dicts:
        plt.plot(elem.keys(), elem.values(),
                 color=colors[dicts.index(elem)]
                 )

    x = np.linspace(0.8, 2, 1000)
    y_true = list(pareto.pdf(t, theta) for t in x)

    plt.plot(x, y_true, color='black')
    plt.legend([*cnts1, "real"])
    plt.show()


draw_bw()
