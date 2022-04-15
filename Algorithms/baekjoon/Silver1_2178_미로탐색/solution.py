from collections import deque

def bfs(x, y):
    dx = [-1, 1, 0, 0] 
    dy = [0, 0, -1, 1]

    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
    
        for idx in range(4):
            new_x, new_y = x + dx[idx], y + dy[idx]

            # 갈 수 있는 곳이면 현재 위치까지 올 수 있는 거리에 +1
            if 0 <= new_x < N and 0 <= new_y < M and matrix[new_x][new_y] == 1:
                matrix[new_x][new_y] = matrix[x][y] + 1
                queue.append((new_x, new_y))
      
    return matrix[N-1][M-1]


N, M = map(int, input().split())

matrix = [list(map(int, list(input()))) for _ in range(N)]
answer = bfs(0, 0)
print(answer)