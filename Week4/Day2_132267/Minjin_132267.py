def solution(a, b, n):
    answer = 0
    # 몫과 나머지를 이용해 새로 얻은 콜라(new_cola)와 기존의 콜라(cola)를 구함.
    while n >= a:
        new_cola = (n//a)*b
        n = n%a + new_cola
        answer += new_cola
    return answer