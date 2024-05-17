def solution(s):
    # 공백제거 
    s = s.replace(' ', '')
    stack = []
    
    # 문자열을 하나씩 스택에 추가
    for i in s:
        if(len(stack) == 0):
            stack.append(i)
        # 스택의 top 값과 현재 문자 값이 같은 경우 스택에 추가하지 않고 top값을 pop
        elif(stack[-1] == i):
            stack.pop()
        else:
            stack.append(i)

    # 스택이 비어있는 경우 1을, 아닌 경우 0을 리턴  
    if(len(stack) == 0):
        return 1
    else:
        return 0