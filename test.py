import numpy as np


def birthday_montecarlo(n, exper_num):
    counter = 0
    for _ in range(0, exper_num):
        values = np.random.randint(1, 366, size=n)
        if len(np.unique(values)) < n: counter += 1
    return counter / exper_num


print(birthday_montecarlo(20, 100000))
