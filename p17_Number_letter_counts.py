'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. 
The use of "and" when writing out numbers is in compliance with British usage.

one
ten
one hundred
one thousand

'''

digit = ('','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen')
tenDigit = ('','','twenty','thirty','fourty','fifty','sixty','seventy','eighty','ninety')

letterCnt = 0

for i in range(1,1001):
    if i < 20:
        print(digit[i])
        #print(len(digit[i]))
        letterCnt += len(digit[i])
    elif i < 100:
        print(tenDigit[int(i/10)],'',digit[int(i%10)])
        #print(len(tenDigit[int(i/10)]) + len(digit[int(i%10)]))
        letterCnt += len(tenDigit[int(i/10)]) + len(digit[int(i%10)])
    elif i >= 1000:
        print('one thousand') # 11자리 더해준다.
        letterCnt += 11
    else:
        if i%100 < 20:
            print(digit[int(i/100)],'hundred and',digit[int(i%100)])
            #print(len(digit[int(i/100)]) + len(digit[int(i%100)]) + 10) #'hundred and' 글자 개수 10개 더 더해줘야함.
            letterCnt += len(digit[int(i/100)]) + len(digit[int(i%100)]) + 10
        else:
            print(digit[int(i/100)],'hundred and',tenDigit[int(str(i)[1:2])],'',digit[int(str(i)[2:])])
            #print(len(digit[int(i/100)]) + len(tenDigit[int(str(i)[1:2])]) + len(digit[int(str(i)[2:])]) + 10) #'hundred and' 글자 개수 10개 더 더해줘야함.
            letterCnt += len(digit[int(i/100)]) + len(tenDigit[int(str(i)[1:2])]) + len(digit[int(str(i)[2:])]) + 10

        if i%100 == 0:
            letterCnt -= 3
            #100으로 나누어 떨어지면 and가 필요 없으므로 -3

print(letterCnt) #21224
# 오잉 왜 답이 틀리다고 나오지...?