import sys
sys.stdin = open('input.txt')


def charging_bus(k, N):
    charges = list(map(int, input().split()))

    current_lo = 0
    cnt = 0

    while current_lo + k < N:
        for n in range(current_lo+k, current_lo, -1):
            if n in charges:
                cnt += 1
                current_lo = n
                break
        else:
            cnt = 0
            break

    return cnt


T = int(input())

for tc in range(T):
    k, N, m = map(int, input().split())
    answer = charging_bus(k, N)
    print(f'#{tc+1} {answer}')