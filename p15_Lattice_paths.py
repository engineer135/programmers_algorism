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
                #print("".join(tempStr))
                routeSet.add("".join(tempStr))

routeSet = set([])
str = list('r'*3 + 'd'*3)
#print(str)
mergeRoute(str, routeSet)
str2 = list(str[::-1]) # 문자열 뒤집어서 한번 더 돌린다.
#print(str2)
mergeRoute(str2, routeSet)

print(routeSet)
#for route in routeSet:
#    print(route)
print(len(routeSet)) #802 이럴수가... 틀린답이라고 한다.. 그럴리가 없는데....

