Tempstr = input()
if Tempstr[0] in {"F"}:
    C=((eval(Tempstr[1:]))-32)/1.8
    print('C{:.2f}'.format(C))
elif Tempstr[0] in {"C"}:
    F=((eval(Tempstr[1:]))*1.8)+32
    print('F{:.2f}'.format(F))
else:
    print("输入格式错误")
