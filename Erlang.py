from scipy.stats import erlang
import matplotlib.pyplot as plt
import numpy as np


colors = ["red", "orange", "yellow", "green",
          "black", "blue", "violet"]
args = np.linspace(0, 4, 1000)

# y_true = erlang.cdf(args, 8, 0.125)
y_true = []

ks = [1, 2, 3, 5, 7, 9, 1]
rates = [2, 2, 2, 1, 0.5, 1, 1]
# scales = [1/x for x in rates]
pairs = []

for i in range(7):
    y_true.append(erlang.cdf(args, a=ks[i], scale=rates[i]))
    pairs.append((ks[i], rates[i]))

# for i, el in enumerate(y_true):
#     plt.plot(args, el, color=colors[i])

y = erlang.cdf(args, a=8, scale=0.125)
plt.plot(args, y, color="r")

# leg = [r"$k = {0}, \lambda = {1}$".format(k, rate) for (k, rate) in pairs]
leg = [r"$k = 8, \theta = 0.125$"]
plt.legend(leg, loc="lower right")
plt.show()
