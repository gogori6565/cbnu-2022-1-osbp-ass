#2021041075 이주현 
import turtle
import random
from tkinter.simpledialog import *
import math

#전역 변수th
swidth,sheight=500,500
inStr=''
tX,tY=[0]*2
radian,angle,radius=0,0,200

#메인 코드
if __name__ == "__main__" :
    turtle.title('거북이가 나선 모양의 글자쓰기')
    turtle.shape('turtle')
    turtle.setup(width=swidth+50,height=sheight+50)
    turtle.screensize(swidth,sheight)
    turtle.penup()
    
    inStr=askstring('문자열 입력','거북이가 쓸 문자열을 입력')
    angle=360*2/len(inStr)

    for ch in inStr :
        radian=3.14*angle/180
        tX=radius*math.cos(radian)
        tY=radius*math.sin(radian)
        
        r=random.random(); g=random.random(); b=random.random()
            
        turtle.goto(tX,tY)
        
        turtle.pencolor(r,g,b)
        turtle.write(ch,font=('',20))
        angle+=360*2/len(inStr)
        radius-=200/(len(inStr)-1)
        
    turtle.done()
