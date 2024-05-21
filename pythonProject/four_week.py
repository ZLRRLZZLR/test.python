# s = 0
# count = 1
# while count <=966:
#     if count%2 == 0:
#         s -= count
#     else:
#         s += count
#     count += 1
# print(s)

# s = ""
# for i in range(100, 1000):
#     t = str(i)
#     if pow(eval(t[0]),3) + pow(eval(t[1]),3) + pow(eval(t[2]),3) == i :
#         s += "{},".format(i)
# print(s[:-1])

# count = 0
# while count < 3:
#     name = input()
#     password = input()
#     if name == 'Kate'and password == '666666':
#         print("登录成功！")
#         break
#     else:
#         count += 1
#         if count == 3:
#             print("3次用户名或者密码均有误！退出程序。")

# s = ""
# for i in range(1000, 10000):
#     t = str(i)
#     if pow(eval(t[0]),4) + pow(eval(t[1]),4) + pow(eval(t[2]),4) + pow(eval(t[3]),4) == i :
#         print(i)

#Prime
# def is_prime(n):
#     for i in range(2,n):
#         if n%i == 0:
#             return False
#     return True
# sum = 0
# for i in range(2,100):
#     if is_prime(i):
#         sum += i
# print(sum)
