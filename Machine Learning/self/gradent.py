import numpy as np
from matplotlib import pyplot as plt


def gradient_descent(x, y):
    m_curr = b_curr = 0
    iteration = 5
    n = len(x)
    learning_rate = 0.0501
    plt.scatter(x, y)
    for i in range(iteration):
        y_predict = m_curr * x + b_curr

        cost = sum([val ** 2 for val in (y - y_predict)]) / n
        m_derivative = (-2 / n) * sum(x * (y - y_predict))
        b_derivative = (-2 / n) * sum((y - y_predict))

        m_curr = m_curr - (learning_rate * m_derivative)
        b_curr = b_curr - (learning_rate * b_derivative)
        plt.plot(x, y_predict, color="green")
        print("m{} , b{} , cost{} , iteration{}".format(m_curr, b_curr, cost, i))


x = np.array([1, 2, 3, 4, 5])
y = np.array([5, 7, 9, 11, 13])
gradient_descent(x, y)
plt.show()
