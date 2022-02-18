
def solution(matrix):
    numbers = list(range(1,10))

    # 행 확인
    for row in range(9):
        for number in numbers:
            if number not in matrix[row]:
                return 0
            else:
                answer = 1

    # 열 확인
    for col in range(9):
        col_matrix = [i[col] for i in matrix]
        for number in numbers:
            if number not in col_matrix:
                return 0 
            else:
                answer = 1

    # 3 * 3 행렬 검증
    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            new_matrix = [i[col:col+3] for i in matrix[row:row+3]]
            new_matrix = [element for new in new_matrix for element in new]
            for number in numbers:
                if number not in new_matrix:
                    return 0 
                else:
                    answer = 1
    return answer

T = int(input())

for tc in range(T):
    matrix = [list(map(int, input().split())) for _ in range(9)]
    answer = solution(matrix)
    print(f'#{tc+1} {answer}')