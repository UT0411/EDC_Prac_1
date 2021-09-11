import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
from WH import WH_Random
from MB import MB_Random

def numgen(func):
    values = []
    for x in range(1000000):
        values.append(func())
    return values


def graph(func):
    values = numgen(func)
    mu, std = stats.norm.fit(values)

    print("Mean = " + str(mu))
    print("Standard Deviation = " + str(std))
    print("Variance  = " + str(std**2))

    x = np.linspace(min(values), max(values), 1000)
    pdf = stats.norm.pdf(x, mu, std)


    plt.plot(x, pdf, 'k')
    plt.hist(values, bins=300, density=True, alpha=0.5)
    plt.show() 

graph(WH_Random)
graph(MB_Random)