#2021041075 이주현
from time import *
from datetime import *

#함수 선언
def countDays (start,cur) :
    retDays=0
    year,month,day=start.split('/')
    sDay=date(int(year),int(month),int(day))
    year,month,day=cur.split('/')
    cDay=date(int(year),int(month),int(day))
    diffDays=cDay-sDay
    retDays=diffDays.days #날짜만
    return retDays

def getDay (tm) :
    weeks=['월','화','수','목','금','토','일']
    return weeks[tm.tm_wday]

#전역 변수
startDate,curDate,tm='','',None

#메인 코드
if __name__ == "__main__" :
    startDate=input('시작 날짜(연/월/일) --> ')
    tm = localtime()
    curDate=str(tm.tm_year)+'/'+str(tm.tm_mon)+'/'+str(tm.tm_mday)

    print(startDate, "부터 오늘(", curDate,")까지는",countDays(startDate,curDate)," 일이 지났습니다")
    print("그리고 오늘은 ",getDay(tm),"요일 입니다")
