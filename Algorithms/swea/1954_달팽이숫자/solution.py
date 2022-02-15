def solution(n):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    # n * n matrix 초기화
    matrix = [[0 for i in range(n)] for j in range(n)]

    # 현재 위치
    row, col = 0, 0
    idx = 0


    for i in range(1, n*n+1):

        matrix[row][col] = i
        row, col = row + dx[idx], col + dy[idx]

        # matrix[row][col]이 matrix index범위를 넘어가거나 이미 다른 숫자로 채워졌을 경우
        if not(0 <= row < n) or not(0 <= col < n) or matrix[row][col] != 0:
            row, col = row - dx[idx], col - dy[idx]
            idx = (idx + 1) % 4
            row, col = row + dx[idx], col + dy[idx]
    return matrix


T = int(input())

for tc in range(T):
    n = int(input())
    answer_matrix = solution(n)
    print(f'#{tc + 1}')
    for r in answer_matrix:
        answer = ' '.join(map(str, r))
        print(answer)