from binomial import generate_binoms


def getRealization():
    cnts = [5, 10, 100, 200, 400, 600, 800, 1000]

    n = 71
    p = 0.5

    realizations = []

    for cnt in cnts:
        localRealization = []
        for _ in range(5):
            localRealization.append(generate_binoms(cnt, n, p))

        realizations.append(localRealization)

    return realizations
