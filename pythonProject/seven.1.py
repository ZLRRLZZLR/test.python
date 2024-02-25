f = open("latex.log")
s, c = 0, 0
for line in f:
    line = line.strip("\n")
    if line == "":
        continue
    s += len(line)
    c += 1
print(round(s/c))