from matplotlib import pyplot as plt
import numpy as np
import statistics


def bin(n, p):
    # let s - current count of success
    s = 0

    for _ in range(n):
        xiUniform = np.random.uniform()

        if xiUniform < p:
            s += 1

    return s


def generate_binoms(cnt, n, p):
    result = []

    for _ in range(cnt):
        result.append(bin(n, p))

    return result


class Model():
    def __init__(self, n, p):
        self.data = []
        self.n = n
        self.p = p


def draw_plot():
    model = Model(71, 0.5)
    model.data = generate_binoms(cnt=20000, n=model.n, p=model.p)

    print("Real mean = " +
      str(round(statistics.mean(model.data), 2)) +
      "\tEstimate mean = " +
      str(round(model.n * model.p, 2))
      )
    print("Real variance = " +
      str(round(statistics.variance(model.data), 2)) +
      "\tEstimate variance = " +
      str(round(model.n * model.p * (1 - model.p), 2))
      )

    plot_data = dict(
        (i, model.data.count(i) / len(model.data)) for i in model.data
    )

    d = dict(sorted(plot_data.items(), key=lambda x: x[0]))

    print(d.keys())
    print(d.values())
    plt.scatter(d.keys(), d.values())
    plt.grid()
    plt.show()