import numpy as np


def gradient_descent(x, y):
    m = b = 0
    iterations = 10
    n = len(x)
    learning_rate = 0.08
    for i in range(iterations):
        y_predicted = m * x + b

        md = -(2 / n) * sum(x * (y - y_predicted))
        bd = -(2 / n) * sum(y - y_predicted)
        m = m - learning_rate * md
        b = b - learning_rate * bd

        cost = (1 / n) * sum([val ** 2 for val in (y - y_predicted)])

        print("m {}, b {}, iteration {}, cost {}".format(m, b, i, cost))


x = np.array([1, 2, 3, 4, 5])
y = np.array([5, 7, 9, 11, 13])

gradient_descent(x, y)
