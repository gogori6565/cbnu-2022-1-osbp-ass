import turtle
import random

# 함수 선언

def screenRightClick(x,y) :
    global r,g,b
    r=random.random()
    g=random.random()
    b=random.random()

    turtle.pencolor((r,g,b))
    turtle.pendown()
    turtle.goto(x,y)

    tSize = random.randrange(1,10)
    turtle.shapesize(tSize)
    
    dgree=random.randrange(0,360)
    
    turtle.color(r,g,b)
    turtle.seth(dgree)
    turtle.stamp()    

# 변수 선언
r,g,b=0.0,0.0,0.0

# 메인 코드
if __name__ == "__main__" :
    turtle.title('거북이 도장 찍기')
    turtle.shape('turtle')
    turtle.onscreenclick(screenRightClick,3)

    turtle.done()

# 2021041075 이주현
