
def dfs(i, j):
    # 현재위치도 방문으로 변경
    visited[i][j] = 1
    # 상 우 하 좌
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    # 도착지면 1 반환
    if matrix[i][j] == 3:
        return 1
    
    else:
        # 4 방향
        for idx in range(4):
            x = i + dx[idx]
            y = j + dy[idx]
            # 인덱스를 벗어나지 않고 길이 있다면, 방문 하지 않았다면 반복
            if 0 <= x < N and 0 <= y < N and matrix[i][j] != 1:
                if not visited[x][y]:
                    dfs(x, y)


T = int(input())

for tc in range(T):
    N = int(input())

    matrix = [list(map(int, input())) for _ in range(N)]

    # 출발지, 도착지 찾기
    for row in range(N):
        for col in range(N):
            if matrix[row][col] == 2:
                start = [row, col]
            if matrix[row][col] == 3:
                end = [row, col]

    # 방문 여부를 확인할 matrix 생성
    visited = [[0] * N for _ in range(N)]
    dfs(start[0], start[1])
    print(f'#{tc+1} {visited[end[0]][end[1]]}')