def solution(s):
    answer = ''
    # 공백으로 단어의 첫 문자를 판별함.
    idx = 0
    for i in s:
        if i == ' ':
            answer += i
            idx = 0
        elif idx == 0:
            answer += i.upper()
            idx += 1
        else:
            answer += i.lower()
            idx += 1
    return answer