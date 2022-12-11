import numpy as np
import matplotlib.pyplot as plt
import statistics

samples = np.linspace(start=0, stop=5, num=250)


def gen_uniforms(n):
    uniforms = []

    for _ in range(n):
        thetaUniform = np.random.uniform()

        uniforms.append(thetaUniform)

    return uniforms


def pareto(x, theta):
    return x ** (-1 / theta)


def uniformsToParetoByElements(localUniforms, theta):
    arr = list(map(pareto, localUniforms, [theta] * len(localUniforms)))
    res = []
    for elem in arr:
        res.append(round(elem, 5))
    return res


def generate_Pareto(cnt, theta):
    return uniformsToParetoByElements(gen_uniforms(cnt), theta)


def cdf(x, theta=8):
    if x >= 1:
        return 1 - x**(-theta)

    return 0


class Model:
    def __init__(self, theta):
        self.data = []
        self.theta = theta


def draw_plot():
    model = Model(8)
    model.data = generate_Pareto(10000, model.theta)

    d = dict()

    for elem in model.data:
        for i in range(len(samples) - 1):
            srednee = (samples[i] + samples[i + 1]) / 2
            if samples[i] <= elem < samples[i + 1]:
                if srednee in d.keys():
                    d[srednee] += 1
                else:
                    d[srednee] = 1
            elif samples[i + 1] < 1:
                d[srednee] = 0

    d = dict(sorted(d.items(), key=lambda x: x[0]))

    print("Real mean = " +
          str(round(statistics.mean(model.data), 2)) +
          "\tEstimate mean = " +
          str(round(model.theta / (model.theta - 1), 2))
          )

    print("Real variance = " +
          str(round(statistics.variance(model.data), 2))
          + "\tEstimate variance = " +
          str(round(model.theta / (
                  (model.theta - 2) * (model.theta - 1) ** 2
          ), 2))
          )

    plt.plot(d.keys(), d.values())
    plt.grid()
    plt.xlim(0.5, 2.2)
    plt.show()