def solution(brown, yellow):
    # m, n은 각각 가로 또는 세로의 길이
    m, n = 0, 0
    # m의 값을 조절하여 풀이
    while (brown+yellow) != m*n:
        m += 1
        # n을 m을 이용해 표현, m*n - (m-2)*(n-2) = brown 식을 정리하면 구할 수 있음.
        n = ((brown+4)/2 - m)
    return sorted([m, n], reverse=True)