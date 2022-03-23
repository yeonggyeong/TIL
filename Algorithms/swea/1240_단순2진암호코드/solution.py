
def find_code(N, M):
    matrix = [list(input()) for _ in range(N)]

    # 시작 행 index 찾기
    for row in range(N):
        if '1' in matrix[row]:
            start_row = row
            break

    # 마지막 열 index 찾기
    for col in range(M-1, -1, -1):
        if '1' in [i[col] for i in matrix]:
            end_col = col
            break
    
    # 암호 첫줄만 추출
    for i in matrix[start_row:start_row+1]:
        new_matrix = i[col-55:end_col+1]


    dic = {'0001101':0, '0011001':1, '0010011':2, '0111101':3, '0100011':4, '0110001':5, '0101111':6,
            '0111011':7, '0110111':8, '0001011':9}

    # 이진암호문을 숫자로 변경
    code = []
    for j in range(0, len(new_matrix), 7):
        binary_number = ''.join(new_matrix[j:j+7])
        number = dic[binary_number]
        code.append(int(number))
    
    return code

def check_code(code):

    odd_sum = 0
    even_sum = 0
    for idx in range(8):
        if idx == 7:
            last_number = code[idx]
        elif idx % 2:
            even_sum += code[idx]
        else:
            odd_sum += code[idx]

    if (odd_sum * 3 + even_sum + last_number) % 10:
        return 0
    else:
        return sum(code)

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    code = find_code(N, M)
    answer = check_code(code)
    print(f'#{tc+1} {answer}')
