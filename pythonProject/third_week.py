# a = eval(input())
# print("{:-^20}".format(pow(a, 3)))

# n = eval(input())
# for i in range(1,n+1,2):
#     print("{0:^{1}}".format('*'*i, n))

# s = input()
# t = ""
# for c in s:
#     if 'a' <= c <= 'z':
#         t += chr( ord('a') + ((ord(c)-ord('a')) + 3 )%26 )
#     elif 'A' <= c <= 'Z':
#         t += chr( ord('A') + ((ord(c)-ord('A')) + 3 )%26 )
#     else:
#         t += c
# print(t)

# a = eval(input())
# print("{:+>30.3f}".format(pow(a, 0.5)))

s = input()
ls = s.split("-")
print("{}+{}".format(ls[0], ls[-1]))