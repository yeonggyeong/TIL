# 행, 열을 하나씩 순회하며 연속된 1의 개수가 k와 같은지 확인
def get_count(N, K, matrix):

    total = 0
    for col in range(N):
            count = 0
            for row in range(N):
                if matrix[col][row] == 0:
                    if count == K:
                        total += 1
                    count = 0
                else:
                    count += 1
            if count == K:
                total += 1

    for row in range(N):
            count = 0
            for col in range(N):
                if matrix[col][row] == 0:
                    if count == K:
                        total += 1
                    count = 0
                else:
                    count += 1
            if count == K:
                total += 1
    return total

T = int(input())

for tc in range(T):
    N, K = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    answer = get_count(N, K, matrix)

    print(f'#{tc+1} {answer}')