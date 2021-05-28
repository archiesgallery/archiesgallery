import numpy as np
a = np.array([23, 5, 70, 45, 86, 91, 11])
print(np.sort(a))
def sorting(x):
    for i in range(len(x)):
        swap = i + np.argmin(x[i:])
        (x[i], x[swap]) = (x[swap], x[i])
    return x
print(sorting(a))
