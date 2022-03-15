def dfs():
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    stack = [[1, 1]]

    while stack:
        x, y = stack.pop()

        for idx in range(4):
            new_x, new_y = x + dx[idx], y + dy[idx]
            # 인덱스 범위를 벗어나지 않는 new_x, new_y
            if 0 <= new_x < 16 and 0 <= new_y < 16:
                # 도착점이라면 바로 1 반환
                if matrix[new_x][new_y] == '3':
                    return 1
                # 길이라면 999로 바꾸고 길을 stack 추가
                elif matrix[new_x][new_y] == '0':
                    matrix[new_x][new_y] = 999
                    stack.append((new_x, new_y))
    return 0

for tc in range(10):
    answer = 0
    n = int(input())
    matrix = [list(input()) for _ in range(16)]
    answer = dfs()
    print(f'#{tc+1} {answer}')