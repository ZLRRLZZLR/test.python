#数字形式转换 I
# diguit=['零','一','二','三','四','五','六','七','八','九',]
# S = input()
# for c in S:
#   print(diguit[eval(c)],end="")
#温度转换 II
# TempStr = input()
# if TempStr[0] in ['F']:
#     C = (eval(TempStr[1:]) - 32)/1.8
#     print("C{:.2f}".format(C))
# elif TempStr[0] in ['C']:
#     F = 1.8*eval(TempStr[1:]) + 32
#     print("F{:.2f}".format(F))
# else:
#     print
#货币转换 I
# Money = input()
# if Money[0] in ['R']:
#     USD = (eval(Money[3:])/6.78)
#     print("USD{:.2f}".format(USD))
# elif Money[0] in ['U']:
#     RMB = eval(Money[3:])*6.78
#     print("RMB{:.2f}".format(RMB))
# else:
#     print()
#Hello World的条件输出
# n = eval(input())
# if n == 0:
#     print("Hello World")
# elif n > 0:
#     print("He\nll\no \nWo\nrl\nd")
# else:
#     for c in "Hello World":
#         print(c)
#数值运算
s = input()
print("{:.2f}".format(eval(s)))
