import sys
sys.stdin = open('input.txt')

T = int(input())

# 최댓값을 마지막 날로 설정하고 뒤에서부터 앞으로 반복
# 만약, 값이 작다면 answer에 추가
def get_profit(days, prices):
    max_price = prices[-1]
    answer = 0

    for i in range(days-2, -1, -1):
        if prices[i] >= max_price:
            max_price = prices[i]
        else:
            answer = answer + max_price - prices[i]

    return answer

for tc in range(T):
    days = int(input())
    prices = list(map(int, input().split()))
    
    answer = get_profit(days, prices)
    print(f'#{tc+1} {answer}')
        
        