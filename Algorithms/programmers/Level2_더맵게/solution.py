import heapq

def solution(scoville, K):
    answer = 0

    # 최대힙으로 변경
    heapq.heapify(scoville)

    # 비어있을때
    if not scoville:
        return -1

    while scoville:
        # 비어 있지 않을때
        min_food = heapq.heappop(scoville)

        # 스코빌 지수가 제일 낮은 음식이 k보다 높을때
        # answer 반환
        if min_food >= K:
            return answer

        # 섞을 음식이 없으면 -1 반환
        if not scoville:
            return -1
        second_food = heapq.heappop(scoville)

        # 음식 섞기
        heapq.heappush(scoville, min_food + second_food * 2)
        answer += 1
    return -1