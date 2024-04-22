def solution(s):
    # s를 공백을 기준으로 분리한 뒤 모든 요소를 int로 변환 
    # list(map(함수, 리스트))를 통해 리스트로 변환 
    arr = list(map(int, s.split(' ')));    
    # sort 사용해서 오름차순으로 정렬
    arr.sort();           
    #  arr의 0번째(최솟값)와 -1번째(최댓값) return 
    answer = str(arr[0]) + " " + str(arr[-1]);                     
    return answer; 