#2021041075이주현
import random

#함수 선언
def getnum (num) :
    numstr=''
    for i in range(0,len(num)) :
        if num[i].isdigit() :
            numstr+=num[i]
            
    return numstr

#전역 변수
numList=[]
min, tmp=0,0

#메인 코드
if __name__ == "__main__" :
    for i in range(0,10) :
        num = hex(random.randrange(0,100000))
        numList.append(num.replace('0x',''))
          
    print('정렬 전 데이터 : ', end='')
    [print(num, end=' ') for num in numList]

    for i in range(0,len(numList)-1) :
        min = i
        for j in range(i+1,len(numList)) :
            if int(getnum(numList[min]))>int(getnum(numList[j])) :
                min = j
        tmp = numList[i]
        numList[i]=numList[min]
        numList[min]=tmp

    print('\n정렬 후 데이터 : ', end='')
    [print(num, end=' ') for num in numList]
