# count = 0
# for i in range(10):
#     s1 = input()
#     s2 = eval(input())
#     if s1 =="Kate"and s2 == 666666:
#         print("登录成功！")
#         break
#     else:
#         count += 1
#         if count == 3:
#             print("3次用户名或者密码均有误！退出程序。")
#             break

count = 0
while count < 3:
    name = input()
    password = input()
    if name == 'Kate'and password == '666666':
        print("登录成功！")
        break
    else:
        count += 1
        if count == 3:
            print("3次用户名或者密码均有误！退出程序。")