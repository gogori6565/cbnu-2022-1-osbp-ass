#2021041075 이주현
from tkinter import *

#함수 선언
def photo_view():
    if var.get()==1:
        labelImage.configure(image=photo1)
    elif var.get()==2:
        labelImage.configure(image=photo2)
    else:
        labelImage.configure(image=photo3)
    
#전역 변수
var,labelImage=0,None
photo1,photo2,photo3=[None]*3

#메인 코드
if __name__=="__main__":
    window=Tk()
    window.geometry("400x400")
    window.title("애완동물 선택하기")
    
    var=IntVar()

    label1=Label(window,text="좋아하는 동물 투표",font=("궁서체",20),fg="blue")
    rb1=Radiobutton(window,text="강아지",variable=var,value=1)
    rb2=Radiobutton(window,text="고양이",variable=var,value=2)
    rb3=Radiobutton(window,text="토끼",variable=var,value=3)
    button1=Button(window,text="사진 보기",command=photo_view)

    photo1=PhotoImage(file="dog.gif")
    photo2=PhotoImage(file="cat.gif")
    photo3=PhotoImage(file="rabbit.gif")
    
    labelImage=Label(window,width=200,height=200,bg="yellow",image=None)

    label1.pack(padx=5,pady=5)
    rb1.pack(padx=5,pady=5)
    rb2.pack(padx=5,pady=5)
    rb3.pack(padx=5,pady=5)
    button1.pack(padx=5,pady=5)
    labelImage.pack(padx=5,pady=5)

    window.mainloop()
