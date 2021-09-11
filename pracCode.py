import random
from datetime import datetime
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np

random.seed(datetime.now())
s1 = random.randrange(1, 30000)
s2 = random.randrange(1, 30000)
s3 = random.randrange(1, 30000)

def WH_Random():
    global s1, s2, s3
    s1 = 171*s1 % 30269
    s2 = 172*s2 % 30307
    s3 =170*s3 % 30323

    r = (s1/30269.0 + s2/30307.0 + s3/30323.0) #% 1 #Add this 1 before using
    return r

values = []
for x in range(1000000):
    values.append(WH_Random())

mu, std = stats.norm.fit(values)

print("Mean = " + str(mu))
print("Standard Deviation = " + str(std))
print("Variance  = " + str(std**2))

x = np.linspace(min(values), max(values), 1000)
pdf = stats.norm.pdf(x, mu, std)


plt.plot(x, pdf, 'k')
plt.hist(values, bins=300, density=True, alpha=0.5)
plt.show() 

print()