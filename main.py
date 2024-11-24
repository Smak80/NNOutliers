import numpy as np
from matplotlib import pyplot as plt


def generate_normal_data():
    return np.random.normal(scale=3, size=(300, 1))


def outliers(d: np.array):
    res = np.array(d)
    for k in range(np.size(d)):
        if np.random.randint(0, 100, 1) == 0:
            res[k] *= 25
    return res


def remove_outliers(d: np.array):
    ds = np.sort(d)
    sz = ds.size
    q1, q3 = np.quantile(d, [0.25, 0.75])
    irq = q3 - q1
    (mn, mx) =  (q1 - 1.5 * irq), (q3 + 1.5 * irq)
    return d[(d >= mn) & (d <= mx)]

data = generate_normal_data()
#data = outliers(data)

f1 = plt.figure(1)
pl1 = f1.add_subplot(2, 2, 1)
pl1.plot(range(1, len(data) + 1), data.T[0])

pl2 = f1.add_subplot(2, 2, 2)
pl2.hist(data, bins=30)

#data = remove_outliers(data)

# pl3 = f1.add_subplot(2, 2, 3)
# pl3.plot(range(1, data.size + 1), data)
#
# pl4 = f1.add_subplot(2, 2, 4)
# pl4.hist(data, bins=20)

plt.show()