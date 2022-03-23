
def dfs(x, y, string):
    global total

    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    # 문자열의 길이가 7이면 함수 종료
    if len(string) == 7:
        total.append(string)
        return

    for idx in range(4):
        new_x = x + dx[idx]
        new_y = y + dy[idx]
        if 0 <= new_x < 4 and 0 <= new_y < 4:
            dfs(new_x, new_y, string + matrix[new_x][new_y])

T = int(input())
for tc in range(T):
    matrix = [list(input().split()) for _ in range(4)]

    total = []
    for row in range(4):
        for col in range(4):
            dfs(row, col, '')
    
    answer = len(set(total))

    print(f'#{tc+1} {answer}')
