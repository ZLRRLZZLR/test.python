def calculate_BMI(weight,height):
    BMI = weight /height **2
    if BMI <= 18.5:
        category = "偏瘦"
    elif BMI <= 25:
        category = "正常"
    elif BMI <= 30:
        category = "偏旁"
    else :
        category = "偏旁"
        print(f"您的BMI分类为{category}")
        return BMI
