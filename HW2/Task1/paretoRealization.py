from Pareto import generate_Pareto


def getRealization():
    cnts = [5, 10, 100, 200, 400, 600, 800, 1000]

    theta = 8

    realizations = []

    for cnt in cnts:
        localRealization = []
        for _ in range(5):
            localRealization.append(generate_Pareto(cnt, theta))

        realizations.append(localRealization)

    return realizations
