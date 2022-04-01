#2021041075 이주현

#함수 선언

def base2(num):
    if num>0 :
        base2(num//2)
        print(num%2,end=" ")

def base8(num):
    if num>0:
        base8(num//8)
        print(num%8,end=" ")
    
def base16(num):
    if num>0:
        base16(num//16)
        renum=num%16
        if(renum<10):
            print(renum,end=" ")
        else:
            if renum==10: print('A',end=" ")
            elif renum==11: print('B',end=" ")
            elif renum==12: print('C',end=" ")
            elif renum==13: print('D',end=" ")
            elif renum==14: print('E',end=" ")
            elif renum==15: print('F',end=" ")

#전역 변수

#메인 코드
if __name__ == "__main__" :
    num=input("10진수 입력 --> "); print("\n")

    print("2진수 : ",end=""); base2(int(num)); print('\n')
    print("8진수 : ",end=""); base8(int(num)); print('\n')
    print("16진수 : ",end=""); base16(int(num))
