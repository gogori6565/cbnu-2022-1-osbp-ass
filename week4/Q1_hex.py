#2021041075이주현
import random

#전역 변수
numList=[]
min, tmp=0,0

#메인 코드
if __name__ == "__main__" :
    for i in range(0,10) :
        num = hex(random.randrange(0,100000))
        numList.append(num)

    print('정렬 전 데이터 : ', end='')
    [print(num, end=' ') for num in numList]

    for i in range(0,len(numList)-1) :
        min = i
        for j in range(i+1,len(numList)) :
            if int(numList[min],16)<int(numList[j],16) :
                min = j
        tmp = numList[i]
        numList[i]=numList[min]
        numList[min]=tmp

    print('\n정렬 후 데이터 : ', end='')
    [print(num, end=' ') for num in numList]
    

    
