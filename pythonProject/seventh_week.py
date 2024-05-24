# f = open("latex.log")
# s = 0
# for line in f:
#     line = line.strip('\n')
#     if len(line) == 0:
#         continue
#     s += 1
# print("共{}行".format(s))

# f = open("latex.log")
# cc = 0
# d = {}
# for i in range(26):
#     d[chr(ord('a')+i)] = 0
# for line in f:
#     for c in line:
#         d[c] = d.get(c, 0) + 1
#         cc += 1
# print("共{}字符".format(cc), end="")
# for i in range(26):
#     if d[chr(ord('a')+i)] != 0:
#         print(",{}:{}".format(chr(ord('a')+i), d[chr(ord('a')+i)]), end="")

# f = open("latex.log")
# ls = f.readlines()
# s = set(ls)
# for i in s:
#     ls.remove(i)
# t = set(ls)
# print("共{}独特行".format(len(s)-len(t)))

# f = open("data.csv")
# for line in f:
#     line = line.strip("\n")
#     ls = line.split(",")
#     ls = ls[::-1]
#     print(",".join(ls))
# f.close()

# f = open("data.csv")
# s = f.read()
# s = s.replace(" ","")
# print(s)
# f.close()

# f = open("latex.log")
# s, c = 0, 0
# for line in f:
#     line = line.strip("\n")
#     if line == "":
#         continue
#     s += len(line)
#     c += 1
# print(round(s/c))

# f = open("data.csv")
# ls = f.readlines()
# ls = ls[::-1]
# lt = []
# for item in ls:
#     item = item.strip("\n")
#     item = item.replace(" ", "")
#     lt = item.split(",")
#     lt = lt[::-1]
#     print(";".join(lt))
# f.close()