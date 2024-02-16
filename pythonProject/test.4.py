import random

def genpwd(length):
    b = random.randint(10**(length-1),10**length-1)
    return b
length = eval(input())
random.seed(17)
for i in range(3):
    print(genpwd(length))