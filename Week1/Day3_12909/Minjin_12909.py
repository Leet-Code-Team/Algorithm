def solution(s):
    # 스택 생성
    stack = []
    for i in s:
        # 스택 값 추가
        if i == "(":
            stack.append(i)
        else:
            # 스택 값 제거
            if len(stack) != 0:
                stack.pop()
            # 스택의 길이가 0이면, ")" 앞에 "("가 없으므로 False 값을 리턴
            else:
                return False
    return len(stack) == 0