#2021041075 이주현
#전역 변수
st=""
newch, ch="",""
i=0

#메인 코드
if __name__ == "__main__" :
    st=input("문자열을 입력하세요 : ")

    for i in range(0,len(st)):
        if ord(st[i])>=ord('A') and ord(st[i])<=ord('Z') :
            ch=st[i].lower()
        elif ord(st[i])>=ord('a') and ord(st[i])<=ord('z') :
            ch=st[i].upper()
        else :
            ch=st[i]
            
        newch+=ch

    print("대소문자 변환 결과 --> ",newch)
