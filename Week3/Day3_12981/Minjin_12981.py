def solution(n, words):
    for idx in range(1, len(words)):
        # 앞 단어의 마지막 알파벳과 뒷 단어의 첫 번째 알파벳을 비교 or 같은 단어가 나왔는지 확인
        if words[idx-1][-1] != words[idx][0] or words[idx] in words[:idx]:
            return [idx%n + 1, idx//n + 1]
    return [0, 0]