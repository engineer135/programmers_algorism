'''
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''
import time

print("start time {}".format(time.time()))

def getCollatz(number, chainCnt):
    chainCnt += 1
    #print(number)

    if number == 1 :
        #print("chainCnt", chainCnt)
        return chainCnt
    
    if number%2 == 0 :
        return getCollatz(number/2, chainCnt)
    else :
        return getCollatz(3*number+1, chainCnt)

answer = 0
maxCnt = 0
chainCnt = 0
i = 1
while i<1000000 :
    #print("i=",i)
    chainCnt = getCollatz(i, chainCnt)
    #print("chainCnt=",chainCnt)

    if chainCnt > maxCnt :
        maxCnt = chainCnt
        answer = i

    i += 1
    chainCnt = 0


print("answer",answer," max Chain Cnt", maxCnt)

print("end time {}".format(time.time()))


'''
start time 1526308216.4237812
answer 837799  max Chain Cnt 525
end time 1526308272.2705712

답은 나오지만 시간이 너무 오래 걸리네... 방법이 없을까 -_-;;
다른 사람들 답을 봐도 별로 시원찮은 것만 나오네.. 흠..
'''