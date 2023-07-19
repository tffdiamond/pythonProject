import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("txt.csv")


def mean(points):
    total = 0
    n = len(points)

    for i in range(n):
        x = points.iloc[i].examscore

        total += x

    m = (total / n)

    return m


def median(points):
    x = sorted(points.examscore)

    if len(x) % 2 == 0:
        return (x.__getitem__(50) + x.__getitem__(51))/2
    else:
        return x[50]


def mode(points): # modify this code or prolly implement a better approach
    sortedArray = sorted(points.examscore)
    repetitionData= []
    index = 0
    for x in sortedArray:
        try:
            if repetitionData[index-1][0] == x:
                continue
        except:
            pass
        repetitionData.append([x, sortedArray.count(x)])
        index += 1

    # return max(repetitionData[1]) not true because it returns the second element in the row

print(mode(data))