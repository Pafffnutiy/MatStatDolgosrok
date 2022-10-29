from HW2.paretoData import paretoData
import matplotlib.pyplot as plt
import numpy as np


cnts = [5, 10, 100, 200, 400, 600, 800, 1000]


def calcSampleAverage():
    data = np.zeros((5, 8))

    for j in range(5):
        for i in range(len(cnts)):
            data[j][i] = round(sum(paretoData[i][j])/len(paretoData[i][j]), 3)

    return data


def calcSampleVar():
    newData = []
    for i in range(len(cnts)):
        arr1 = []
        for j in range(5):
            average = sum(paretoData[i][j])/len(paretoData[i][j])
            arr = []

            for k in range(cnts[i]):
                arr.append((paretoData[i][j][k]-average)**2)

            arr1.append(arr)

        newData.append(arr1)

    data = np.zeros((5, 8))

    for j in range(5):
        for i in range(len(cnts)):
            data[j][i] = round(sum(newData[i][j]) / len(newData[i][j]), 3)

    return data


def draw_table(data, title):
    rcolors = plt.cm.BuPu(np.full(5, 0.1))
    ccolors = plt.cm.BuPu(np.full(8, 0.1))

    plt.figure(figsize=(7, 7))
    plt.title(title)

    row_labels = []
    template = "Sample {0}"

    for i in range(5):
        row_labels.append(template.format(i))

    plt.table(rowLabels=row_labels, colLabels=cnts, cellText=data,
              loc="upper center",
              rowColours=rcolors, colColours=ccolors)
    plt.axis("off")
    plt.show()


def calcInaccuracy(theor, data):
    result = []
    for i in range(5):
        for j in range(8):
            percents = round((data[i][j] - theor) / theor * 100, 2)
            result.append(str(percents) + "%")

    result = np.reshape(result, (5, 8))

    return result


def draw_table_average():
    draw_table(calcSampleAverage(),
               title=r'Sample average $\overline{X}$')


def draw_table_var():
    draw_table(calcSampleVar(),
               title=r'Sample variance $\overline{S}^2$')


def draw_table_inaccuracy_average():
    draw_table(calcInaccuracy(1.14, calcSampleAverage()),
               title=r'Inaccuracy of sample average $\overline{X}$')


def draw_table_inaccuracy_var():
    draw_table(calcInaccuracy(0.027, calcSampleVar()),
               title=r'Inaccuracy of sample variance $\overline{S}^2$')

draw_table_var()
draw_table_inaccuracy_var()