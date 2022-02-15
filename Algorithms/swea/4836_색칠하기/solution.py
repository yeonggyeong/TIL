# matrix 색칠하기위한 함수
def draw_matrix(start_x, start_y, end_x, end_y, color, matrix, cnt):
    for row in range(start_x, end_x+1):
        for col in range(start_y, end_y+1):
            # 색이 겹치는 부분 -> 0이 아닌 부분과 같은 색이 아닌 부분은 구별하기 위해 99로 변환
            # 겹치는 부분을 변환해줄때마다 cnt += 1 실행하여 몇 칸이 겹치는지 count
            if matrix[row][col] != 0 and matrix[row][col] != color:
                matrix[row][col] = 99
                cnt += 1
            else:
                matrix[row][col] = color
    return matrix, cnt


T = int(input())

for tc in range(T):
    n = int(input())
    matrix = [[0 for i in range(10)] for i in range(10)]
    # 겹치는 부분을 count하기 위한 변수 선언
    cnt = 0
    # n번만큼 색칠하기
    for _ in range(n):
        start_x, start_y, end_x, end_y, color = map(int, input().split())
        matrix, cnt = draw_matrix(start_x, start_y, end_x, end_y, color, matrix, cnt)

    print(f'#{tc+1} {cnt}')