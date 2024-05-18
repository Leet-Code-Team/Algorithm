def solution(absolutes, signs):
    result = 0
    # i를 signs 길이만큼 반복 
    for i in range(len(signs)):
        # signs[i]가 False일 때 음의 부호를 곱하여 result에 더함 
        if signs[i] == False:
            result += absolutes[i]*(-1)
        # True일 때 양의 부호로 더함 
        else:
            result += absolutes[i]
    return result 