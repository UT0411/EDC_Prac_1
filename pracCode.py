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

def g3(x):
    if(abs(x)< 1):
        return 17.49731196*np.exp(-0.5*x**2) - 4.73570326*(3 - x**2) - 2.15787544*(1.5 - abs(x))
    elif (abs(x)< 1.5):
        return 17.49731196*np.exp(-0.5*x**2) - 2.36785163*((3 - x)**2) - 2.15787544*(1.5 - abs(x))
    elif (abs(x)< 3):
        return 17.49731196*np.exp(-0.5*x**2) - 2.36785163*((3 - x)**2)
    else:
        return 0 


def MB_Random():
    prob = random.random()
    u1 = random.random()
    u2 = random.random()
    u3 = random.random()
    if prob < 0.8638:
        x = 2*(u1+u2+u3-1.5)
    elif prob < 0.8638 + .1107:
        x = 1.5*(u1+u2-1)
    elif prob < 0.8638 + .1107 + .0228002039: 
        x = 6*u1 -3
        y = 0.358*u2
        while (y>g3(x)):
            u1 = random.random()
            u2 = random.random()
            x = 6*u1 -3
            y = 0.358*u2
    else:
        x =0 
        y= 0
        while x < 3 and y <3:
            v1 = random.uniform(-1, 1) 
            v2 = random.uniform(-1, 1) 
            w =  - np.log(v1**2+v2**2)
            val = np.power(((9+2*w)/(v1**2+v2**2)), 0.5)
            x = v1*val
            y = v2*val
        if(x<3 and y > 3):
            x = y
    return x
            

values = []
for x in range(1000000):
    values.append(MB_Random())

mu, std = stats.norm.fit(values)

print("Mean = " + str(mu))
print("Standard Deviation = " + str(std))
print("Variance  = " + str(std**2))

x = np.linspace(min(values), max(values), 1000)
pdf = stats.norm.pdf(x, mu, std)


plt.plot(x, pdf, 'k')
plt.hist(values, bins=300, density=True, alpha=0.5)
plt.show() 