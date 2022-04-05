
def solution(s):
    distances[0] = 0

    for _ in range(N-1):
        min_idx = -1
        min_val = float('inf')
        for i in range(N):
            # 해당 섬을 방문하지 않고 최소비용보다 작다면
            if not visited[i] and distances[i] < min_val:
                min_idx = i
                min_val = distances[i]

        visited[min_idx] = 1

        for i in range(N):
            if matrix[min_idx][i] and not visited[i]:
                weight = matrix[min_idx][i]
                if weight < distances[i]:
                    distances[i] = weight



T = int(input())
for tc in range(T):
    N = int(input())
    # x 좌표
    x = list(map(int, input().split()))
    # y 좌표
    y = list(map(int, input().split()))
    E = float(input())

    matrix = [[0 for _ in range(N)] for _ in range(N)]
    for row in range(N):
        for col in range(N):
            # 각 섬끼리의 비용을 matrix형태로 저장
            dist = ((x[row]-x[col])**2+(y[row]-y[col])**2)*E
            matrix[row][col] = dist
            matrix[row][col] = dist


    distances = [float('inf')] * N
    visited = [0 for _ in range(N)]


    s = 0
    solution(s)
    answer = round(sum(distances))
    print(f'#{tc+1} {answer}')

