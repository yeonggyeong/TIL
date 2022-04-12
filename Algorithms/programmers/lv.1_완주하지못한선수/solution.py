def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    # 정렬 후 순서가 다르면 그 참가자 반환
    # 모두 같다면 마지막에 남은 참가자 반환
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    
    return participant[-1]