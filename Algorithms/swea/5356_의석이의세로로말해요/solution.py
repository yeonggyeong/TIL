# 글자마다 길이가 다르기 때문에 최대 길이 찾기
# 글자마다 길이가 다르기 때문에 세로로 출력할때 빈 값이 있으면 넘어가야함
# 따라서 조건문을 통해 값이 있는지 없는지 판별하여 출력
def solution(matrix):

    length = 0
    for row in matrix:
        if len(row) > length:
            length = len(row)

    answers = []
    for col in range(length):
        for i in matrix:
            if len(i) > col:
                answers.append(i[col])
    return answers

T = int(input())

for tc in range(T):
    matrix = [list(map(str, input())) for i in range(5)]
    answers = solution(matrix)
    answer = ''.join(answers)
    print(f'#{tc+1} {answer}')