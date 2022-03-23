
def get_cost(costs, plans):
    dp = [0 for _ in range(13)]

    for idx in range(1, len(plans)):
        # 한 달전의 최소비용 + ( 이번달 이용 계획 * 1일권 , 한달이용권의 최솟값 )
        dp[idx] = dp[idx-1] + min(plans[idx] * costs[0], costs[1])

        # 위에서 정한 최소비용, 3달전 최소비용 + 3달 이용권의 최솟값
        if idx-2 >= 1:
            dp[idx] = min(dp[idx], dp[idx-3] + costs[2])
   
        # 12월의 최소비용과 1년 이용권의 최솟값
        dp[-1] = min(dp[-1], costs[-1])

    return dp[-1]



T = int(input())

for tc in range(T):
    costs = list(map(int, input().split()))
    # idx 맞춰주기 위해서 0이 있는 리스트
    plans = [0]
    lst = list(map(int, input().split()))
    plans.extend(lst)

    answer = get_cost(costs, plans)

    print(f'#{tc+1} {answer}')