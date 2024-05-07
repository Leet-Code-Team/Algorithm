def solution(absolutes, signs):
    answer = 0
    # zip 함수를 사용해 한 번에 처리
    for num, sign in zip(absolutes, signs):
        if sign == True:
            answer += num
        else:
            answer -= num
    return answer