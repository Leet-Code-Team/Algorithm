def solution(n):
    # n0, n1은 각각 F(0), F(1) 값을 나타냄.
    n0, n1 = 0, 1
    for i in range(2, n+1):
        # n_2, n_1은 각각 F(n-2), F(n-1) 값을 나타냄.
        if i == 2:
            fibo = n0 + n1
            n_2, n_1 = n1, fibo
        else:
            fibo = n_2 + n_1
            n_2, n_1 = n_1, fibo
    return fibo%1234567