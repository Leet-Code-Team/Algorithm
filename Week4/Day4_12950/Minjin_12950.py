def solution(arr1, arr2):
    # 이중 for문을 이용해 arr1에 직접 더함.
    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            arr1[i][j] += arr2[i][j]
    return arr1