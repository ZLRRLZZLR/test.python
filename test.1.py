N = input()
if eval(N)==0:
    print("Hello world")
elif eval(N)>0:
    print("He\nll\no \nWo\nrl\nd ")
else:
    print("H\ne\nl\nl\no\n \nW\no\nr\nl\nd")

n = eval(input())
if n == 0:
    print("Hello World")
elif n > 0:
    print("He\nll\no \nWo\nrl\nd")
else:
    for c in "Hello World":
        print(c)