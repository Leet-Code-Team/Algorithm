# 가로를 a, 세로를 b라고 가정할 때 
# yellow = (a-2)*(b-2)

def solution(brown, yellow):
    answer = []
    total = brown + yellow
    for a in range (1, total+1):
        # 전체 갯수에서 가로를 나눴을 때 나머지가 0이라면 (약수라는 의미)
        # ex) a=4, b=3이라면 total=12, 12/4=3
        if total % a == 0:
            # 세로는 전체에서 a를 나눈 값과 같다 
            b = total/a
            # a >= b이며 (a-2)*(b-2) = yellow가 성립한다면 a,b 값을 반환
            if a >= b:
                if (a - 2) * (b - 2) == yellow:
                 return [a, b]
              
    return answer