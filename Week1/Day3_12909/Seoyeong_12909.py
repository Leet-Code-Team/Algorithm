def solution(s):
    stack = []
    for i in s: 
        # for문으로 s의 문자 하나씩 확인하는데 ( 인 경우 stack에 추가 
        if i == '(':
            stack.append(i)
        else: 
            # 스택이 비어있다는 것은 올바른 괄호가 아님을 의미 ( 가 없기 때문에 
            # False 반환
            if stack == []:
                return False 
            # 그 외의 경우에는 stack에서 가장 최근에 추가된 ( 를 제거 
            # -> ( 와 ) 가 짝을 이루었다는 뜻
            else: 
                stack.pop() 
    # stack이 비어 있다면 ( 와 ) 가 모두 짝을 이루었으므로 True 반환됨   
    return stack == []