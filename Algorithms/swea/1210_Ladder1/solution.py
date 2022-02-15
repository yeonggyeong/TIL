# x 위치( 당첨 위치 ) 찾기
# 마지막 행의 요소 중 값이 2인 row, col 찾기
def find_x(matrix):
    for c in range(len(matrix[-1])):
        if matrix[-1][c] == 2:
            return c


# 당첨위치 부터 시작해서 당첨 사다리 찾기
def find_start(matrix, x_col):
    dx = [-1, 0, 1, 0]  # 상 좌 하 우
    dy = [0, -1, 0, 1]

    # 현재위치는 x 부터 시작이 아닌 x자리 바로 윗자리에서 시작
    # x 자리는 양옆이랑 위가 전부 1이기 때문
    row, col = 99 - 1, x_col

    # 현재위치의 row index가 0이 될때까지 반복
    # 돌아가는 걸 방지하기 위해서 지나온 자리는 99로 변경
    while row != 0:
        matrix[row][col] = 99
        # 현재위치의 왼쪽이 1이라면 왼쪽으로 이동/ 이때, col-1은 범위를 벗어나지 않아야 함
        if (0 <= col - 1 < 100) and (matrix[row][col - 1] == 1):
            idx = 1
            row, col = row + dx[idx], col + dy[idx]
        # 현재위치의 오른쪽이 1이라면 오른쪽으로 이동/ 이때, col+1은 범위를 벗어나지 않아야 함
        elif (0 <= col + 1 < 100) and matrix[row][col + 1] == 1:
            idx = 3
            row, col = row + dx[idx], col + dy[idx]
        else:
            idx = 0
            row, col = row + dx[idx], col + dy[idx]
    return col


for tc in range(10):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(100)]

    x_col = find_x(matrix)
    answer = find_start(matrix, x_col)
    print(f'#{tc+1} {answer}')
