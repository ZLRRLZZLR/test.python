import turtle as t
t.pensize(2)      #调整画笔大小
for i in range(4):     #四个部分
    t.seth(90*i)     #对应不同部分调整角度
    t.fd(150)       #前进150个像素
    t.right(90)     #向小海龟自己的右方转90度
    t.circle(-150,45)   #圆心在小海龟右边，半径为150，旋转45度角
    t.goto(0,0)          #画完一个部位，回到原点，进行下一次循环。
t.done()