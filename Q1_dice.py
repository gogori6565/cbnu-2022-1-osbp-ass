#2021041075 이주현
import random

#전역 변수 선언
a,b,c,d,e,f=[0]*6
count, con_count=0,0

#메인 코드 선언
if __name__ == "__main__" :

    while True :
        count+=1

        a=random.randrange(1,7)
        b=random.randrange(1,7)
        c=random.randrange(1,7)
        d=random.randrange(1,7)
        e=random.randrange(1,7)
        f=random.randrange(1,7)

        if a==b==c==d==e==f :
            print("6개 주사위가 모두 동일한 숫자가 나옴 -->",a,b,c,d,e,f)
            break

        elif (a==1 or b==1 or c==1 or d==1 or e==1 or f==1) and \
            (a==2 or b==2 or c==2 or d==2 or e==2 or f==2) and \
                (a==3 or b==3 or c==3 or d==3 or e==3 or f==3) and \
                    (a==4 or b==4 or c==4 or d==4 or e==4 or f==4) and \
                        (a==5 or b==5 or c==5 or d==5 or e==5 or f==5) and \
                            (a==6 or b==6 or c==6 or d==6 or e==6 or f==6) :
            con_count+=1

    print("6개가 동일한 숫자가 나올 때까지 주사위를 던진 횟수 -->",count)
    print("6개가 동일한 숫자가 나올 때까지, 1~6의 연속번호가 나온 횟수 -->", con_count)
