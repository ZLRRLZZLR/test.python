a = 0
for i in range(2,100,):
    flag = 0
    for j in range(2,i//2+1):
        if i % j == 0:
            flag = 1
            break
    if flag == 0:
        a += i
print(a)