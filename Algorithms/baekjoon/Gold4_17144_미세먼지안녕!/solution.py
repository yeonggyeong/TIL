import sys

def operate_air_cleaner(air_cleaner):
    # 반시계 방향
    for i in range(air_cleaner[0]-2, -1, -1):
        matrix[i+1][0] = matrix[i][0]

    for j in range(1, C):
        matrix[0][j-1] = matrix[0][j]

    for k in range(1, air_cleaner[0]+1):
        matrix[k-1][C-1] = matrix[k][C-1]

    for l in range(C-2, 0, -1):
        matrix[air_cleaner[0]][l+1] = matrix[air_cleaner[0]][l]

    matrix[air_cleaner[0]][1] = 0

    # 시계 방향
    for i in range(air_cleaner[1]+2, R):
        matrix[i-1][0] = matrix[i][0]

    for j in range(1, C):
        matrix[R-1][j-1] = matrix[R-1][j]

    for k in range(R-2, air_cleaner[1]-1, -1):
        matrix[k+1][C-1] = matrix[k][C-1]

    for l in range(C-2, 0, -1):
        matrix[air_cleaner[1]][l+1] = matrix[air_cleaner[1]][l]

    matrix[air_cleaner[1]][1] = 0


R, C, T = map(int, sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]

# 공기청정기 위치 찾기
for i in range(R):
    if -1 in matrix[i]:
        air_cleaner = (i, i+1)
        break

dx = [-1, 0, 0, 1]
dy = [0, 1, -1, 0]

for t in range(T):
    temp = []
    for row in range(R):
        for col in range(C):
            # 미세먼지 값이 5 이상인 위치만 찾기
            if matrix[row][col] >= 5:
                dust = matrix[row][col] // 5
                cnt = 0
                for idx in range(4):
                    new_x, new_y = row + dx[idx], col + dy[idx]
                    if 0 <= new_x < R and 0 <= new_y < C and matrix[new_x][new_y] != -1:
                        cnt += 1
                        temp.append((dust, new_x, new_y))
                
                matrix[row][col] = matrix[row][col] - dust * cnt
    for d, x, y in temp:
        matrix[x][y] += d

    operate_air_cleaner(air_cleaner)
    
answer = sum([sum(i) for i in matrix])
print(answer + 2)