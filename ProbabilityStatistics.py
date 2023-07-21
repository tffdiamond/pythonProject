import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv("sampleData.csv")


def mean(data):
    amount = 0
    # Length of Data
    n = len(data)

    for i in range(n):
        x = data.iloc[i].examscore  # Take all data for student exam score

        amount += x

    m = (amount / n)

    return m


def median(data):
    # Sort the exam score data
    x = sorted(data.examscore)

    if len(x) % 2 == 0:
        return (x.__getitem__(50) + x.__getitem__(51)) / 2
    else:
        return x[50]


def mode(data):
    # Count the occurrences of each number
    num_count = {}
    for num in data:
        num_count[num] = num_count.get(num, 0) + 1

    # Find the maximum count
    max_count = max(num_count.values())

    # Find the mode(s)
    mode_values = []
    for num, count in num_count.items():
        if count == max_count:
            mode_values.append(num)

    return mode_values, max_count


average = mean(dataset)
middle = median(dataset)
frequency, total = mode(dataset.examscore)
print("Mean:", average)
print("Middle:", middle)
print("Mode:", frequency)
print("Number of occurrences:", total)
