def solution(n):
    answer =  n + 1
    # True일 때까지 반복    
    while True: 
        # n과 answer의 이진수를 구하고 1의 갯수를 계산
        n_count = format(n, 'b').count("1")
        answer_count = format(answer, 'b').count("1")
        # 이진수로 변환한 뒤의 1의 갯수가 같다면 break
        if (n_count == answer_count): break
        answer += 1 
    return answer