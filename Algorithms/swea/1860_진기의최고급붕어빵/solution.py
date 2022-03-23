
def make_bread(M, K, customers):
    # 붕어빵을 구워야하는 최대 시간
    max_time = max(customers)

    bread = [0 for _ in range(max_time+1)]

    for time in range(max_time+1):
        # 0초가 아니면 time-1초때의 붕어빵의 개수를 가져오기
        if time != 0:
            bread[time] += bread[time-1]
            # 붕어빵이 다 구워지면 추가
            if not time % M:
                bread[time] += K

    # 손님이 오는시간 정렬
    customers.sort()  

    for customer in customers:
        # 손님이 오는 시간에 붕어빵이 있다면
        # 현재 시간부터 최대시간까지 붕어빵의 개수 -1
        if bread[customer] > 0:
            for i in range(customer, max_time+1):
                bread[i] -= 1
        else:
            return 'Impossible'
    
    return 'Possible'

T = int(input())

for tc in range(T):
    N, M, K = map(int, input().split())
    customers = list(map(int, input().split()))

    answer = make_bread(M, K, customers)
    print(f'#{tc+1} {answer}')