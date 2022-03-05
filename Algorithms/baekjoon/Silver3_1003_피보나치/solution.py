

T = int(input())
for tc in range(T):
    n = int(input())
    dp = [[1, 0], [0, 1]]
    if n == 0:
        print(dp[0][0], dp[0][1])
    elif n == 1:
        print(dp[1][0], dp[1][1])
    else:
        for i in range(2, n+1):
            cnt_0 = dp[i-1][0] + dp[i-2][0]
            cnt_1 = dp[i-1][1] + dp[i-2][1]
            dp.append([cnt_0, cnt_1])
        print(dp[n][0], dp[n][1])