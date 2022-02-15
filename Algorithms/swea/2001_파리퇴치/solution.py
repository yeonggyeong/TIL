def solution(n, m):

    matrix = []
    for _ in range(n):
        matrix.append(list(map(int,input().split())))

    # m의 크기만큼 matrix를 쪼갠 후, 합을 구하기
    max_v = 0
    for row in range(n-m+1):
        for col in range(n-m+1):
            new_matrix = [i[col:col+m] for i in matrix[row:row+m]]
            sum_m = 0
            for r in new_matrix:
                for c in r:
                    sum_m += c

            if sum_m > max_v:
                max_v = sum_m

    return max_v

T = int(input())

for tc in range(T):
    n, m = map(int, input().split())
    answer = solution(n, m)
    
    print(f'#{tc+1} {answer}')