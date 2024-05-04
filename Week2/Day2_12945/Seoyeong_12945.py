def solution(n):
    answer = []
    # 
    for i in range(n+1):
        # i가 0이나 1일 때 f(0)과 f(1)을 각각 값으로 반환
        if i==0 or i==1:
            answer.append(i)
        # 2이상의 n이 입력되었을 때 F(n) = F(n-1) + F(n-2)를 적용
        # fibo를 1234567로 나눈 값을 answer에 추가
        else:
            fibo = answer[i-1] + answer[i-2]
            answer.append(fibo % 1234567)
    # 가장 마지막 값 반환
    return answer[-1]