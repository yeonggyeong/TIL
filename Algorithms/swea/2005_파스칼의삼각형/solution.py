def get_triangle(n):
    matrix = [[] for _ in range(n)]

    for i in range(n):
        # 각 행 처음은 1로 추가 
        matrix[i].append(1)
        # 첫번째 행이라면 건너뛰기 -> 오직 1만 추가
        if i == 0:
            continue
        # 두번째 행이라면 [1, 1] 로 합을 사용하지 않고 추가
        elif i == 1:
            matrix[i].append(1)
        else:
        # 세번째 이후 행이라면, 양쪽 끝을 제외하고 index 1부터 행인덱스 -1까지 위의 두 원소의 합 추가
            for j in range(1, i):
                matrix[i].append(matrix[i-1][j-1] + matrix[i-1][j])
            matrix[i].append(1)
    return matrix


T = int(input())

for tc in range(T):
    n = int(input())

    matrix = get_triangle(n)
    print(f'#{tc+1}')
    for row in matrix:
        for col in row:
            print(col, end=' ')
        print()