# 문자를 받아서 중간 글자를 반환하는 함수
# 문자 길이가 홀수면 하나, 짝수면 두개 반환합니다.
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