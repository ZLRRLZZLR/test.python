f = open("latex.log")
d = {}
num = 0
for i in range(26):
    d[chr(ord("a")+i)] = 0
for line in f:
    for i in line:
        d[i] = d.get(i,0)+1
        num += 1
print("共{}字符".format(num),end = "")
for i in range(26):
    if d[chr(ord("a")+i)] != 0:
        print(",{}:{}".format(chr(ord("a")+i),d[chr(ord("a")+i)]),end="")
