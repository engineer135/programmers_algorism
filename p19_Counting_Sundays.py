'''
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

일요일이 해당월의 첫번째 날이 되는 경우가 몇번이나 있는가 하는 문젠가보네?
30일 - 4 6 9 11
31일 - 1 3 5 7 8 10 12
28 or 29일 2

윤년은 29일.
그레고리력의 정확한 윤년 규칙은 다음과 같다.

서력 기원 연수가 4로 나누어떨어지는 해는 윤년으로 한다.(1988년, 1992년, 1996년, 2004년, 2008년, 2012년 …)
이 중에서 100으로 나누어떨어지는 해는 평년으로 한다.(1900년, 2100년, 2200년, 2300년, 2500년 …)
그중에 400으로 나누어떨어지는 해는 윤년으로 둔다.(1600년, 2000년, 2400년 …)

4로 나누어 떨어지지만 100으로 나누어 떨어지는 해는 평년으로 한다.
단, 400으로 나누어 떨어지는 해는 윤년으로 한다.
이 규칙에 의해 보통 4년에 한 번씩 하루가 추가된다. 
그리고 이 추가된 날은 날수가 가장 적은 2월에 추가된다. 이것이 바로 4년마다 2월 29일이 돌아오는 이유다.

월화수목금토일
0 1 2 3 4 5 6

1. 만약에 모든 달이 31일이라면? 간단하게 아래처럼 구현 가능

2. 여기에 31만 가변적으로 변하면 될거 같은데?
31, 28, 31, 30 ... 이런식으로...
monthEndDayArr = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
2월인 경우에만 연도 가지고 계산 필요...


'''
monthEndDayArr = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
dayOfWeekArr = ('월','화','수','목','금','토','일')
dayOfWeek = 0 #요일
day = 1 #일자
endDay = 0 #마지막날짜
month = 1 #월
year = 1900 #시작연도
endYear = 2001 #종료연도
firstSunday = 0 #일요일이 월의 첫날인 경우

while (True) :
    if year >= endYear:
        break

    #print("year=",year,"month=",month,"day=",day,"요일=",dayOfWeekArr[dayOfWeek])

    if (day == 1 and dayOfWeek == 6) :
        firstSunday += 1
        print("year=",year,"month=",month,"day=",day,"요일=",dayOfWeekArr[dayOfWeek])

    if(dayOfWeek >= 6):
        dayOfWeek = 0 #월요일로 리셋
    else:
        dayOfWeek += 1
        
    endDay = monthEndDayArr[month]

    # 2월인 경우 윤년 계산 필요
    if month == 2 and day >= 28:
        if year%400 == 0 :
            endDay += 1 # 400으로 나누어 떨어지면 무조건 윤년
        elif year%4 == 0 and year%100 != 0 :
            endDay += 1 # 4로 나누어 떨어지고 100으로는 나누어 떨어지지 않는 해는 윤년

    #if endDay == 29 :
    #    print("윤년입니다.")

    if day >= endDay:
        day = 1 #1일로 리셋. 다음달로 넘어간다.
        if(month >= 12):
            month = 1 #1월로 리셋
            year += 1 #다음연도로 넘어간다
        else:
            month += 1
    else:
        day += 1


print("firstSunday",firstSunday)
# 일요일이 월의 첫번째에 오는 경우 합계. 여기서 2를 빼야함. 왜냐면... 1900년에 두번이 있거든~~
# 그러면 답은 171


