#2021041075 이주현
import turtle
import random
import operator

#전역 변수
myturtle, tX, tY, tColor, tSize, tShape=[None]*6
playerTurtles=[] #2차원 리스트
shapeList=[]
result=[] #정렬된 2차원 리스트
swidth, sheight=500,500
r,g,b=0.0,0.0,0.0
#메인 코드
if __name__ == "__main__" :
    turtle.title('거북이 리스트 활용 (정렬)')
    turtle.setup(width=swidth+50,height=sheight+50)
    turtle.screensize(swidth,sheight)
    index=0

    for i in range(0,5):
        myturtle=turtle.Turtle('turtle')
        tX=random.randrange(-swidth/2, swidth/2)
        tY=random.randrange(-sheight/2,sheight/2)
        
        r=random.random()
        g=random.random()
        b=random.random()
        dgree=random.randrange(0,360)
        tSize=random.randrange(1,100)/10
        playerTurtles.append([myturtle,tX,tY,dgree,tSize,r,g,b])

    result=sorted(playerTurtles,key=operator.itemgetter(4))
    
    for tList in result:
        myturtle=tList[0]
        myturtle.color(tList[5],tList[6],tList[7])
        myturtle.seth(tList[3])
        myturtle.turtlesize(tList[4])
        myturtle.penup()
        if index==0:
            myturtle.goto(tList[1],tList[2])
            index+=1
            continue #블록 남은 부분 건너뛰기
        myturtle.goto(result[index-1][1],result[index-1][2]) #이전 거북이 위치
        myturtle.pendown()
        myturtle.goto(tList[1],tList[2]) #본인 거북이 위치
        index+=1
        
    turtle.done()

        
