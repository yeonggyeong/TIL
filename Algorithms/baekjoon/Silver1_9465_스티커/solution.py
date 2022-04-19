
T = int(input())

for tc in range(T):
    N = int(input())

    matrix = [list(map(int, input().split())) for _ in range(2)]

    '''
    50 10 100 20 40
    30 50 70  10 60 
    '''
    '''
    50 40 200 140 250
    30 100 120 210 260
    '''
    dp = [[0 for _ in range(N)] for _ in range(2)]

    dp[0][0] = matrix[0][0]
    dp[1][0] = matrix[1][0]

    for col in range(1, N):
        if col == 1:
            dp[0][col] = dp[1][col-1] + matrix[0][col]
            dp[1][col] = dp[0][col-1] + matrix[1][col]
        else:
            dp[0][col] = max(dp[1][col-2], dp[1][col-1]) + matrix[0][col]
            dp[1][col] = max(dp[0][col-2], dp[0][col-1]) + matrix[1][col]

    print(max(dp[0][N-1], dp[1][N-1]))