T = int(input())

for tc in range(T): 
    n, m = map(int, input().split())
    matrix = [list(input()) for _ in range(n)]

    # 행에서 찾기
    for row in matrix:
        for col in range(0, n-m+1):
            if row[col:col+m] == row[col:col+m][::-1]:
                answer = row[col:col+m]

    # 열에서 찾기
    for col in range(n):
        col_matrix = [i[col] for i in matrix]
        for row in range(0, n-m+1):
            if col_matrix[row:row+m] == col_matrix[row:row+m][::-1]:
                answer = col_matrix[row:row+m]

    answer = ''.join(answer)
    print(f'#{tc+1} {answer}')