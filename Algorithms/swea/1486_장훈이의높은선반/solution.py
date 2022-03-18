from itertools import combinations

T = int(input())

for tc in range(T):
    N, B = map(int, input().split())

    heights = list(map(int, input().split()))

    minimun = 99
    # 1부터 n개까지의 부분집합
    for i in range(1, N+1):
        for combination in list(combinations(heights, i)):
            # 부분집합의 합이 장훈의 키보다 높다면
            if sum(combination) >= B:
                temp_min = sum(combination) - B

                if temp_min < minimun:
                    minimun = temp_min

    print(f'#{tc+1} {minimun}')
