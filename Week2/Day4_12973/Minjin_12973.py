def solution(s):
    # 이중 for문을 사용할 경우, 시간 초과가 발생할 수 있음. -> stack 활용
    stack = []
    for i in s:
        if len(stack) == 0:
            stack.append(i)
        elif stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
    return 1 if len(stack)==0 else 0