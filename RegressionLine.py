import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("sampleData.csv")
print(data)


def gradient_descent(m_now, b_now, points, L):
    m_gradient = 0
    b_gradient = 0

    n = len(points)

    for i in range(n):
        x = points.iloc[i].studytime
        y = points.iloc[i].examscore

        m_gradient += -(2 / n) * x * (y - (m_now * x + b_now))
        b_gradient += -(2 / n) * (y - (m_now * x + b_now))

    slope = m_now - m_gradient * L
    intercept = b_now - b_gradient * L

    return slope, intercept


m = 0
b = 0
L = 0.0001
epochs = 1000

for i in range(epochs):
    if i % 50 == 0:
        print(f"Epoch: {i}")
    m, b = gradient_descent(m, b, data, L)

print(f"Slope (m) of the regression line: {m}")
print(f"Intercept (b) of the regression line: {b}")

plt.scatter(data.studytime, data.examscore, color="black")
plt.plot(list(range(1, 10)), [m * x + b for x in range(1, 10)], color="red")
plt.show()
