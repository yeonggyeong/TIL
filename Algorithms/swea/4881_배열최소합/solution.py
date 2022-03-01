def get_minsum(row):
    global sum_part, min_sum

    if min_sum < sum_part:
        return

    # 마지막 row일때    
    if row == N:
        if sum_part < min_sum:
            min_sum = sum_part
        return

    for col in range(N):
        # 해당 column이 선택되지 않았다면
        if not selected[col]:
            selected[col] = 1
            sum_part += matrix[row][col]
            get_minsum(row+1)
            selected[col] = 0
            sum_part -= matrix[row][col]

T = int(input())

for tc in range(T):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]    
    # N개의 숫자 선택
    selected = [0] * N 
    sum_part = 0
    min_sum = 9999

    get_minsum(0)
    print(f'#{tc+1} {min_sum}')