# def cmul(a, *b):
#     m = a
#     for i in b:
#         m *= i
#     return m
#
# print(eval("cmul({})".format(input())))

# def fbi(n):
#     if n == 1 or n == 2:
#         return 1
#     else:
#         return fbi(n-1) + fbi(n-2)
#
# n = eval(input())
# print(fbi(n))

# steps = 0
# def hanoi(src, des, mid, n):
#     global steps
#     if n == 1:
#         steps += 1
#         print("[STEP{:>4}] {}->{}".format(steps, src, des))
#     else:
#         hanoi(src, mid, des, n-1)
#         steps += 1
#         print("[STEP{:>4}] {}->{}".format(steps, src, des))
#         hanoi(mid, des, src, n-1)
# N = eval(input())
# hanoi("A", "C", "B", N)

# import random
#
# def genpwd(length):
#     a = 10**(length-1)
#     b = 10**length - 1
#     return "{}".format(random.randint(a, b))
#
# length = eval(input())
# random.seed(17)
# for i in range(3):
#     print(genpwd(length))

# def prime(m):
#     for i in range(2,m):
#         if m % i == 0:
#             return False
#     return True
#
# n = eval(input())
# n_ = int(n)
# n_ = n_+1 if n_ < n else n_
# count = 5
#
# while count > 0:
#     if prime(n_):
#         if count > 1:
#             print(n_, end=",")
#         else:
#             print(n_, end="")
#         count -= 1
#     n_ += 1