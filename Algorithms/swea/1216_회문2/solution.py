
for tc in range(10):
    n = int(input())
    matrix = [list(input()) for _ in range(100)]

    # 행 우선 탐색
    max_length = 1
    for row in matrix:
        for col in range(0, 100):
            for end in range(99, -1,-1):
                if row[col:end+1] == row[col:end+1][::-1]:
                    answer = len(row[col:end+1])
                    max_length = answer if answer > max_length else max_length

    # 열 탐색
    for col in range(100):
        col_matrix = [i[col] for i in matrix]
        for row in range(0, 100):
            for end in range(99, -1, -1):
                if col_matrix[row:end+1] == col_matrix[row:end+1][::-1]:
                    answer = len(col_matrix[row:end+1])
                    max_length = answer if answer > max_length else max_length

    print(f'#{n} {max_length}')