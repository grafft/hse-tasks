import math
import numpy as np
import pandas as pd
from sklearn.metrics import roc_auc_score

df = pd.read_csv('data-logistic.csv', header=None)
l = df.shape[0]
X = df.iloc[:, [1, 2]]
y = df[0]


def gradient(C):
    w, wold = [0, 0], [0,0]
    steps = 0
    k = 0.1
    ld = 1
    while steps < 10000 and ld > 1e-5:
        sm1, sm2 = 0, 0
        for i, x in X.iterrows():
            ex = math.exp(-y[i] * (w[0] * x[1] + w[1] * x[2]))
            sm1 += y[i] * x[1] * (1 - 1 / (1 + ex))
            sm2 += y[i] * x[2] * (1 - 1 / (1 + ex))
        w[0] = wold[0] * (1 - k * C) + k * sm1 / l
        w[1] = wold[1] * (1 - k * C) + k * sm2 / l
        ld = ((w[0] - wold[0]) ** 2 + (w[1] - wold[1]) ** 2) ** 0.5/((w[0]**2+w[1]**2)**0.5*(wold[0]**2+wold[1]**2)**0.5)
        wold = w[:]
        steps += 1

    print(steps)
    return w


ws = gradient(0)
print(ws)
ys_scores = [1 / (1 + math.exp(-ws[1] * x[1] - ws[1] * x[2])) for _, x in X.iterrows()]
wr = gradient(10)
print(wr)
yr_scores = [1 / (1 + math.exp(-wr[1] * x[1] - wr[1] * x[2])) for _, x in X.iterrows()]

print('{0:.3f} {1:.3f}'.format(roc_auc_score(y, ys_scores), roc_auc_score(y, yr_scores)))
