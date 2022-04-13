#2021041075 이주현
from tkinter import *
from tkinter.filedialog import *

#함수 선언
def func_open():
    global filename
    filename=askopenfilename(parent=window,filetypes=(("GIF 파일","*.gif"),("모든 파일","*.*")))
    photo=PhotoImage(file=filename)
    pLabel.configure(image=photo)
    pLabel.image=photo

def func_exit():
    window.quit()
    window.destroy()

def zoom(event):
    global photo
    
    if event.keysym=="Up":
        photo=PhotoImage(file=filename)
        photo=photo.zoom(2,2)
        pLabel.configure(image=photo)
        pLabel.image = photo
    elif event.keysym=="Down":
        photo=PhotoImage(file=filename)
        photo=photo.subsample(2,2)
        pLabel.configure(image=photo)
        pLabel.image = photo
        

#전역 변수


#메인 코드
if __name__=="__main__":
    window=Tk()
    window.title("연습문제")
    window.geometry("500x500")

    photo=PhotoImage()
    pLabel=Label(window,image=photo)
    pLabel.pack(expand=1,anchor=CENTER)

    mainMenu=Menu(window)
    window.config(menu=mainMenu)
    fileMenu=Menu(mainMenu)
    mainMenu.add_cascade(label="파일",menu=fileMenu)
    fileMenu.add_command(label="파일 열기",command=func_open)
    fileMenu.add_separator()
    fileMenu.add_command(label="프로그램 종료",command=func_exit)

    window.bind("<Key>",zoom)
            
    window.mainloop()
