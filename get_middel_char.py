def string_middle(str):
    # 함수를 완성하세요
    # length = len(str)
    # if length%2 == 0 :
    #     middle = str[length//2-1:(length//2)+1]
    # else :
    #     middle = str[length//2:(length//2)+1]

    # return middle



    # 헐 이렇게 간단히 되네 -_-
    return str[(len(str)-1)//2:len(str)//2+1]

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(string_middle("power"))