import sys
sys.stdin = open('input.txt')

# 행의 최댓값
def sum_row(matrix):
    max_r = 0
    for row in range(100):
        sum_r = 0
        for col in range(100):
            sum_r += matrix[row][col]
        if max_r < sum_r:
            max_r = sum_r
    return max_r 

# 열의 최댓값
def sum_col(matrix):
    max_c = 0
    for col in range(100):
        sum_c = 0
        for row in range(100):
            sum_c += matrix[row][col]
        if max_c < sum_c:
            max_c = sum_c
    return max_c

# 대각선의 최댓값
def sum_cross(matrix):
    sum_cross = 0
    sum_cross_2 = 0
    for v in range(100):
        sum_cross += matrix[v][v]
        sum_cross_2 += matrix[v][99-v]  
    
    max_cross = sum_cross if sum_cross > sum_cross_2 else sum_cross_2
    return max_cross

# 행, 열, 대각선의 최댓값 중에 가장 큰 수 찾기
def get_max(lst):
    result = lst[0]
    for element in lst[1:]:
        if element > result:
            result = element
    return result

for tc in range(10):
    num = int(input())
    matrix = []
    for i in range(100):
        matrix.append(list(map(int, input().split())))

    max_r, max_c, max_cross = sum_row(matrix), sum_col(matrix), sum_cross(matrix)
    max_lists = [max_r, max_c, max_cross]
    result = get_max(max_lists)
    print(f'#{tc+1} {result}')