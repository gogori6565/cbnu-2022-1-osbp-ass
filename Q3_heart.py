#2021041075 이주현

#전역 변수
num, heartnum,heart ="","",""
i=0

#메인 코드
if __name__ == "__main__" :
    num=input("숫자를 여러 개 입력하세요 : ")
    print("")

    i=0
    
    while True :

        heartnum=num[i]
        
        for _ in range(0,int(heartnum),1) :
            heart+="\u2665"

        print(heart)
        heart=""

        i+=1

        if(i>len(num)-1) :
            break
    
