M = input()
N = input()
op = input()
if op=="+":
    print(eval(M)+eval(N))
elif op=="-":
    print(eval(M)+eval(N))
elif op=="*":
    print(eval(M)*eval(N))
else:
    print(eval(M)/eval(N))

s = input()
print("{:.2f}".format(eval(s)))