# dp 안 쓰고 풀기
# 시간초과로 정답 확인 불가능
import heapq

def solution():
    max_score = 0

    while True:
        if not heap:
            return max_score
        # 점수가 가장 높은 스티커 떼기
        sticker = heapq.heappop(heap)
        # 이미 떼어진 스티커면 다른 스티커 떼기
        while matrix[sticker[1][0][0]][sticker[1][0][1]] < 0:
            if heap:
                sticker = heapq.heappop(heap)
            else:
                return max_score

        max_score += sticker[0]
        # 뗄 수 있는 스티커와 뗄 수 없는 스티커 분배
        for i, j in sticker[1]:
            if matrix[i][j] != -1:
                matrix[i][j] = -1


T = int(input())

for tc in range(T):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(2)]
    heap = []

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for row in range(2):
        for col in range(N):
            # 현재 위치를 떼면 뗄 수 없는 스티커들의 정보
            share = [(row, col)]
            for idx in range(4):
                new_row, new_col = row + dx[idx], col + dy[idx]
                if 0 <= new_row < 2 and 0 <= new_col < N:
                    share.append((new_row, new_col))
            # 최대힙을 만들기 위해 가장 첫번째값에 '-'
            heapq.heappush(heap, [-matrix[row][col], share])
    answer = solution()

    print(-answer)