def solution(n):
    # n의 2진수에서의 "1"의 갯수
    bin_n = format(n, "b")
    len_n = bin_n.replace("0", "")

    num = n
    len_num = 0
    # 숫자를 늘려가며 2진수에서의 "1"의 갯수를 비교
    while len_num != len_n:
        num += 1
        bin_num = format(num, "b")
        len_num = bin_num.replace("0", "")

    return num