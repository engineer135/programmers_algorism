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


와쿠이 요시유키라는 사람이 쓴 수학 사전을 빌려왔다.
101번 항목인 순열의 공식에 답이 있다.

기본 개념.
a,b,c 알파벳으로 두자리 문자를 만들때 경우의 수를 구하라 하면
3*3 = 9 
첫째자리 abc중 하나, 둘째자리 abc중 하나, 이 경우의 수들을 곱하면, 두자리일때 경우의 수가 나온다.

a,b,c,d,e 알파벳으로 두자리 문자를 만든다면
5*5 = 25
경우의 수가 많이 늘어났다.

그럼 한번 쓴 알파벳을 못 쓰도록 막는다면?
a,b,c,d,e가 각각 하나의 카드라고 가정하는 거지.
5*4 = 20
첫째자리는 다섯개중 다섯개 다 가능
둘째자리는 다섯개중 네개만 가능
이런식으로, 곱해나가면, 답이 나온다.
다섯자리를 만들어야한다면, 5!이 답이다.

그리고 이 문제의 경우 같은 종류를 포함하는 순열의 공식이라고 볼 수 있다.
카드가 모두 n장이 있는데, 그 가운데 a카드가 p장, b카드가 q장, c카드가 r장이라고 가정하면
이 카드 n장을 늘어놓아서 만들 수 있는 서로 다른 순열의 수는
n!/p!q!r!... (단 p+q+r...=n)
이 된다.

모든 카드 n장이 서로 구별이 가능하다면 위에서 본 것처럼 n!이 된다. << 이부분은 잘 이해가 안간다..

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
#이렇게 하면 모든 경우의 수가 다 나오지 않는다. 틀린 풀이이다.


아, gitHub에 올라간 파일이랑 로컬파일이랑 다를때는, 
git pull 하면 머지가 되는데
그 조건은 로컬에 있는 파일을 commit 까지 한 경우이다.
untracked, staged 이런 경우는 해당되지 않는다.
맨날 혼자서만 하다보니 몰랐다.. 브랜치도 좀 만들어보고 해야할듯. 익숙해지게.

'''