def dfs(i, j, direction_type, dessert):
    global answer

    if direction_type < 3: 
        tmp = direction_type + 2 
    else: 
        tmp = direction_type + 1

    for k in range(direction_type, tmp):
        new_x = i + directions[k][0]
        new_y = j + directions[k][1]
        if start[0] == new_x and start[1] == new_y:
            answer = max(answer, dessert)
            return

        if 0 <= new_x < N and 0 <= new_y < N:
            if visited[matrix[new_x][new_y]] == False:
                visited[matrix[new_x][new_y]] = True
                dfs(new_x, new_y, k, dessert+1)
                visited[matrix[new_x][new_y]] = False


T = int(input())

for tc in range(T):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    visited = [False for _ in range(101)]
    answer = -1
    directions = [(1, 1), (1, -1), (-1, -1), (-1, 1)] 
    for i in range(N):
        for j in range(N):
            start = [i, j]
            visited[matrix[i][j]] = True
            dfs(i, j, 0, 1) 
            visited[matrix[i][j]] = False 
            
    print(f'#{tc+1} {answer}')