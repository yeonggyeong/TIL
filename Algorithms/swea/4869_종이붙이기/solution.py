
def solution(n):
    # N=10일때와 20일때는 초기값으로 설정
    dp = [1, 3]

    # N일때 , N의 길이는 N-1에 20 * 10 하나 추가
    #       , N의 길이는 N-2에 20 * 20, 10*20 (가로로 2개) 추가한 것과 같음 / 
    #         20 * 10 (세로 2개)추가 한것도 같지만 N-1에 20*10 추가한 것도 동일하기 때문에 제외
    for i in range(2, N):
        dp.append(dp[i-1] + dp[i-2] * 2)

    return dp[N-1]


T = int(input())

for tc in range(T):

    N = int(input()) // 10

    answer = solution(N)
    print(f'#{tc+1} {answer}')