from collections import deque

N, M, K = map(int, input().split())

fireballs = deque()
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    fireballs.append([r-1, c-1, m, s, d])

matrix = [[[] for _ in range(N)] for _ in range(N)]

for fireball in fireballs:
    matrix[fireball[0]][fireball[1]].append(fireball[2:])

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]


for _ in range(K):

    while fireballs:
        # 행, 열, 질량, 속도, 방향
        r, c, m, s, d = fireballs.popleft()

        new_r, new_c = (r + s * dx[d]) % N, (c + s * dy[d]) % N 
        matrix[new_r][new_c].append([m, s, d])
        matrix[r][c] = []

    for row in range(N):
        for col in range(N):
            if len(matrix[row][col]) >= 2:
                fire_m, fire_s, cnt, cnt_odd = 0, 0, 0, 0
                for fire in matrix[row][col]:
                    fire_m += fire[0]
                    fire_s += fire[1]
                    cnt += 1
                    if fire[2] % 2:
                        cnt_odd += 1
                
                fire_m = fire_m // 5
                fire_s = fire_s // cnt

                if cnt == cnt_odd or cnt == 0:
                    fire_d = [0, 2, 4, 6]
                else:
                    fire_d = [1, 3, 5, 7]
                
                if fire_m > 0:
                    for idx in range(4):
                        fireballs.append([row, col, fire_m, fire_s, fire_d[idx]])
            
            elif len(matrix[row][col]) == 1:
                fireballs.append([row, col, m, s, d])

print(matrix)
