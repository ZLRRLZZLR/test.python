count = 0
def prime(m):
        for i in range(2,m):
            if m % i == 0:
                return False
        return True
n = int(eval(input()))
p = int(n)
p = p+1 if p <n else n

while count < 5:
    if prime(p):
        if count < 4:
            print(p, end =",")
        else:
            print(p, end ="")
        count += 1
    p += 1



