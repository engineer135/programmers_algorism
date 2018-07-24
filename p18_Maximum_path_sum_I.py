'''
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. 
However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)

아 모든 경로를 다 더해본다음에 그중에 가장 큰 값을 찾는 거였구나.
문제 자체를 잘못 이해했네 멍청이처럼 -_-
이걸 어떻게 풀어야 스마트하게 풀었다고 할 수 있을까...
고민해보자...

'''

'''
index = 0
maxNum = 0
sum = 0
with open(".\p18_sample", "r") as f:
    lines = f.readlines()
    for line in lines:
        list = line.split()
        minIndex = index
        maxIndex = index if index+1 >= len(list) else index+1

        print("index==",index)
        print("minIndex==",minIndex)
        print("maxIndex==",maxIndex)

        maxNum = max([list[minIndex], list[maxIndex]])

        print(maxNum)

        if maxNum == list[minIndex]:
            index = minIndex
        elif maxNum == list[index]:
            index = index
        elif maxNum == list[maxIndex]:
            index = maxIndex

        sum += int(maxNum)
        #print("sum", sum)

print("final sum", sum)
'''

'''
두달만에 이 문제를 다시 잡아본다.
모든 수를 더하는 게 아닌 다른 방법이 있다는데.. 그게 뭘까..

일단 모든 수를 더하는 방법으로 풀어보자. 가장 간단하게.

0000 
0001
0010 0011 0012

경우의 수가 엄청 많은데 -_-...
굳이 다 더할 필요가 있을까.. 어차피 가장 큰 값만 찾으면 되는데 음...

으악... 결국 답을 찾아봤다 -_-;;;;;;
https://stackoverflow.com/questions/8002252/euler-project-18-approach
설명을 보니 역시나 간단하다.. 
밑에서부터 가장 큰 경우의 수를 찾아서 더해나가면 답이 나오는구나 허참..
알고리즘이란게 원래 그런거지만.. 남이 해놓은거 보면 참 간단하다 젠장
알고리즘을 알았으니 짜는거만이라도 직접 해보자 -_-

'''

from functools import reduce

def getMaxList(list):
    tempList = []
    index = 0

    for idx in range(index, len(list)-1):
        a = list[idx]
        b = list[idx+1]
        bigger = reduce(lambda a,b : a if a > b else b, [a,b])
        tempList.append(bigger)

    return tempList

def getSumList(orgList, targetList):
    tempList = []
    index = 0

    for idx in range(index, len(orgList)):
        #print(orgList[idx])
        #print(targetList[idx])
        tempList.append(int(orgList[idx]) + int(targetList[idx]))
    
    print(tempList)

    return tempList

index = 1
lineIndex = 0
sumList = []
with open(".\p18_sample", "r") as f:
    lines = f.readlines()
    lineIndex = len(lines) - 1

    #print(lines[lineIndex])
    #list = lines[lineIndex].split()
    #print(getMaxList(list))

    sumList = getSumList(getMaxList(lines[lineIndex].split()), lines[lineIndex-index].split())

    while(len(sumList) > 1):
        index += 1
        sumList = getSumList(getMaxList(sumList), lines[lineIndex-index].split())

'''
[125, 164, 102, 95, 112, 123, 165, 128, 166, 109, 122, 147, 100, 54]
[255, 235, 154, 150, 140, 179, 256, 209, 224, 172, 174, 176, 148]
[325, 246, 187, 178, 256, 329, 273, 302, 263, 242, 193, 233]
[378, 317, 231, 321, 354, 372, 393, 354, 360, 293, 247]
[419, 365, 393, 387, 419, 425, 430, 376, 454, 322]
[460, 434, 419, 475, 508, 470, 510, 524, 487]
[559, 499, 479, 536, 514, 526, 594, 616]
[647, 501, 613, 609, 533, 657, 683]
[666, 614, 636, 684, 660, 717]
[686, 640, 766, 731, 782]
[704, 801, 853, 792]
[818, 900, 935]
[995, 999]
[1074]

답이 나오는구나
분발하자.

'''

