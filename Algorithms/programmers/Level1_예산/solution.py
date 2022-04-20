def solution(d, budget):
    
    sort_d = sorted(d)
    answer = 0 
    for i in sort_d:
        # 현재 부서의 예산이 총 예산보다 적다면 
        # 예산 - 현재 부서의 예산
        if i <= budget:
            budget -= i
            answer += 1
        # 사용 가능한 예산이 0이거나 현재 부서의 예산이 크면 중지
        elif budget == 0 or i > budget:
            return answer 
    return answer