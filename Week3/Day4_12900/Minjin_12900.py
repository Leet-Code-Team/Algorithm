def solution(n):
    n1, n2 = 1, 2
    for i in range(1,n):
        n1, n2 = n2, n1+n2
    return n1%1000000007