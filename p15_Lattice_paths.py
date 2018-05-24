'''
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20×20 grid?

아래 or 오른쪽으로만 갈 수 있다는 전제 조건이 있구나.

일단, 시작점에서 오른쪽으로만 출발해서 나오는 경우의 수를 곱한뒤 2를 곱하면 답이 나온다.
그리드 개수1 1*2 = 2
그리드 개수4 3*2 = 6
그리드 개수9 9*2 = 18
이런식으로... 이건 내가 직접 그려본거라서 정확하다.
의심의 여지가 없다. 레알 참트루.

right down 두방향만 가능
그리드 네개인 경우
2r 2d
1r 2d 1r
1r 1d 1r 1d

2d 2r
1d 2r 1d
1d 1r 1d 1r
이런식으로 표현이 가능.
이걸 함수로 만들면 답이 나올듯.

3r 3d

2r 3d 1r
2r 2d 1r 1d
2r 1d 1r 2d

1r 3d 2r
1r 2d 2r 1d
1r 2d 1r 1d 1r
1r 1d 2r 2d
1r 1d 1r 1d 1r 1d

9개가 나오고, 2를 곱하면 18개. 경로는 18개.
실제로 돌려봤더니, 20개가 나온다. 하나 빠트렸음 ㅋ

3r 3d   =           rrrddd
2r 3d 1r=           rrdddr
1r 3d 2r=           rdddrr
2r 2d 1r 1d=        rrddrd
2r 1d 1r 2d=        rrdrdd
1r 2d 2r 1d=        rddrrd
1r 2d 1r 1d 1r=     rddrdr
1r 1d 2r 2d=        rdrrdd
1r 1d 1r 1d 1r 1d=  rdrdrd

패턴을 찾았다..! 3일 걸렸다 -_-;;;;;;;;;;;

네개로 간소화해서 생각해보자
#rrdd
#drdr
#ddrr
rdrd
drrd
rddr 
6개...
근데 이걸 어떻게 구현하지.. -_-


와쿠이 요시유키라는 사람이 쓴 수학 사전을 봤다.
이런 case가 이미 있다.
공식이 있더라.
기본 바탕은 순열과 조합인데, 이걸 발전시켜서 중복된 글자 조합..의 경우의 수를 구하는 것이다.

기본 개념.
a,b,c 알파벳으로 두자리 문자를 만들때 경우의 수를 구하라 하면
3*3 = 9 
첫째자리 abc중 하나, 둘째자리 abc중 하나, 이 경우의 수들을 곱하면, 두자리일때 경우의 수가 나온다.

a,b,c,d,e 알파벳으로 두자리 문자를 만든다면
5*5 = 25
경우의 수가 많이 늘어났다.

그럼 한번 쓴 알파벳을 못 쓰도록 막는다면?
5*4 = 20 = (알파벳 개수) * (알파뱃 개수 - 1) 두자리만큼만 factorial 곱한다.

이제 2*2 그리드에 적용해보자.
a,b 알파벳으로 네자리 문자를 만들어야 한다.
2*2*2*2 = 16
하지만 제약 조건이 있다.
a,b 모두 두번까지만 사용이 가능하다는 것.
(a,b)(a,b) 이것과 같다.
앞에 두자리 경우의 수는 2*1 두자리만큼만 factorial 곱.
뒤에 두자리도 마찬가지 2*1 두자리만큼만 factorial 곱.
그리고 2*2=4 하면 총 네가지 경우의 수가 나온다.
하지만 답은 6이잖아?
4!/2!2! = 6인데,
여기서 4!은 어떻게 나오고, 왜 나누는지. 이 두가지를 설명할 수 있어야 한다.










a,b,c,d 알파벳을 카드라고 치자. 
이 카드를 조합해서 세글자를 만들 때, 
중복을 허용하고 나올 수 있는 모든 조합의 수를 살펴보면
첫째자리 abcd 모두 가능, 둘째자리 abcd 모두 가능, 셋째자리 abcd 모두 가능
4 * 4 * 4 = 64가지 경우의 수가 나온다.
첫째자리에 abcd중 하나, 둘째자리도 abcd중 하나, 셋째자리도 abcd중 하나가 올 수 있으므로.

그럼 중복이 안된다고 하면 카드는 a,b,c,d 네장이고,
첫째자리는 abcd, 넷중 하나이므로 4
둘째자리는 앞에서 선택한건 제외하면 둘중 하나이므로 3
셋째자리도 앞에서 선택한건 제외하면 2
4 * 3 * 2 = 24가지 경우의 수가 가능.
준비된 알파벳 카드의 팩토리얼만큼 경우의 수가 나온다.

그리드를 다시 살펴보자.
2*2 그리드의 경우 a,b 카드를 가지고 글자 네개를 만드는 것과 같다.
그런데 특이한건 중복이 허용되긴 하지만, 무한히 허용되지 않고, 최대 두번만 허용된다는 것이다.

이 얘기는
a,b | a,b
이렇게 두개로 쪼개서 봐야 한다.
a,b 카드를 둘로 나눠서 각각 두자리씩 만들어주는 것이다.
첫번째 두자리에 a과 b가 조합할 수 있는 경우의 수는 중복 불가능하므로 2*1 = 2
두번째 두자리에 a과 b가 조합할 수 있는 경우의 수는 중복 불가능하므로 2*1 = 2
이렇게 나온 두 경우의 수를 곱하면 2 * 2 = 4



식으로 하면 
n!/p!q!r!... 뭐 이런 식이다.
3*3의 그리드라고 치면 rrrddd 이 조합이고, n=6, p=3, q=3 이므로
6!/3!3! = 20
이게 답이다.

그럼 
20*20이면
n=40, p=20, q=20
40!/20!20! = ?

구하면 된다.

'''

def factorial(number):
    if number == 1:
        return 1
    else:
        return number * factorial(number-1)

#print(factorial(40)) #815915283247897734345611269596115894272000000000
#print(factorial(20)) #2432902008176640000
#print(2432902008176640000*2432902008176640000) #5919012181389927685417441689600000000

#print(815915283247897734345611269596115894272000000000/5919012181389927685417441689600000000) #137846528820.0

print(factorial(12))
'''

def mergeRoute(str, routeSet):
    routeSet.add("".join(str))
    for i in range(0, len(str)):
        #print(str[i])
        for j in range(i+1, len(str)):
            if(str[i] != str[j]):
                tempStr = list(str)
                temp = tempStr[j]
                tempStr[j] = tempStr[i]
                tempStr[i] = temp
                print("".join(tempStr))
                routeSet.add("".join(tempStr))

routeSet = set([])
str = list('r'*3 + 'd'*3)
#print(str)
mergeRoute(str, routeSet)
print("===========")
str2 = list(str[::-1]) # 문자열 뒤집어서 한번 더 돌린다.
#print(str2)
#mergeRoute(str2, routeSet)

#print(routeSet)
#for route in routeSet:
#    print(route)
print(len(routeSet)) #802 이럴수가... 틀린답이라고 한다.. 그럴리가 없는데....

'''