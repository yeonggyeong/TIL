import sys
sys.setrecursionlimit(10 ** 6)

def dfs(row, col):
    
    # 지렁이의 움직임
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for idx in range(4):
        row, col = row+dx[idx], col+dy[idx]

        # 밭을 넘어가지 않고 배추가 있다면 dfs 반복
        if 0 <= row < N and 0 <= col < M and matrix[row][col] != 0:
            matrix[row][col] = 0
            dfs(row, col)
        row, col = row-dx[idx], col-dy[idx]


T = int(input())

for tc in range(T):
    M, N, K = map(int, input().split())

    matrix = [[0] * M for _ in range(N)]

    # 배추가 있는 곳 변경
    for _ in range(K):
        x, y = map(int, input().split())
        matrix[y][x] = 1
    
    # 지렁이 개수 count
    cnt = 0
    for x in range(N):
        for y in range(M):
            if matrix[x][y] != 0:
                cnt += 1
                matrix[x][y] = 0
                dfs(x, y)

    print(cnt)