#변수 선언
a=''

#메인 코드
if __name__ == "__main__" :
    a=input('문자열을 입력 --> ')

    for i in range(len(a)-1, -1, -1) :
        print('%c' % a[i], end = '')

# 2021041075 이주현
