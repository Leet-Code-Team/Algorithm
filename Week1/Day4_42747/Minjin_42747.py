def solution(citations):
    # n: 논문의 편수
    n = len(citations)
    citations = sorted(citations, reverse=True)
    # citat: 인용 수, (idx+1): citat 이상의 논문 수
    for idx, citat in enumerate(citations):
        # 해당 논문의 citat가 (idx+1)보다 작거나 같을 경우, h의 후보값 중 최대값을 return
        if (idx+1) >= citat:
            return max(idx, citat)
    # 모든 논문의 citat가 (idx+1)보다 큰 값을 갖는 경우, h의 최대값인 n을 return
    return n