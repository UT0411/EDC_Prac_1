import random
from datetime import datetime

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

