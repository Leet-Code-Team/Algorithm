def solution(a, b):
    answer = 0
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]

    # 총 일 수 구하기
    for i in range(a-1):
        answer += months[i]
    answer += b
    
    return days[(answer%7) - 1]