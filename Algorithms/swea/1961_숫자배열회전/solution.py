
# 90도씩 회전해서 matrix 저장
def get_matrix(n, matrix, results):
    rotate_matrix = [[''] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rotate_matrix[i][j] = matrix[n-1-j][i]

        results.append(''.join(rotate_matrix[i]))

    return rotate_matrix, results

T = int(input())

for tc in range(T):
    
    n = int(input())

    matrix = [list(map(str, input().split())) for _ in range(n)]
    results = []

    # 90도 회전한 결과에 90도 회전을 해 180도 회전한 matrix 생성
    # 180도 회전한 matrix에 90도 회전 해 270도 회전한 matrix 생성
    first_rotate, results = get_matrix(n, matrix, results)
    second_rotate, results = get_matrix(n, first_rotate, results)
    thrid_rotate, results = get_matrix(n, second_rotate, results)

    print(f'#{tc+1}')
    for i in range(n):
        for j in range(3):
            print(results[i+ j * n], end = ' ')
        print()