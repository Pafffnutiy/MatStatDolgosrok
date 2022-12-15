import numpy as np

def ecdf(realization, x):
    cnt = 0
    for elem in realization:
        if elem <= x:
            cnt += 1

    return cnt / len(realization)


def supp(s1, s2):
    # m = max(len(s1), len(s2))
    # x = np.linspace(0, 1000, num=m)
    x = np.linspace(0, 1000, num=100000)
    f1 = list(ecdf(s1, t) for t in x)
    f2 = list(ecdf(s2, t) for t in x)
    s = 0
    for i in range(len(x)):
        s = max(s, abs(f1[i] - f2[i]))

    return s