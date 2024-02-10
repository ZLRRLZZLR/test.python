score = eval(input("请输入您的分数:"))
if 60 <= score < 70:
    grade = "D"
elif 70 <= score < 80:
    grade = "C"
elif 80 <= score < 90:
    grade = "B"
elif 90 <= score <= 100:
    grade = "A"
print("你的成绩等第为{}".format(grade))
