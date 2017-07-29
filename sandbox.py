import numpy as np
a = list(np.random.uniform(0,1, 100))
b = []

def func(x):
    return x**30

for k in range(len(a)):
    for i in range(len(a)):
        for j in range(len(a)):
            b.append(func(a[i]) > func(a[j]) or func(a[i]) + a[j] > func(sum(a)))
        print(b)